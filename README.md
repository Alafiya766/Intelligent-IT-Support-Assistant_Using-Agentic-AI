Overview:

This project is a simple AI-based IT Support Assistant that helps users solve common technical issues such as password reset, internet problems, email issues, and software installation.
The system uses an agent workflow built with LangGraph and a language model from Hugging Face Transformers to provide responses.
When a user asks a question, the system first searches a memory-based knowledge store. If the answer is found, it returns the stored solution. Otherwise, the GPT-2 model generates a helpful response.
<hr>
Technologies Used:


1.Python

2.LangGraph

3.Hugging Face Transformers

4.GPT-2 Model
<hr>
Features:


-AI-powered IT support assistant

-Memory-based solution retrieval

-AI-generated responses for unknown queries

-Simple command-line interface
<hr>
How to Run:

Install dependencies:

    pip install transformers langgraph torch

Run the program:

    python graph_builder.py
