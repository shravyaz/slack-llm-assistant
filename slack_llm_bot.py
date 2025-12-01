import os
from dotenv import load_dotenv
from groq import Groq
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load variables from .env into environment
load_dotenv()




# ---------- 1. CONFIG: READ FROM ENV ONLY ----------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")


# ---------- 2. GROQ CLIENT + LLM FUNCTION ----------

client = Groq(api_key=GROQ_API_KEY)

def ask_llm(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_completion_tokens=512,
    )

    reply_text = completion.choices[0].message.content.strip()
    return reply_text

# ---------- 3. SLACK APP SETUP ----------
app = App(token=SLACK_BOT_TOKEN)

@app.event("message")
def handle_message(event, say):
    print("\n💬 Received message event from Slack:")
    print(event)

    if event.get("subtype") == "bot_message":
        return

    text = event.get("text", "").strip()
    if not text:
        return

    tokens = text.split()
    if tokens and tokens[0].startswith("<@") and tokens[0].endswith(">"):
        text_for_llm = " ".join(tokens[1:])
    else:
        text_for_llm = text

    try:
        reply = ask_llm(text_for_llm)
    except Exception as e:
        reply = f"Oops, error talking to LLM: {e}"

    say(reply)

# ---------- 4. START APP ----------

def main():
    print("Starting Slack LLM Bot... (Ctrl+C to stop)")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()
