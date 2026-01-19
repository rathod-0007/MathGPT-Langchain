---
title: MathGPT LangChain
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.30.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# MathGPT-Langchain

A mathematical assistant and reasoning agent powered by Google Gemma2 via Groq, built using LangChain and Streamlit.

## 🔗 Live Demo
Check out the live application here: **[MathGPT-Langchain](https://mathgpt-langchain-0007.streamlit.app/)**

## Features

* **Step-by-Step Reasoning:** Solves complex math word problems with explained logic.
* **Calculator Integration:** Uses `LLMMathChain` for precise numerical computations.
* **Knowledge Retrieval:** Fetches context from Wikipedia for general queries.
* **Streamlit Interface:** Interactive chat interface with session state management.

## Tech Stack

* **Python**
* **Streamlit**
* **LangChain** (Agents, Chains, Tools)
* **Groq API** (Gemma2 Model)
* **Wikipedia API**

## Installation

```bash
git clone https://github.com/your-username/mathgpt-langchain.git
cd mathgpt-langchain
pip install -r requirements.txt
