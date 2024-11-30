import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import openai

# Set your API keys for OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize OpenAI Embeddings using LangChain
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Specify which embedding model

# Connect to the Pinecone index using LangChain's Pinecone wrapper
pinecone_index_name = "langchain-embeddings-demo"
vectorstore = PineconeVectorStore(index_name=pinecone_index_name, embedding=embeddings)

# Define your documents
texts = ["This is a hardcoded first text component.", "Here is the hardcoded second text component.", "Here is the hardcoded third text component."]
metadata = [{"id": 1}, {"id": 2}, {"id": 3}]  # Metadata for each document, for example

# Create embeddings and upsert to Pinecone
vectorstore.add_texts(texts=texts, metadatas=metadata)

print("Embeddings from hard-coded text components created and inserted in Pinecone Vector Database successfully!")
