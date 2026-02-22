import os
from dotenv import load_dotenv
from google import genai

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

DATA_FOLDER = "data"


def create_rag_pipeline(uploaded_file, log_func):

    os.makedirs(DATA_FOLDER, exist_ok=True)

    file_path = os.path.join(DATA_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    log_func("📁 Saved to data folder")

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    log_func(f"📖 Extracted {len(documents)} pages")

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)
    log_func(f"✂ Split into {len(docs)} chunks")

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    log_func("🔎 Generating Embeddings...")

    vectorstore = FAISS.from_documents(docs, embeddings)
    log_func("🗂 Stored in FAISS Vector Database")

    return vectorstore


def ask_question(vectorstore, question):

    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Answer ONLY using the provided context.

        Context:
        {context}

        Question:
        {question}
        """
    )

    return response.text