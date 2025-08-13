import os
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import pandas as pd
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

if __name__ == '__main__':
    print("Ingesting...")

    file = pd.read_csv("Cocktails.csv", encoding="utf-8")

    documents = [
        Document(
            page_content=f"{row['description']} Flavor profile: {row['flavor_profile']}",
            metadata={"name": row["name"], "base_spirit": row["base_spirit"],"strength": row["alcohol_strength"]}
        )
        for _, row in file.iterrows()
    ]

    # loader = CSVLoader("/Users/Warren/intro-to-vector-dbs/Cocktails.csv", encoding="utf-8")
    # document = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPEN_API_KEY"))
    #embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    PineconeVectorStore.from_documents(documents, embeddings, index_name=os.environ['INDEX_NAME'])
    print("Finish!")