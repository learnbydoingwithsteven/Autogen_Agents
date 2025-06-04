from ..common import agent
from typing import List


def find_insights(topic: str) -> List[str]:
    """Find interdisciplinary applications related to a topic."""
    response = agent.chat(
        f"List interdisciplinary applications related to {topic}."
    )
    return [item.strip() for item in response.split('\n')]


if __name__ == "__main__":
    print("Insights:", find_insights("graph neural networks"))
