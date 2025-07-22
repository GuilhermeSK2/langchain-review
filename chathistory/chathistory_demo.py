# Importa a biblioteca para poder interagir com o modelo de llm
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Importa a biblioteca para poder criar o prompt
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Habilita/Desabilita o debug
set_debug(False)


# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a Agile Coach. Answer any questions "
    "related to the agile process"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])


# Cria uma simples chain
chain = prompt_template | llm

history_for_chain = ChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)

print("Agile Guide")

while True:
    question = input("Insira a pergunta:")
    if question:
        response = (chain_with_history
                    .invoke({"input": question},
                            {"configurable": {
                                "session_id": "abc123"
                            }}
                            ))
        print(response.content)