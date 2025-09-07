from llama_index.core import VectorStoreIndex, Document, SimpleDirectoryReader
# from knowledge_loader import KnowledgeLoader
from src.gemini_client import GeminiClient


class RAGAgent:
    def __init__(self, loader, model_name="gemini-1.5-flash"):
        self.loader = loader
        self.client = GeminiClient(model_name)

    def query_global(self, question: str) -> str:
        context = self.loader.get_all_knowledge()
        prompt = f"""
        You are a helpful assistant. Use the context below to answer the question concisely.

        Context:
        {context}

        Question:
        {question}
        """
        return self.client.ask(prompt)

    def query_prospect(self, prospect: str, question: str) -> str:
        context = self.loader.get_prospect_knowledge(prospect)
        prompt = f"""
        You are a helpful assistant. Use only the given prospect's context to answer concisely.

        Prospect: {prospect}
        Context:
        {context}

        Question:
        {question}
        """
        return self.client.ask(prompt)
