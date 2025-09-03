import os


class KnowledgeLoader:
    def __init__(self, data_folder: str):
        self.data_folder = data_folder
        self.knowledge = {}  # Holds prospect_name -> content
        self._load_all_prospects()

    def _load_all_prospects(self):
        if not os.path.exists(self.data_folder):
            print(f"Data folder '{self.data_folder}' does not exist.")
            return

        for file_name in os.listdir(self.data_folder):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.data_folder, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        # Store content with lowercase file name as key
                        prospect_name = os.path.splitext(file_name)[0].lower()
                        self.knowledge[prospect_name] = content
                except Exception as e:
                    print(f"Error reading '{file_name}': {e}")

    def get_all_knowledge(self) -> str:
        all_content = "\n\n".join(self.knowledge.values())
        return all_content
    

    def get_prospect_knowledge(self, prospect_name: str):
        return self.knowledge.get(prospect_name.lower(), "")

    

    def get_prospects_list(self):
        return sorted(list(self.knowledge.keys()))
