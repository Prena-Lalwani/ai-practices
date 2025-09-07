from typing import List, Tuple
from src.rag_agent import RAGAgent
from src.gemini_client import GeminiClient


class ConversationalAgent:
    def __init__(self, loader, mode="global", max_turns=5):
        self.loader = loader
        self.rag_agent = RAGAgent(loader)
        self.mode = mode
        self.selected_prospect = None
        self.history = []  # store previous turns
        self.max_turns = max_turns

    def set_mode(self, mode: str, prospect: str = None):
        self.mode = mode
        self.selected_prospect = prospect

    def chat(self, question: str) -> str:
        self.history.append({"user": question})

        if self.mode == "global":
            answer = self.rag_agent.query_global(question)
        elif self.mode == "prospect":
            if not self.selected_prospect:
                return "Please select a prospect first."
            answer = self.rag_agent.query_prospect(self.selected_prospect, question)
        else:
            return "Invalid mode. Use 'global' or 'prospect'."

        self.history.append({"assistant": answer})

        # keep only last max_turns
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns*2:]

        return answer
