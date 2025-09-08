import os
import json

class HistoryManager:
    def __init__(self, history_folder="history"):
        self.history_folder = history_folder
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
        turn = [[ "user", user_msg ], [ "assistant", assistant_msg ]]
        history.append(turn)
        self.save_history(prospect_name, history)

    def save_history(self, prospect_name: str, history):
        """Save the history 2D array back to JSON file."""
        file_path = self.get_history_file(prospect_name)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
