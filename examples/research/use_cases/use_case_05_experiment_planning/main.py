from ..common import agent
from typing import List


def plan_experiment(protocols: List[str]) -> str:
    """Combine multiple experimental protocols into a single plan."""
    combined = "\n".join(protocols)
    return agent.chat(f"Merge these protocols into one plan:\n{combined}")


if __name__ == "__main__":
    example = ["Protocol A", "Protocol B"]
    print(plan_experiment(example))
