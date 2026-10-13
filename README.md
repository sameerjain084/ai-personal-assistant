# 🤖 AI Personal Assistant

An AI-powered personal assistant built using **Flask, Python, and Google's Gemini API**. Ask questions, get AI-generated answers, and summarize long emails through a simple and user-friendly web interface.

## ✨ Features

- 💬 **AI Chat Assistant** — Ask questions and receive AI-generated responses.
- 📧 **Email Summarizer** — Summarize lengthy emails into concise, easy-to-understand summaries.
- ⚡ **Fast Responses** — Powered by Google's Gemini generative AI models.
- 🎨 **Clean User Interface** — Simple, responsive interface built with HTML and CSS.
- 🔐 **Secure API Configuration** — API keys managed through environment variables.
- 🐍 **Python Backend** — Flask handles API requests and application logic.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and routing |
| Google Gemini API | AI-generated responses |
| Google Gen AI SDK | Gemini API integration |
| HTML5 | Web page structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
ai-personal-assistant/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

> **Note:** The `.env` file contains your API key and should never be committed to GitHub.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sameerjain084/ai-personal-assistant.git
cd ai-personal-assistant
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the project's root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your actual API key.

### 5. Run the application

```bash
python main.py
```

Open your browser and visit:

**http://127.0.0.1:5000/**

## 💡 How to Use

### AI Chat Assistant
1. Enter your question in the **Ask Anything** field.
2. Click **Ask**.
3. Read the AI-generated response.

### Email Summarizer
1. Paste the email content into the **Summarize Email** field.
2. Click **Summarize**.
3. Review the generated summary.

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | API key used to authenticate Gemini API requests |

Keep your `.env` file private. Never hardcode API keys in your source code or share them publicly.

## 🔒 Security

- Store API keys in environment variables.
- Exclude `.env` from version control using `.gitignore`.
- Never upload credentials, tokens, or other sensitive information to GitHub.
- Use production-grade deployment settings before hosting the application publicly.



## 👨‍💻 Author

**Sameer Jain**

B.Tech Computer Science Engineering | Cloud Computing and Automation

- GitHub: [@sameerjain084](https://github.com/sameerjain084)
- LinkedIn: [Sameer Jain](https://www.linkedin.com/in/sameer-jain-7836b7216/)

## 📄 License

This project is open source and available under the MIT License, provided you add an appropriate `LICENSE` file to the repository.

---

⭐ If you find this project useful, consider giving the repository a star!
