import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.knowledge_loader import KnowledgeLoader
# from src.agent import KnowledgeAgent
from src.rag_agent import RAGAgent
# from src.gemini_client import GeminiClient

env_loaded = load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
if not env_loaded:
    print("⚠️ Warning: .env file not loaded, make sure it's in project root.")

    # ✅ Step 1: Configure Gemini with API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)
print("Gemini API configured:")



def main():
    # Step 1: Initialize Knowledge Loader
    loader = KnowledgeLoader("data")

    # Step 2: Initialize Agent
    # agent = KnowledgeAgent(loader)
    rag_agent = RAGAgent(loader)

    # Step 3: Ask user for answer mode
    print("Welcome to the Knowledge Agent!")
    print("Do you want your question answered globally (all prospects) "
          "or from a specific prospect? (Enter 'global' or 'prospect')")
    mode = input("Mode: ").strip().lower()

    if mode == "global":
        question = input("Enter your question: ").strip()
        answer = rag_agent.query_global(question)
        print("\nAnswer (Global):", answer)

    elif mode == "prospect":
        # List available prospect files
        prospects = loader.get_prospects_list()
        if not prospects:
            print("No prospects found in the data folder.")
            return

        # Enumerate and display prospects
        print("\nSelect a prospect by number:")
        for idx, prospect in enumerate(prospects, start=1):
            print(f"{idx}. {prospect.capitalize()}")

        # Ask user to select
        try:
            selection = int(input("Enter the prospect number: ").strip())
            if 1 <= selection <= len(prospects):
                selected_prospect = prospects[selection - 1]
                question = input("Enter your question: ").strip()
                answer = rag_agent.query_prospect(selected_prospect, question)
                print(f"\nAnswer ({selected_prospect.capitalize()}):", answer)
            else:
                print("Invalid selection. Exiting.")
                return
        except ValueError:
            print("Invalid input. Please enter a number. Exiting.")
            return

        #     # question = input("Enter your question: ").strip()
        #     # answer = agent.answer_question_prospect(question, selected)
        #     # print(f"\nAnswer ({selected.capitalize()}):", answer)
        # else:
        #     print("Invalid prospect selected. Please check the list and try again.")

    else:
        print("Invalid mode selected. Please enter 'global' or 'prospect'.")

if __name__ == "__main__":
    main()
