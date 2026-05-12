# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings

# from groq import Groq
# from dotenv import load_dotenv

# import os

# # =========================================================
# # LOAD ENV VARIABLES
# # =========================================================

# load_dotenv()

# # =========================================================
# # GROQ LLM CLIENT
# # =========================================================

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # =========================================================
# # EMBEDDING MODEL
# # =========================================================

# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # =========================================================
# # LOAD CHROMA VECTOR DATABASE
# # =========================================================

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# VECTOR_DB_PATH = BASE_DIR / "vector_db"

# print("\nVECTOR DB PATH:")
# print(VECTOR_DB_PATH)

# vectorstore = Chroma(
#     persist_directory=str(VECTOR_DB_PATH),
#     embedding_function=embedding_model
# )

# collection = vectorstore._collection

# print("\nTOTAL DOCUMENTS INSIDE VECTOR DB:")
# print(collection.count())
# # =========================================================
# # RETRIEVER
# # =========================================================

# retriever = vectorstore.as_retriever(
#     search_kwargs={"k": 5}
# )

# # =========================================================
# # MAIN RAG FUNCTION
# # =========================================================

# def ask_rag(question: str):

#     try:

#         # =================================================
#         # RETRIEVE DOCUMENTS
#         # =================================================

#         docs = retriever.invoke(question)

#         print("\n" + "=" * 60)
#         print("RETRIEVED DOCUMENTS")
#         print("=" * 60)

#         if not docs:
#             print("No documents retrieved from vector database.")

#             return {
#                 "answer": "No relevant sales records were found in the database."
#             }

#         # =================================================
#         # PRINT RETRIEVED DOCS FOR DEBUGGING
#         # =================================================

#         for i, doc in enumerate(docs):

#             print(f"\nDOCUMENT {i+1}")
#             print("-" * 40)
#             print(doc.page_content)

#         # =================================================
#         # CREATE CONTEXT
#         # =================================================

#         context = "\n\n".join(
#             [doc.page_content for doc in docs]
#         )

#         # =================================================
#         # ADVANCED SALES ANALYST PROMPT
#         # =================================================

#         prompt = f"""
# You are LeadGPT, an advanced AI-powered Business and Sales Intelligence Assistant.

# Your role is to analyze sales, leads, revenue, customer performance, business trends, and operational insights using ONLY the provided business data context.

# =========================================================
# INSTRUCTIONS
# =========================================================

# 1. Use ONLY the provided context data.
# 2. Never hallucinate or create fake information.
# 3. If the answer is present:
#    - provide direct business insights
#    - mention exact names
#    - include numerical values
#    - summarize findings professionally
# 4. If rankings are requested:
#    - rank properly
#    - include values where possible
# 5. If comparisons are requested:
#    - compare clearly
#    - highlight better and worse performers
# 6. Keep responses concise but professional.
# 7. Format the response cleanly using bullet points when useful.
# 8.If exact information is unavailable,
# provide the closest possible insight based on the retrieved business records."

# =========================================================
# BUSINESS CONTEXT DATA
# =========================================================

# {context}

# =========================================================
# USER QUESTION
# =========================================================

# {question}

# =========================================================
# PROFESSIONAL ANSWER
# =========================================================
# """

#         # =================================================
#         # LLM RESPONSE
#         # =================================================

#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",

#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are an expert AI Sales Analyst and "
#                         "Business Intelligence Assistant."
#                     )
#                 },
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],

#             temperature=0.2,
#             max_tokens=700
#         )

#         final_answer = response.choices[0].message.content

#         # =================================================
#         # RETURN RESPONSE
#         # =================================================

#         return {
#             "answer": final_answer
#         }

#     except Exception as e:

#         print("\nERROR IN RAG PIPELINE")
#         print(str(e))

#         return {
#             "answer": f"Error occurred: {str(e)}"
#         }




from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv
import os
from pathlib import Path

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

# =========================================================
# GROQ LLM CLIENT
# =========================================================

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# =========================================================
# EMBEDDING MODEL
# =========================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================================================
# LOAD CHROMA VECTOR DATABASE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
VECTOR_DB_PATH = BASE_DIR / "vector_db"

print("\nVECTOR DB PATH:")
print(VECTOR_DB_PATH)

vectorstore = Chroma(
    persist_directory=str(VECTOR_DB_PATH),
    embedding_function=embedding_model
)

collection = vectorstore._collection

print("\nTOTAL DOCUMENTS INSIDE VECTOR DB:")
print(collection.count())

# =========================================================
# RETRIEVER
# =========================================================

retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# =========================================================
# MAIN RAG FUNCTION (ENHANCED)
# =========================================================

def ask_rag(question: str):
    try:
        # =================================================
        # RETRIEVE DOCUMENTS
        # =================================================

        docs = retriever.invoke(question)

        print("\n" + "=" * 60)
        print("RETRIEVED DOCUMENTS")
        print("=" * 60)

        if not docs:
            print("No documents retrieved from vector database.")
            return {
                "answer": "No relevant sales records were found in the database."
            }

        # =================================================
        # PRINT RETRIEVED DOCS FOR DEBUGGING
        # =================================================

        for i, doc in enumerate(docs):
            print(f"\nDOCUMENT {i+1}")
            print("-" * 40)
            print(doc.page_content)

        # =================================================
        # CREATE CONTEXT
        # =================================================

        context = "\n\n".join([doc.page_content for doc in docs])

        # =================================================
        # ADVANCED PROMPT (IMPROVED)
        # =================================================

        prompt = f"""You are LeadGPT, an advanced AI-powered Business and Sales Intelligence Assistant.

Your expertise spans:
- Sales analysis and forecasting
- Lead quality assessment
- Revenue trend analysis
- Customer performance metrics
- Business intelligence insights

Key Principles:
1. Accuracy First: Only use provided data. Never fabricate numbers or names.
2. Clarity: Present findings in a structured, professional manner.
3. Actionability: Provide insights that drive business decisions.
4. Completeness: Address all aspects of the question when possible.
5. Honesty: Acknowledge data limitations explicitly.

=========================================================
BUSINESS CONTEXT DATA
=========================================================

{context}

=========================================================
ANALYSIS INSTRUCTIONS
=========================================================

Answer the following question based ONLY on the provided context data:

• Extract and present specific facts with exact numbers and names
• Provide rankings when relevant, with supporting metrics
• Make clear comparisons when the question asks for it
• Structure your response for professional readability
• If certain information is missing, note it explicitly
• Provide 2-3 key insights or recommendations based on the data

=========================================================
USER QUESTION
=========================================================

{question}

=========================================================
PROFESSIONAL ANALYSIS
=========================================================
"""

        # =================================================
        # LLM RESPONSE (IMPROVED PARAMETERS)
        # =================================================

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI Sales Analyst and Business Intelligence Assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.15,
            max_tokens=800,
            top_p=0.9,
            frequency_penalty=0.1
        )

        final_answer = response.choices[0].message.content

        # =================================================
        # RETURN RESPONSE
        # =================================================

        return {
            "answer": final_answer,
            "documents_found": len(docs),
            "status": "success"
        }

    except Exception as e:
        print("\nERROR IN RAG PIPELINE")
        print(str(e))
        return {
            "answer": f"Error occurred: {str(e)}",
            "status": "error"
        }