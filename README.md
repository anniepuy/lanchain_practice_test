# Overview

Langchain Practice Test is a Repo that contains all of my testing to get a tutorial from DataCamp to work locally.

## Learning Lessons

1. Conda vs. Venv
   Admittedly, I missed used conda and venv the past month. I used conda typcially in my Anaconda Jupyter Notebooks. Switching back to VS Code for development, I started to use venv.
   Eventually I made a mistake and ended up with a separate project using a virutal environment on top of my base enviroment. (oh that was a fun entanglement)

So for this, I really wanted to understand the difference in using the command line vs. VS code tools.
I leard that you can create and activate a venv both in terminal or command pallette. While I knew this, I never really practiced it outside of the terminal. VS code likes to sneakily just add popups asking if you want to create a venv when in your terminal you've already created one with conda. I am sure it's some user error on my part, but either way, this little pop up put self-doubt in my head and I end up with a venv in venv.

Lesson: While in VS code just use the damn command pallette to create venv.
View => Command Pallette => Create Environment => Select Interpretor

2.Environment Variables
To use environment variables one needs to install
pip install python-dotenv

3. Import statements
   My first draft at replicating the DataCamp tutorials locally was an issue with my import statement:
   from langchain_huggingface import HuggingFaceEndpoint

DataCamp has students execute the code in their sandbox cloud environment, therefore replicating the tutorials are not 100% straighforward. I needed to find out how to import LangChain's HuggingFace methods.

I did a little Google and followed this https://python.langchain.com/docs/integrations/llms/huggingface_endpoint/

Which stated to use %pip install --upgrade --quiet huggingface_hub

Welp, that didn't work. Pylance still could not resolve it.

So I went basic style:
pip install langchain

Welp, Pylance still could not import it.

So I let GitHub CoPilot assist. It changed my import statement to:
from langchain.llms import HuggingFaceEndpoint

Next I get an error:
ModuleNotFoundError: No module named 'langchain_community'

So I import pip install langchain_community.

I run my script again.

Next, I get errors:
LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.llms import HuggingFaceEndpoint`.

To install langchain-community run `pip install -U langchain-community`.

and..
LangChainDeprecationWarning: The class `HuggingFaceEndpoint` was deprecated in LangChain 0.0.37 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-huggingface package and should be used instead. To use it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:`~langchain_huggingface import HuggingFaceEndpoint``.

Well..sh\*\*.
I head over to ChatGPT and paste the error. ChatGPT's answer:
pip install langchain-huggingface

Yup. That simple.

Things I wish:

1. DataCamp would also provide additional instructions if a student wants to replicate it on a project outside of their virutal hub.
2. Where is this in LangChain's documentation? Please someone help find it for me.
3. GitHub CoPilot, even though uses "ChatGPT-4" is not the same as ChatGPT-4.

# Depricated Issues

1. LangChain Memory Buffer is Depricated
   Holy cow, this was an adventure down documentation. LangChain has signifcantly changed their methods - sounds like a good approach to keep users from ever really USING it.
