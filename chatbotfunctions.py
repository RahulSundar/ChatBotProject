import os, sys
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.memory import ChatMemoryBuffer

from embeddinggenerator import *

SECRET_API_TOKEN = os.environ["SECRET_API_TOKEN"]
openai.api_key = SECRET_API_TOKEN

def react_chatbot_engine(index):

    #memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
    chat_engine = index.as_chat_engine(
    chat_mode="react",
    #memory=memory,
    system_prompt=(
        "You are a helpful and friendly chatbot who addresses <your requirement here>"
        ),
    verbose=True,
    )
    return chat_engine

def condense_question_chatbot_engine(index):

    memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
    chat_engine = index.as_chat_engine(
    chat_mode="condense_question",
    memory=memory,
    system_prompt=(
        "You are a helpful and friendly chatbot who addresses <your requirement here>"
        ),
    verbose=True,
    )
    return chat_engine

def condense_context_question_chatbot_engine(index):

    memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
    chat_engine = index.as_chat_engine(
    chat_mode="condense_plus_context",
    memory=memory,
    system_prompt=(
        "You are a helpful and friendly chatbot who addresses <your requirement here>"
        "Here are the relevant documents for the context:\n"
        "{context_str}"
        "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
        ),
    verbose=True,
    )
    return chat_engine


def context_chatbot_engine(index):

    memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
    chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        "You are a helpful and friendly chatbot who addresses <your requirement here>"
        ),
    )
    return chat_engine


def generate_respone(chat_engine, query):

    response = chat_engine.chat(query)
    return response
    








