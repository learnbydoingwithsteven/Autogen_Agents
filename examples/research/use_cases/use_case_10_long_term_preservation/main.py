from ..common import knowledge_graph
from typing import List


def archive_outputs(outputs: List[str]):
    """Record research outputs in the knowledge graph."""
    for item in outputs:
        knowledge_graph.add_node(item, type="result")
        knowledge_graph.add_edge(item, "archive", relation="stored_in")


if __name__ == "__main__":
    archive_outputs(["dataset_v1", "model_checkpoints"])
    print("Archived nodes:", knowledge_graph.nodes())
