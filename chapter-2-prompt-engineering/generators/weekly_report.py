from prompts.prompt import prompt
from base_generator import report_generator


class weekly_status_report(report_generator):
    def __init__(self, api_key: str):
        super().__init__(api_key)

        self.prompt_template = prompt(
            "Generate a weekly status report for project '{project_name}'. "
            "Key achievements: {achievements}. "
            "Next steps: {next_steps}. "
            "Make the tone professional and concise."
        )

    def generate_report(self, project_data: dict) -> str:
        formatted_prompt = self.prompt_template(project_data)
        print("Formatted prompt:\n", formatted_prompt)
        generated_report = self._call_gpt(formatted_prompt)
        return generated_report
