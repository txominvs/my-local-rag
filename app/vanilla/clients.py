import ollama
import chromadb

OLLAMA_HOST = "http://localhost:11434"
ollama_client = ollama.Client(host=OLLAMA_HOST)

chroma_client = chromadb.HttpClient(host="localhost", port=8000)
chroma_collection = chroma_client.get_or_create_collection("rag_context")