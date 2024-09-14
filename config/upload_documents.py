from modules.db_ingestor import ingest_docs
from modules.paths_reference import ROOT_PATH
import pandas as pd
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from tqdm.auto import tqdm
def run():
    embeddings = OllamaEmbeddings(model="llama3.1")
    df = pd.read_json(ROOT_PATH / "data" / "Speeches_corpus.json", lines=True,encoding="utf-8")
    df = df.query("origin == 'ted talks'")
    # print(df.columns)
    progress_bar = tqdm(total=len(df))
    for i in range(0, len(df), 5):
        ingest_docs(df.iloc[i:i+5], embeddings)
        progress_bar.update(5)

if __name__ == "__main__":
    load_dotenv()
    run()