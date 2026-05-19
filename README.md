# 💬 Conversational AI Chatbot with Memory

> A stateful multi-turn AI chatbot that actually remembers what you said — powered by LangChain memory modules and Streamlit.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.3.1-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.57.0-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 What

**Conversational AI Chatbot with Memory** is a Streamlit web application that enables true multi-turn conversations with an AI — where the model remembers everything said earlier in the session, just like ChatGPT.

This project implements **LangChain's memory management system**: conversation history is stored, managed, and passed back to the LLM on every turn — making it context-aware across the entire session.

---

## 💡 Why

Most LLM tutorials show a single question → answer. Real products require **conversation state**.

Without memory, every message is treated as a brand-new conversation — the AI has no idea who you are, what you just said, or what the conversation is about. Memory management is one of the most critical skills for building production chatbots, and interviewers always ask: *"How do you handle conversation state?"*

This project demonstrates:
- The most in-demand LangChain conversational skill in AI engineering roles
- How to manage and persist memory across Streamlit UI reruns
- The difference between buffer memory and windowed memory — and when to use each

---

## ⚙️ How It Works

```
User Message → Memory Buffer → ConversationChain → ChatOpenAI → Response → Memory Buffer
```

1. **Input** — User types a message in the Streamlit chat interface
2. **Memory** — `ConversationBufferMemory` appends the message to the running history
3. **Chain** — `ConversationChain` packages full history + new message and sends to the LLM
4. **Response** — ChatGPT-3.5-turbo generates a context-aware reply
5. **Update** — Response is appended back into memory for the next turn
6. **Persist** — Streamlit `session_state` keeps memory alive across UI reruns

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12 | Core language |
| LangChain | 1.3.1 | Conversation chain & memory orchestration |
| LangChain Community | 0.4.1 | Community integrations |
| LangChain OpenAI | 1.2.1 | ChatOpenAI wrapper |
| LangChain Core | 1.4.0 | Base interfaces & primitives |
| OpenAI | 2.37.0 | GPT-3.5-turbo API access |
| Streamlit | 1.57.0 | Web UI |
| python-dotenv | 1.2.2 | Environment variable management |

---

## 📁 Folder Structure

```
conversational-ai-chatbot-with-memory/
├── app.py                    # Streamlit UI entry point
├── requirements.txt          # Project dependencies
├── .env.example              # OPENAI_API_KEY=your_key_here
├── README.md
└── src/
    ├── chat_engine.py        # ConversationChain + memory setup
    ├── memory_manager.py     # Buffer vs windowed memory logic
    └── ui_components.py      # Streamlit chat bubble styling
```

---

## 📦 Requirements

```txt
# LangChain ecosystem
langchain==1.3.1
langchain-community==0.4.1
langchain-openai==1.2.1
langchain-core==1.4.0

# OpenAI
openai==2.37.0

# UI
streamlit==1.57.0

# Environment variables
python-dotenv==1.2.2
```

> Install all dependencies at once:
> ```bash
> pip install -r requirements.txt
> ```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.12** installed
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Shuaibiqbal/conversational-ai-chatbot-with-memory
cd conversational-ai-chatbot-with-memory

# 2. Create a virtual environment with Python 3.12
python3.12 -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Set up environment variables
cp .env.example .env
# Open .env and add your OpenAI API key:
# OPENAI_API_KEY=sk-...

# 7. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🔑 Key Concepts Demonstrated

- **ConversationBufferMemory** — Stores the complete chat history and passes it to the LLM on every turn
- **ConversationBufferWindowMemory** — Keeps only the last K turns, preventing context window overflow on long chats
- **ConversationChain** — Wraps the LLM and memory into a single callable pipeline
- **Streamlit session_state** — Persists memory across UI reruns without resetting the conversation
- **Chat UI Design** — Styled user vs AI chat bubbles for a clean, production-like interface

---

## 🗺️ Roadmap

- [ ] Add `ConversationSummaryMemory` for very long sessions
- [ ] Allow users to switch memory type (Buffer / Window / Summary) from the UI
- [ ] Add system prompt customization (persona, tone, role)
- [ ] Export conversation history as `.txt` or `.pdf`
- [ ] Deploy to Streamlit Cloud
- [ ] Add token usage tracking per session

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Shuaib Iqbal**
- GitHub: [@Shuaibiqbal](https://github.com/Shuaibiqbal)
- ORCID: [0000-0002-1894-8217](https://orcid.org/0000-0002-1894-8217)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> ⭐ If you found this project helpful, please consider giving it a star on GitHub!
