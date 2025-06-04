"""Common utilities for example Autogen use cases."""

from __future__ import annotations

import networkx as nx


class OllamaModel:
    def __init__(self, model_name: str = "llama2"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        return f"[Generated with {self.model_name}] {prompt[:50]}..."


class Agent:
    def __init__(self, model: OllamaModel):
        self.model = model

    def chat(self, prompt: str) -> str:
        return self.model.generate(prompt)


knowledge_graph = nx.DiGraph()
model = OllamaModel()
agent = Agent(model)
