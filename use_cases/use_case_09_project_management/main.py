from ..common import agent
from typing import List


def suggest_tasks(goal: str) -> List[str]:
    """Break a research goal into actionable tasks."""
    response = agent.chat(
        f"Break down the following research goal into actionable tasks: {goal}"
    )
    return [task.strip() for task in response.split('\n')]


if __name__ == "__main__":
    print("Tasks:", suggest_tasks("Investigate graph neural network scalability"))
