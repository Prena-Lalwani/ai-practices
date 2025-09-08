from prompts.prompt import prompt
from generators.base_generator import report_generator


class monthly_summary_report(report_generator):
    def __init__(self, api_key: str):
        super().__init__(api_key)

        self.prompt_template = prompt(
            "Generate a monthly summary report for project '{project_name}'. "
            "This month’s highlights: {highlights}. "
            "Challenges faced: {challenges}. "
            "Plans for next month: {plans}. "
            "Make it professional, clear, and well-structured."
        )

    def generate_report(self, project_data: dict) -> str:
        formatted_prompt = self.prompt_template(project_data)
        generated_report = self._call_gpt(formatted_prompt)
        return generated_report
