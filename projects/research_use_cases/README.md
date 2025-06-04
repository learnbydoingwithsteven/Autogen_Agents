# Research Use Cases

This directory contains example use cases for [Autogen](https://github.com/microsoft/autogen) linked to a local model served by [Ollama](https://ollama.ai/). Each folder demonstrates a different research scenario.

## Setup

1. Start an Ollama server with a model. For example:

```bash
ollama serve &
ollama run llama2
```

2. Install the required package:

```bash
pip install pyautogen
```

## Available Use Cases

- `literature_review_automation` – Literature Review Automation
- `experiment_design` – Experiment Design Suggestions
- `data_collection` – Data Collection Planning
- `survey_analysis` – Survey Analysis and Visualization
- `statistical_modeling` – Statistical Modeling Guidance
- `hypothesis_generation` – Hypothesis Generation
- `paper_summary` – Research Paper Summarization
- `citation_management` – Citation Management Assistant
- `research_collaboration` – Research Collaboration Coordinator
- `grant_proposal_writing` – Grant Proposal Writing Aid

Each folder includes a `README.md` describing the scenario and a `main.py` that configures Autogen to interact with the local model. Run any example by executing `python3 main.py` in that directory.
