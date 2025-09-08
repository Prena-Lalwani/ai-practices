import os
import json
import google.generativeai as genai


class HistoryManager:
    def __init__(self, model, history_folder="history"):
        self.history_folder = history_folder
        self.model = model
        os.makedirs(self.history_folder, exist_ok=True)

    def get_history_file(self, prospect_name: str) -> str:
        """Return the path to the history JSON file for a prospect or global."""
        filename = f"{prospect_name}.json"
        return os.path.join(self.history_folder, filename)

    def load_history(self, prospect_name: str):
        """Load history from JSON file, return 2D array format."""
        file_path = self.get_history_file(prospect_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return []  # empty history

    def append_turn(self, prospect_name: str, user_msg: str, assistant_msg: str):
        """Append a new conversation turn and save to file."""
        history = self.load_history(prospect_name)
        if history and isinstance(history[0], dict) and "summary" in history[0]:
            summary_obj, messages = history
        else:
            # Old format or empty file: initialize summary
            summary_obj = {"summary": ""}
            messages = history if history else []

        turn = [["user", user_msg ], ["assistant", assistant_msg ]]
        messages.append(turn)

        if len(messages) >= 10:
            summary_text = self.summarize_history(messages[:10])
            if summary_obj["summary"]:
                summary_obj["summary"] += " " + summary_text
            else:
                summary_obj["summary"] = summary_text
            # Remove summarized messages
            messages = messages[10:]
           

        self.save_history(prospect_name, [summary_obj, messages])


    def save_history(self, prospect_name: str, history):
        """Save the history 2D array back to JSON file."""
        file_path = self.get_history_file(prospect_name)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

    def summarize_history(self, history_chunk):
        try:
            text = "\n".join([f"{speaker}: {msg}" for turn in history_chunk for speaker, msg in turn])
            prompt = f"Summarize the following conversation in a concise paragraph:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"[Error summarizing: {e}]"
