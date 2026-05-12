from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# LOAD CSV

loader = CSVLoader(
    file_path="/Users/atharvabhalerao/Desktop/LeadGPT/backend/app/data/project_sales_data.csvVector DB Created SuccessfullyVector DB Created SuccessfullyVector DB Created SuccessfullyVector DB Created SuccessfullyVector DB Created Successfully"
)

documents = loader.load()

# SPLIT DOCUMENTS

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# EMBEDDING MODEL

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# VECTOR DATABASE

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="../../vector_db"
)

vectorstore.persist()

print("Vector DB Created Successfully")