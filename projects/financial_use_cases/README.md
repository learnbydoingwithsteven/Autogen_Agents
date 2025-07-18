# Autogen_Agents

This repository contains example use cases for [Autogen](https://github.com/microsoft/autogen) linked to a local model served by [Ollama](https://ollama.ai/). Each directory demonstrates a different financial industry scenario.

## Setup

1. Start an Ollama server with a model. For example:

   ```bash
   ollama serve &
   ollama run llama2
   ```

2. Install the required package:

   ```bash
   pip install ag2
   ```

## Available Use Cases

- `algorithmic_trading` – Algorithmic Trading Idea Generation
- `compliance_monitoring` – Compliance Monitoring
- `credit_risk_assessment` – Credit Risk Assessment
- `customer_support` – Customer Support Chatbot
- `data_extraction` – Financial Data Extraction
- `fraud_detection` – Fraud Detection
- `loan_underwriting` – Loan Underwriting
- `market_sentiment_analysis` – Market Sentiment Analysis
- `portfolio_optimization` – Portfolio Optimization
- `regulatory_reporting` – Regulatory Reporting

Each folder includes a `README.md` explaining the scenario and a `main.py` that configures Autogen to communicate with the locally hosted model. Run any example by executing `python3 main.py` in that directory.
