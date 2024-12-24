"""
Title: Basic Connect Script
Author: Ann Hagan
Purpose: Script to connect to HuggingFace model hub using LangChain. User can swap out models.
Date: 2024-12-23
"""
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint 


#Set your hugging face API token
huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_KEY")

#Define the model from HugginFace
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

#We are going to use this model to predict the words that come next in the question.
question = 'Whatever you do, take care of your shoes'

output = llm.invoke(question)

print(output)