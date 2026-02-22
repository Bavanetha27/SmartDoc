# 📘 SmartDoc – AI-Powered Document Assistant

**SmartDoc** is a web-based AI platform that allows users to upload large PDF documents and ask questions to get **instant, intelligent answers**. Built with **Streamlit**, **LangChain**, and **FAISS**, SmartDoc provides a secure, session-based, SaaS-style experience for document Q&A.

---

## 🔹 Features

* **Upload Large PDFs** – Efficiently process hundreds of pages using intelligent chunking.
* **AI-Powered Q&A** – Ask natural language questions and get accurate contextual answers.
* **Session-Based Security** – Each user’s documents and queries are isolated for privacy.
* **User Authentication** – Register and login functionality with MongoDB backend.
* **Processing Logs** – Sidebar log tracks document processing in real-time.
* **SaaS UI** – Modern, dark-themed interface with animations and hover effects.

---

## 🛠 Tech Stack

| Layer                  | Technology                        |
| ---------------------- | --------------------------------- |
| Frontend               | Streamlit                         |
| Backend / Logic        | Python, LangChain, FAISS          |
| Embeddings             | HuggingFace Sentence-Transformers |
| Database               | MongoDB                           |
| PDF Parsing            | PyPDF                             |
| Environment Management | python-dotenv                     |
| Deployment             | Streamlit Cloud / Docker / Local  |

---

## 💻 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/SmartDoc.git
cd SmartDoc
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
```

Activate:

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit langchain langchain-community langchain-huggingface faiss-cpu sentence-transformers pypdf pymongo python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_google_genai_key
MONGO_URI=mogodb_url
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🗂 Project Structure

```
SmartDoc/
│
├── app.py               # Main entry point
├── utils.py             # RAG pipeline and helper functions
├── db.py                # db logic
├── data/                # Uploaded documents
├── pages/               # Streamlit multipage structure
│   ├── 1_Register.py
│   ├── 2_Login.py
│   └── 3_AI_Chat.py
├── requirements.txt
└── .env                 # API keys & environment variables
```

---

## 🔐 Authentication

* **MongoDB** stores user credentials securely.
* Only authenticated users can access the AI document Q&A page.
* Users can logout to clear session and logs.

---

## ⚡ Usage

1. Upload a PDF document.
2. The system indexes the document using FAISS embeddings.
3. Ask questions in natural language.
4. See answers along with processing logs.

---

## 🌐 Deployment Options

* **Streamlit Cloud** – Deploy directly from GitHub.
* **Docker** – Containerized deployment.
* **Local Network** – Use `--server.address 0.0.0.0` for LAN access.

---

## 📦 Future Improvements

* Multi-document support.
* Chat history storage.
* More AI models support (Gemini, GPT, etc.).
* Enhanced SaaS UI with subscription management.
* Offline document processing.

---

## 📄 License

MIT License © 2026


