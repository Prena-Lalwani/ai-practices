import google.generativeai as genai


class GeminiClient:
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def ask(self, prompt: str) -> str:
        try:
            full_prompt = f"Answer concisely in 2–3 sentences max:\n\n{prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error with Gemini API: {e}"
