# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Importa a biblioteca para poder criar o prompt
from langchain.prompts import ChatPromptTemplate


# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Habilita/Desabilita o debug
set_debug(False)


# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a Agile Coach. Answer any questions "
    "related to the agile process"),
    ("human", "{input}")
])

# Adiciona um título usando streamlit
st.title("Guia Ágil")

# Recebe a cidade usando o streamlit
input = st.text_input("Insira a pergunta: ")

# Cria uma simples chain
chain = prompt_template | llm

# Verifica se o usuário inseriu os dados
if input:
    # Chama o modelo passando a pergunta
    response = chain.invoke({
        "input":input
        })

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)