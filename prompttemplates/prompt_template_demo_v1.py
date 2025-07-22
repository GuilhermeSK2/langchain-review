# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm que está rodando localmente
from langchain_ollama import ChatOllama

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Importa a biblioteca para poder criar o prompt
from langchain.prompts import PromptTemplate


# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Habilita/Desabilita o debug
set_debug(False)


# Instanciando o modelo de llm
llm = ChatOllama(model="mistral")


prompt_template = PromptTemplate(
    input_variables=["country","no_of_paras","language"],
    template="""
    You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Avoid giving information about fictional places. If the country is fictional
    or non-existent answer: I don't know.
    Answer the question: What is the traditional cuisine of {country}?
    Answer in {no_of_paras} short paras in {language}.
    """
)

# Adiciona um título usando streamlit
st.title("Informações de Culinária")

# Recebe o país usando o streamlit
country = st.text_input("Insira o país: ")

# Recebe o número de parágrafos usando o streamlit e limitando o valor mínimo a 1 e máximo a 5
no_of_paras = st.number_input("Insira o número de parágrafos: ", min_value=1, max_value=5)

# Recebe o idioma desejado usando o streamlit
language = st.text_input("Insira o idioma da resposta: ")
    
if country:
    # Chama o modelo passando a pergunta
    response = llm.invoke(prompt_template.format(
        country=country,
        no_of_paras=no_of_paras,
        language=language
        ))

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)