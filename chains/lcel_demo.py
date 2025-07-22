# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Importa a biblioteca para poder criar o prompt
from langchain.prompts import PromptTemplate


# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Habilita/Desabilita o debug
set_debug(False)


# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template="""
    Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions.
    2. Local cuisine you must try.
    3. Answer in {language}.
    4. Tips for traveling on a {budget} budget.
    Enjoy your trip!
    """
)

# Adiciona um título usando streamlit
st.title("Guia de Viagem")

# Recebe a cidade usando o streamlit
city = st.text_input("Insira a cidade: ")

# Recebe o mês da viagem usando o streamlit
month = st.text_input("Insira o mês da viagem: ")

# Recebe o idioma desejado de resposta usando o streamlit
language = st.text_input("Insira o idioma da resposta: ")

# Recebe o orçamento usando o streamlit
budget = st.selectbox("Orçamento para a viagem", ["Baixo", "Médio", "Alto"])

# Cria uma simples chain
chain = prompt_template | llm

# Verifica se o usuário inseriu os dados
if city and month and language and budget:
    # Chama o modelo passando a pergunta
    response = chain.invoke({
        "city":city,
        "month":month,
        "language":language,
        "budget":budget
        })

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)