from pathlib import Path

from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# =====================================================
# DATASET PATH
# =====================================================

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

# =====================================================
# VECTOR DB PATH
# =====================================================

VECTOR_DB_PATH = BASE_DIR / "vector_db"

# =====================================================
# LOAD CSV
# =====================================================

loader = CSVLoader(
    file_path=str(DATA_PATH)
)

documents = loader.load()

# =====================================================
# SPLIT DOCUMENTS
# =====================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================================================
# VECTOR DATABASE
# =====================================================

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory=str(VECTOR_DB_PATH)
)

vectorstore.persist()

# =====================================================
# SUCCESS MESSAGE
# =====================================================

print("✅ Vector DB Created Successfully")