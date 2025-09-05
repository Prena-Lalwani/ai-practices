import re
from src.gemini_client import GeminiClient


class KnowledgeAgent:

    def __init__(self, knowledge_loader):
        self.loader = knowledge_loader
        self.gemini = GeminiClient()

    def answer_question_global(self, question: str) -> str:
        # Step 1: Get combined knowledge
        knowledge_text = self.loader.get_all_knowledge()
        prompt = f"""
        You are a knowledge assistant.
        Context: {knowledge_text}

        Question: {question}

        Provide a clear, structured, and helpful answer based only on the context.
        """
        return self.gemini.ask(prompt)

    def answer_question_prospect(self, prospect: str, question: str) -> str:
        # Step 1: Get combined knowledge
        knowledge_text = self.loader.get_prospect_knowledge(prospect)
        prompt = f"""
        You are a knowledge assistant.
        Prospect: {prospect}
        Context: {knowledge_text}

        Question: {question}

        Provide a precise and structured answer relevant to this prospect.
        """
        return self.gemini.ask(prompt)

    def _search_knowledge(self, question: str, knowledge_text: str, mode: str) -> str:

        # Step 2: Split into sentences
        sentences = re.split(r"(?<=[.!?]) +", knowledge_text)

        # Step 3: Extract keywords from question
        question_keywords = re.findall(r"\w+", question.lower())

        # Step 4: Match sentences containing any keyword
        matched_sentences = [
            sentence
            for sentence in sentences
            if any(keyword in sentence.lower() for keyword in question_keywords)
        ]

        # Step 5: Return the first relevant sentence, or a default message
        if matched_sentences:
            return matched_sentences[0]
        return "No relevant information found in the global knowledge."
