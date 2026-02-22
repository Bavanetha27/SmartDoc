import os
from dotenv import load_dotenv
from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

DATA_FOLDER = "data"

def create_rag_pipeline(uploaded_file, log_func=None):

    os.makedirs("data", exist_ok=True)

    file_path = os.path.join("data", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if log_func:
        log_func("📁 File saved to data folder")

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    if log_func:
        log_func(f"📖 Extracted {len(documents)} pages")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)

    if log_func:
        log_func(f"✂ Split into {len(docs)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if log_func:
        log_func("🔎 Generating embeddings...")

    vectorstore = FAISS.from_documents(docs, embeddings)

    if log_func:
        log_func("🗂 Stored in FAISS")

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