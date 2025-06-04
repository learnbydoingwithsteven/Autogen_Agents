# Financial Autogen Examples

These examples demonstrate how to use [Autogen](https://github.com/microsoft/autogen) with a local model served by [Ollama](https://ollama.ai/). Follow the steps below to get started.

## Setup

1. Launch an Ollama server with a model:

   ```bash
   ollama serve &
   ollama run llama2
   ```

2. Install the required package:

   ```bash
   pip install pyautogen
   ```

## Available Use Cases

The `financial_examples` directory contains the following folders:

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

Each subfolder has a `README.md` and `main.py` showing how to run the example. Run an example with:

```bash
cd <folder>
python3 main.py
```
