📘 Personal RAG Assistant (Flask + ChromaDB + Perplexity API)

A fully functional Retrieval-Augmented Generation (RAG) application built with Flask, ChromaDB, SentenceTransformers, and the Perplexity API.
This system ingests personal .txt files, converts them into embeddings, stores them locally in a vector database, and answers user questions using contextual retrieval.

Designed for privacy, modularity, and real-world AI integration.

🚀 Features

🔍 Semantic Search over your personal text data

🧠 Embeddings using SentenceTransformers (all-MiniLM-L6-v2)

🗂 Local Vector Storage using ChromaDB

🤖 LLM Answering via Perplexity Sonar model

🔐 Privacy First — personal data never leaves your machine

🌐 Flask Web Interface for easy interaction

📁 Automatic loading of all .txt files from /data folder

🏗 Project Structure
flask_rag_app/
│
├── app.py                 # Flask server
├── rag.py                 # RAG engine (embedding, retrieval, LLM)
├── requirements.txt       # Dependencies
├── .env                   # PERPLEXITY_API_KEY
├── data/                  # Personal text files (user-provided)
├── vectorstore/           # ChromaDB persistent storage
├── templates/
│     ├── index.html       # Query input page
│     └── result.html      # Answer page
└── static/
      └── styles.css       # Optional styling

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

2️⃣ Create Virtual Environment (Python 3.10)
py -3.10 -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Perplexity API Key

Create a .env file:

PERPLEXITY_API_KEY=your_api_key_here

5️⃣ Add Your Personal Text Files

Place all .txt files inside:

data/

6️⃣ Run the Application
python app.py


Open in browser:

http://127.0.0.1:5000/

🔧 How It Works
📝 1. Data Ingestion

The app loads all .txt files from /data on startup.

🧩 2. Text Chunking

Long text is split into smaller meaningful chunks.

📐 3. Embedding Generation

Using all-MiniLM-L6-v2 from SentenceTransformers.

🗄 4. Vector Storage

Chunks + embeddings + metadata are stored in ChromaDB.

🔍 5. Semantic Retrieval

A user query is embedded → nearest relevant chunks are retrieved.

🤖 6. Answer Generation

Chunks + question are sent to Perplexity, which generates the final answer.

📦 requirements.txt
Flask==3.0.3
chromadb==0.5.0
sentence-transformers==2.6.1
transformers==4.40.2
torch==2.2.2
typing_extensions==4.12.1
requests==2.31.0
python-dotenv==1.0.1

📊 Result

The app accurately answers questions grounded in personal knowledge.

Retrieval quality is strong due to high-quality embeddings.

Perplexity generates accurate, concise responses.

🛠 Future Improvements

PDF and image OCR ingestion

Chat history system

Multi-user authentication

Deployment on Render/HuggingFace Spaces

Streamlit UI version

🧑‍💻 Author

Sandeep Kumar
AI & Software Enthusiast
Open to collaborations and new projects 🚀
