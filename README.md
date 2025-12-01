Slack LLM Assistant 🤖💬

A real-time Slack chatbot powered by the Groq Llama 3.1 LLM, built using Python and Slack Bolt (Socket Mode).
This bot listens to messages in Slack, sends them to an LLM, and replies instantly inside Slack channels.

🚀 Features

✔ Real-time Slack bot using Socket Mode
✔ Uses Groq API (Llama 3.1 8B Instant) for ultra-fast LLM responses
✔ Reads API keys securely from .env (NOT stored in code)
✔ Can answer questions, explain concepts, chat, help with tasks
✔ Clean modular code (chatbot.py + slack_llm_bot.py)

🛠️ Tech Stack

Python 3.x

Slack Bolt SDK

Socket Mode

Groq LLM (Llama-3.1-8B-Instant)

dotenv for environment variables

📁 Project Structure
llm console bot/
│── slack_llm_bot.py       # Slack bot handler (events, replies)
│── chatbot.py             # LLM integration using Groq API
│── .env                   # API tokens (not uploaded to GitHub)
│── .gitignore             # Hides .env from Git
│── README.md              # Documentation
│── requirements.txt       # Python dependencies

🔧 Setup Instructions
1. Clone Repository
git clone https://github.com/shravyaz/slack-llm-assistant.git
cd slack-llm-assistant

2. Install Dependencies
pip install -r requirements.txt

3. Create .env
GROQ_API_KEY=your_groq_api_key
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-level-token

4. Run the Slack Bot
python slack_llm_bot.py


Your bot will now respond inside Slack 🎉

🧠 How It Works

A user sends a message or mentions the bot in Slack.

Slack sends the event to your Socket Mode bot.

Your slack_llm_bot.py receives the message and extracts text.

Text is passed to LLM via Groq API in chatbot.py.

The bot sends back the LLM-generated reply to Slack.

✨ Demo (Concept)

User:

@Shravya-LLM-Assistant explain sockets in python

Bot:

Sockets allow two systems to communicate over a network…

📜 License

This project is for learning and portfolio purposes.