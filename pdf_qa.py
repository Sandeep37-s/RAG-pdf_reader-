import os
import requests
import warnings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Ignore harmless LangChain / HuggingFace warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# === STEP 1: Create Vector Store from PDF ===
def create_pdf_vectorstore(pdf_path):
    """Loads PDF, splits text, embeds it, and stores in FAISS."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Use free local embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


# === STEP 2: Ask OpenRouter ===
def ask_openrouter(prompt):
    """Sends a chat completion request to OpenRouter API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # Optional metadata for OpenRouter logs
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "AI PDF Reader"
    }

    payload = {
        "model": "gpt-3.5-turbo",  # You can change to: "mistralai/mixtral-8x7b", "nousresearch/hermes-2-pro", etc.
        "messages": [
            {"role": "system", "content": "You are a helpful assistant answering questions from PDF content."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ OpenRouter API Error:", e)
        return "⚠️ Unable to connect to OpenRouter API. Please check your internet or API key."


# === STEP 3: Generate Answer from PDF Context ===
def get_pdf_answer(vectorstore, question):
    """Retrieves relevant chunks from PDF and asks OpenRouter."""
    retriever = vectorstore.as_retriever()
    # LangChain v0.2+ requires run_manager=None for internal call
    relevant_docs = retriever._get_relevant_documents(question, run_manager=None)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"Answer the question based only on the following PDF content:\n\n{context}\n\nQuestion: {question}"
    answer = ask_openrouter(prompt)
    return answer
