import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai

# Set your API keys for OpenAI 
openai.api_key = os.environ['OPENAI_API_KEY']

# Initialize OpenAI Embeddings using LangChain
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Specify which embedding model

# Load and split document
loader = TextLoader("video_001501/coastal-marine-synopsis/Central-Bay-of-Compeche.txt")  # Load a text file
documents = loader.load()

# Use a TextSplitter to split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=50)
split_documents = text_splitter.split_documents(documents)

# Connect to the Pinecone index using LangChain's Pinecone wrapper
# Add the splitDocuments into Pinecone
pinecone_index_name = "langchain-embeddings-demo"
vectorstore = PineconeVectorStore(index_name=pinecone_index_name, embedding=embeddings)
vectorstore.add_documents(documents=split_documents )

print("Embeddings from single text file created and inserted in Pinecone Vector Database successfully!")
