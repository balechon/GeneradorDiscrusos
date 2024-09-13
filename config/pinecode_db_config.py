import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_community.embeddings import OllamaEmbeddings

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = os.getenv("INDEX_NAME")


if INDEX_NAME not in pc.list_indexes():
    pc.create_index(
        name=INDEX_NAME,
        dimension = 4096,
        metric = "cosine",
        spec = ServerlessSpec(
            cloud = "aws",
            region = "us-east-1"
        )
    )


index = pc.Index(INDEX_NAME)
