from src.knowledge_loader import KnowledgeLoader
from src.conversational_agent import ConversationalAgent
from dotenv import load_dotenv
import google.generativeai as genai
import os

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
    loader = KnowledgeLoader("data")
    agent = ConversationalAgent(loader)

    print("🤖 Chat with the agent (type 'exit' to quit)")

    # Mode selection
    mode = input("Choose mode (global/prospect): ").strip().lower()
    if mode == "prospect":
        prospects = loader.get_prospects_list()
        if not prospects:
            print("No prospects found in data folder.")
            return
        print("\nAvailable prospects:")
        for idx, p in enumerate(prospects, 1):
            print(f"{idx}. {p}")
        selection = int(input("Enter number: ").strip())
        if 1 <= selection <= len(prospects):
            agent.set_mode("prospect", prospects[selection - 1])
        else:
            print("Invalid selection.")
            return
    else:
        agent.set_mode("global")

    # Chat loop
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = agent.chat(user_input)
        print(f"Assistant: {answer}")


if __name__ == "__main__":
    main()
