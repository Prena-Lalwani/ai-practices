import re


class KnowledgeAgent:
    
    def __init__(self, knowledge_loader):
        self.loader = knowledge_loader

    def answer_question_global(self, question: str) -> str:
        # Step 1: Get combined knowledge
        knowledge_text = self.loader.get_all_knowledge()

        # Step 2: Split into sentences
        sentences = re.split(r"(?<=[.!?]) +", knowledge_text)

        # Step 3: Extract keywords from question
        question_keywords = re.findall(r"\w+", question.lower())

        # Step 4: Match sentences containing any keyword
        matched_sentences = [
            sentence for sentence in sentences
            if any(keyword in sentence.lower() for keyword in question_keywords)
        ]

        # Step 5: Return the first relevant sentence, or a default message
        if matched_sentences:
            return matched_sentences[0]
        return "No relevant information found in the global knowledge."
