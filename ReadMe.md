# 📄 AI PDF Summarizer (Streamlit + Groq API)

An AI-powered web application that summarizes PDF documents using **Groq LLM (Llama 3)** and Streamlit.

---

## 🚀 Features

- 📤 Upload PDF files easily  
- 📖 Extract text automatically using PyPDF2  
- 🤖 AI-powered summarization using Groq API  
- ⚡ Fast responses with `llama-3.1-8b-instant`  
- 📏 Smart text handling (limits input to 2000 characters)  
- 🌐 Simple and clean Streamlit interface  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🎈  
- Groq API 🤖  
- PyPDF2 📄  
- python-dotenv 🔐  

---

## 📁 Project Structure


AI-PDF-Summarizer/
│
├── app.py
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash

git clone https://github.com/your-username/ai-pdf-summarizer.git
cd ai-pdf-summarizer

2️⃣ Create virtual environment (optional)

python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies

pip install -r requirements.txt
🔑 API Key Setup

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

👉 Get your API key here: https://console.groq.com/keys

▶️ Run the Application

streamlit run app.py

Then open in your browser:

http://localhost:8501

📌 How It Works

User uploads a PDF file
Text is extracted using PyPDF2
Text is trimmed to 2000 characters (token safety)
Sent to Groq LLM (Llama 3 model)
AI generates a summary

Output is displayed in Streamlit UI

⚠️ Limitations

Only first 2000 characters are processed
Large PDFs may lose some information
Requires active internet connection

🔥 Future Improvements
📚 Full PDF chunk-based summarization
💬 Chat with PDF (ChatGPT-like system)
📊 Better UI design
💾 Download summary as PDF
🧠 Memory-based AI assistant


👨‍💻 Author
Thirumal Jeegari