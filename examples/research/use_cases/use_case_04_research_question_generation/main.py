from ..common import agent
from typing import List


def generate_questions(field: str) -> List[str]:
    """Suggest research questions in the specified field."""
    prompt = f"Suggest three emerging research questions in the field of {field}."
    response = agent.chat(prompt)
    return [q.strip() for q in response.split('\n')]


if __name__ == "__main__":
    print("Questions:", generate_questions("graph neural networks"))
