import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_llm(prompt: str) -> str:
    """
    Send a message to the LLM and get the reply.
    """
    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_completion_tokens=512,
    )

    reply_text = chat_completion.choices[0].message.content.strip()
    return reply_text


def main():
    print("Simple LLM Chatbot (type 'exit' to quit)")
    print("----------------------------------------")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Bye! 👋")
            break

        try:
            bot_reply = ask_llm(user_input)
            print("Bot:", bot_reply)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
