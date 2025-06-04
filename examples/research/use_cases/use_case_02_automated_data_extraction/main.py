from ..common import agent, knowledge_graph


def extract_datasets(paper_text: str):
    """Identify datasets mentioned in the given text."""
    response = agent.chat(
        f"Identify datasets mentioned in the following text and give their URLs if available:\n{paper_text}"
    )
    return {"datasets": response}


if __name__ == "__main__":
    text = "We used the ABC dataset (https://example.com/abc) for training."
    print("Datasets:", extract_datasets(text))
