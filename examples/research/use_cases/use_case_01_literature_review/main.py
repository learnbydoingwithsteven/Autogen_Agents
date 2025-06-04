from ..common import agent, knowledge_graph
from typing import List


def summarize_papers(paper_abstracts: List[str]) -> List[str]:
    """Summarize a list of paper abstracts."""
    summaries = []
    for abstract in paper_abstracts:
        summary = agent.chat(f"Summarize this abstract: {abstract}")
        summaries.append(summary)
    return summaries


if __name__ == "__main__":
    example = ["Recent advances in graph neural networks ..."]
    print("Summaries:", summarize_papers(example))
