from modules.db_ingestor import ingest_docs
from modules.paths_reference import ROOT_PATH
import pandas as pd
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings

def run():
    embeddings = OllamaEmbeddings(model="llama3.1")
    df = pd.read_excel(ROOT_PATH / "data" / "Speeches_corpus_translated.xlsx")
    ingest_docs(df, embeddings)

if __name__ == "__main__":
    load_dotenv()
    run()