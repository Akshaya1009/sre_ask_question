# SRE AI Consultant Agent 🤖

An AI-powered script that interacts with **Ollama** to provide expert-level insights into Site Reliability Engineering (SRE) and DevOps challenges. This project is integrated with an automated **AI Release Agent** that handles versioning and tagging upon merge.

## 🚀 Overview

The script queries a locally running LLM (via Ollama) with complex infrastructure questions, such as implementing self-healing systems in Kubernetes. It is designed to be used as a CLI tool or integrated into a larger DevOps platform.

## 🛠️ Prerequisites

1.  **Ollama installed:** [Download here](https://ollama.com)
2.  **Model downloaded:** 
    ```bash
    ollama pull llama3
    ```
3.  **Python 3.8+**

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install ollama python-dotenv
    ```

3.  **Configure Environment:**
    Create a `.env` file in the root directory:
    ```env
    MODEL=llama3
    ```

## 🏃 Running the Script

Execute the agent using Python:
```bash
python chat.py