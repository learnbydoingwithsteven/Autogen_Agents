from ..common import agent, knowledge_graph
from typing import List


def map_topics(idea_description: str) -> List[str]:
    """Map an idea to related topics using the knowledge graph."""
    response = agent.chat(
        f"Which research topics relate to this idea: {idea_description}"
    )
    related = [topic.strip() for topic in response.split(',')]
    for topic in related:
        knowledge_graph.add_node(topic, type="topic")
    return related


if __name__ == "__main__":
    print("Related Topics:", map_topics("Analyzing protein interactions with GNNs"))
