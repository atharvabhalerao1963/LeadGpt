import pandas as pd

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# =====================================================
# ABSOLUTE PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

VECTOR_DB_PATH = BASE_DIR / "vector_db"

print("\nDATASET PATH:")
print(DATA_PATH)

print("\nVECTOR DB PATH:")
print(VECTOR_DB_PATH)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(DATA_PATH)

print("\nDATASET LOADED SUCCESSFULLY")
print(df.head())

# =====================================================
# CREATE DOCUMENTS
# =====================================================

documents = []

for _, row in df.iterrows():

    content = f"""
    Created Date: {row['Created']}
    Product ID: {row['Product_ID']}
    Lead Source: {row['Source']}
    Mobile Number: {row['Mobile']}
    Email: {row['EMAIL']}
    Sales Agent: {row['Sales_Agent']}
    Location: {row['Location']}
    Delivery Mode: {row['Delivery_Mode']}
    Status: {row['Status']}
    """

    documents.append(
        Document(page_content=content)
    )

print(f"\nTOTAL DOCUMENTS CREATED: {len(documents)}")

# =====================================================
# EMBEDDING MODEL
# =====================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================================================
# CREATE VECTOR DATABASE
# =====================================================

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=str(VECTOR_DB_PATH)
)

print("\nVECTOR DATABASE CREATED SUCCESSFULLY")