from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import chromadb

OLLAMA_HOST = "http://localhost:11434"

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url=OLLAMA_HOST
)

chroma_client = chromadb.HttpClient(host="localhost", port=8000)
vectorstore = Chroma(
    client=chroma_client,
    collection_name="rag_context_langchain",
    embedding_function=embeddings,
)

# from clients import chroma_collection
# print(chroma_collection.peek())