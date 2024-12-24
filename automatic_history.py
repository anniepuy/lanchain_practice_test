"""
Title: Automatic history script
Author: Ann Hagan
Purpose: Script to practice LangChain's chat history methods. This is not based on DataCamp but the current documentation of LangChain CAO today. 
Date: 2024-12-23
"""

#Automatic histopry message - uses LangGraph's persistance to store the history
import os
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_huggingface import HuggingFaceEndpoint
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain_core.messages import HumanMessage, RemoveMessage

# ----------------------------------------
# Setup HuggingFace Endpoint
# ----------------------------------------

# Load HuggingFace API token from environment
huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_KEY")

# Initialize HuggingFaceEndpoint
model = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingfacehub_api_token=huggingfacehub_api_token
)

# ----------------------------------------
# Define LangGraph Workflow
# ----------------------------------------

demo_ephemeral_chat_history = [
    HumanMessage(content="Hey there! I'm Nemo."),
    AIMessage(content="Hello!"),
    HumanMessage(content="How are you today?"),
    AIMessage(content="Fine thanks!"),
]
# Create a workflow with MessagesState schema
workflow = StateGraph(state_schema=MessagesState)

# Define the function to call the HuggingFace model
def call_model(state: MessagesState):
    system_prompt = (
        "You are a helpful assistant. "
        "Answer all questions to the best of your ability."
    )
    # Combine system prompt and conversation history
    system_message = SystemMessage(content=system_prompt)
    message_histry = state["messages"][:-1]
    #summarize the messages if the chat history reaches a certain size
    if len(message_histry) > 5:
        last_human_message = state["messages"][-1]
        #invoke model to generate conversation summary
        summary_prompt = (
            "Distill the above chat messages into a single summary message."
            "Include as many specific details as you can."
        )
        summary_message = model.invoke(
            message_histry + [HumanMessage(conent=summary_prompt)]
        )

        # Delete messages that we no longer want to show up
        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"]]
        # Re-add user message
        human_message = HumanMessage(content=last_human_message.content)
        # Call the model with summary & response
        response = model.invoke([system_message, summary_message, human_message])
        message_updates = [summary_message, human_message, response] + delete_messages
    else:
        message_updates = model.invoke([system_message] + state["messages"])

    return {"messages": message_updates}

# Add nodes and edges to the workflow
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

# Add an in-memory checkpointer
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# ----------------------------------------
# Run the Workflow
# ----------------------------------------

# Define the initial user input
initial_state = {"messages": [HumanMessage(content="What is LangGraph?")]}
print(app.invoke (
    {
        "messages": demo_ephemeral_chat_history
        + [HumanMessage("What did I say my name was?")]
    },
    config={"configurable": {"thread_id": "4"}},
 ))