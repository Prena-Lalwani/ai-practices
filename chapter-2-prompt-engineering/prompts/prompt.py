class prompt:

    def __init__(self, template: str):
        self.template = template

    def for_prompt(self, data: dict) -> str:
        try:
            return self.template.format(**data)
        except KeyError as e:
            return ValueError(f"Missing placeholder value: {e}")
