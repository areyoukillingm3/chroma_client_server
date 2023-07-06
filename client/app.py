import chromadb
import chromadb.config
from chromadb.server.fastapi import FastAPI

settings = chromadb.config.Settings(
    chroma_api_impl="rest",
    chroma_server_host="localhost",
    chroma_server_http_port="8000"
)
chroma_client = chromadb.Client(settings)
server = FastAPI(settings)
app = server.app()
chroma_client.create_collection('test')
print(chroma_client.list_collections())
chroma_client.reset()