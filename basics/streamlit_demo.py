# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm que está rodando localmente
from langchain_ollama import ChatOllama

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Habilita o debug
set_debug(True)

# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Instanciando o modelo de llm
llm = ChatOllama(model="mistral")

# Adiciona um título usando streamlit
st.title("Pergunte algo")

# Recebe a pergunta do usuário usando o streamlit
question = st.text_input("Insira a pergunta: ")
    
if question:
    # Chama o modelo passando a pergunta
    response = llm.invoke(question)

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)