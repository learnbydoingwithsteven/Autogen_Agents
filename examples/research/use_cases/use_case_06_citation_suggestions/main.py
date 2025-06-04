from ..common import agent
from typing import List


def suggest_citations(text: str) -> List[str]:
    """Suggest citations for a piece of text."""
    response = agent.chat(
        f"Suggest relevant citations for the following passage:\n{text}"
    )
    return [c.strip() for c in response.split('\n')]


if __name__ == "__main__":
    example = "Graph neural networks offer new ways to model data."
    print("Citations:", suggest_citations(example))
