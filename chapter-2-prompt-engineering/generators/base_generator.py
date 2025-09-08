import openai
from config import require_api_key, OPENAI_MODEL, OPENAI_TEMPERATURE


class report_generator:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or require_api_key()
        openai.api_key = self.api_key

    def _call_gpt(self, formatted_prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": formatted_prompt}],
                temperature=OPENAI_TEMPERATURE,
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            print("GPT API call failed:", e)
            return f"Error: {e}"

    def generate_report(self, data: dict):
        raise NotImplementedError(
            "Every Subclass is bound to implement generate_report()"
        )
