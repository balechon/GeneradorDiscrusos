from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

class SpeechGenerator:
    def __init__(self):
        load_dotenv()
        self.index_name = os.getenv("INDEX_NAME")
        self.embeddings = OllamaEmbeddings(model="llama3.1")
        # self.llm = OllamaLLM(model="llama3.1")
        self.llm = ChatOpenAI(model_name="gpt-4o-mini",temperature=0)
        self.vectorstore = self._setup_vectorstore()
        self.chain = self._setup_chain()

    def _setup_vectorstore(self):
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index = pc.Index(self.index_name)
        return PineconeVectorStore(index=index, embedding=self.embeddings)

    def _create_prompt(self):
        template = """
        Eres un experto en la creación de discursos. 
        Utiliza UNICAMENTE el contexto proporcionado para crear un discurso convincente y bien estructurado sobre el tema dado.
        
        Contexto:
        {context}

        Tema del discurso: {question}

        Por favor, genera un discurso que:
        1. Tenga una introducción atractiva
        2. Desarrolle los puntos principales de manera clara y concisa
        3. Incluya ejemplos o anécdotas relevantes
        4. Termine con una conclusión impactante

        Discurso:
        """
        return PromptTemplate(template=template, input_variables=["context", "question"])

    def _setup_chain(self):
        retriever = self.vectorstore.as_retriever(search_type="similarity", k=5)
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": self._create_prompt(), "verbose": False},
            return_source_documents=True,
            verbose=True
        )

    def generate_speech(self, topic):
        result = self.chain({"query": topic})
        print("Documentos consultados:")
        for i, doc in enumerate(result["source_documents"], 1):
            print(f"Documento {i}:")
            print(f"Contenido: {doc.page_content[:200]}...")  # Imprime los primeros 200 caracteres
            print(f"Metadatos: {doc.metadata}")
            print("---")

        return result["result"]