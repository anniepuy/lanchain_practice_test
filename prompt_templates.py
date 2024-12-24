"""
Title: Prompt Template Script
Author: Ann Hagan via DataCamp tutorial
Purpose: Script create LangChain prompt templates for various use cases.
Date: 2024-12-23
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

template ="You are a {profession} answer the question. {question}"
prompt_template = PromptTemplate(template=template, input_variables=['profession', 'question'])

#print(prompt_template.invoke({"profession":'AI Engineer', "question":'What is Ai?'}))

#integrating a prompt template with an LLM
#Set your hugging face API token
huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_KEY")
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

llm_chain = prompt_template | llm
profession ="Ai Engineer"
question ="What is LangChain?"
print(llm_chain.invoke({"profession":{profession}, "question":{question}}))