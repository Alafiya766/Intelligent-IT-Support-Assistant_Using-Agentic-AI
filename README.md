Overview
This project is a simple AI-based IT Support Assistant that helps users solve common technical issues such as password reset, internet problems, email issues, and software installation.
The system uses an agent workflow built with LangGraph and a language model from Hugging Face Transformers to provide responses.
When a user asks a question, the system first searches a memory-based knowledge store. If the answer is found, it returns the stored solution. Otherwise, the GPT-2 model generates a helpful response.

Technologies Used
Python
LangGraph
Hugging Face Transformers
GPT-2 Model

Features
AI-powered IT support assistant
Memory-based solution retrieval
AI-generated responses for unknown queries
Simple command-line interface

How to Run
Install dependencies:
    pip install transformers langgraph torch

Run the program:
    python graph_builder.py
