# 🧠 Tweet Logger: GPT Chat Logging API

A lightweight Flask API that logs GPT-style conversations into a PostgreSQL database. Designed to integrate with a Custom GPT, store logs via webhooks, and generate tweetable content automatically.

## 🚀 Features

- Accepts chat messages from GPT interactions via HTTP POST
- Stores `user_message` and `assistant_reply` with timestamps
- Connects to a PostgreSQL database (e.g. AWS RDS)
- Deployable to Render, AWS, or any Python-friendly host

---

## 🧰 Tech Stack

- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL
- Render / AWS (hosted backend)
- OpenAI Custom GPT (future integration)
- Twitter Bot (for automated tweets)

---

## 📦 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/tweet-logger.git
cd tweet-logger
