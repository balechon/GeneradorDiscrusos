from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document



def split_text(text, chunk_size=2000, chunk_overlap=0):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_text(text)
def ingest_docs(df,embeddings):
    # Load the documents

    #
    documents = []
    for _, row in df.iterrows():
        chunks = split_text(row['translated_speech'])
        for chunk in chunks:
            documents.append(Document(
                page_content= chunk,
                metadata= {'titulo': str(row['title']), 'source': str(row['origin'])}
            ))

    # processed_df = pd.DataFrame(documents)
    # loader = DataFrameLoader(processed_df, page_content_column="content")
    # documents = loader.load()

    print("\ncargando documentos")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name="discursos-largos"
    )
    print("carga completa")



