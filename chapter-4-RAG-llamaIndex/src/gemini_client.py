import google.generativeai as genai


class GeminiClient:
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def ask(self, prompt: str) -> str:
        try:
            wrapped_prompt = f"""
            Please answer concisely (2–3 sentences max). 
            If context is provided, strictly use it. 
            Do not add extra details beyond what is relevant.

            {prompt}
            """
            response = self.model.generate_content(wrapped_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error with Gemini API: {e}"
