"""
Title: Chat history script
Author: Ann Hagan
Purpose: Script to practice LangChain's chat history methods.
Date: 2024-12-23
"""
#ChatHistoryMemory
#Stores full message history in memory, two methods:
#.add_ai_message(message) - adds a message from the AI to the history
#.add_user_message(message) - adds a message from the user to the history
#.get_chat_history() - returns the full chat history

#Conversation Buffer Memory
#Rolling buffer memory of the last few messages in the conentation

#ConversationSummaryMemory
#summarises the conversation history - condensing information, uses a separate LLM call

#need to run pip install langchain[all] to install all the dependencies

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint 
#old code from DataCamp - depreicated import
# from langchain.memory import ChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
#New requirment not apart of DataCamp Tutorial
#Per documentation - https://langchain.readthedocs.io/en/latest/langchain.memory.html


#Set your hugging face API token
huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_KEY")

#Define the model from HugginFace
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)


#ChatHistoryMemory
#Create the conversation history and add the first AI message
history = ChatMessageHistory()
history.add_ai_message("Hello, how can I help you today?")

#Add user message to the history
history.add_user_message("What is LangChain?")

#Add another user message and call the model
history.add_user_message("How does LangChain work?")
response = llm.invoke(history.messages)
print(response)

#ChatBufferMemory
#This condenses the conversation history into a buffer, which only stores most recent messages

#DEPRICATED - does not work anymore - Define the chain for integrating the memory with the model
#buffer_chain = ConversationBufferMemory(llm = llm, memory= memory) 
