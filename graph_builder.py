from transformers import pipeline
from langgraph.graph import StateGraph, END
from typing import TypedDict
from memory_store import LongTermMemory


# State structure
class AgentState(TypedDict):
    question: str
    context: str
    answer: str


# Load GPT2 model
pipe = pipeline(
    "text-generation",
    model="gpt2"
)

# Memory object
memory = LongTermMemory()


# Retrieve context from memory
def retrieve(state: AgentState):
    context = memory.search(state["question"])
    return {"context": context}


def generate(state: AgentState):

    context = state["context"]
    question = state["question"]

    # If memory already has the answer, return it
    if context != "No relevant information found in memory.":
        return {"answer": context}

    # Otherwise use GPT2
    prompt = f"""
You are an IT support assistant.

User Question: {question}

Give a short helpful answer.
Answer:
"""

    result = pipe(
        prompt,
        max_new_tokens=50,
        temperature=0.7,
        do_sample=True
    )

    full_output = result[0]["generated_text"]

    answer = full_output.replace(prompt, "").strip()

    if answer == "":
        answer = "Sorry, I could not find an answer."

    return {"answer": answer}


# Build LangGraph workflow
def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)

    workflow.set_entry_point("retrieve")

    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()


# Run the program
if __name__ == "__main__":

    app = build_graph()

    question = input("Ask IT Support Question: ")

    state = {
        "question": question,
        "context": "",
        "answer": ""
    }

    result = app.invoke(state)

    print("\nAI Support Answer:")
    print(result["answer"])


