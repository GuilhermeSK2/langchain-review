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
set_debug(True)


# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt_template = PromptTemplate(
    input_variables=["codigo","linguagem","enunciado"],
    template="""
    Você é um professor de programação, especialista na área de arquitetura e desenvolvimento de software.
    O enunciado do exercício proposto é: {enunciado}.
    A linguagem de programação utilizada foi é {linguagem}.
    Analise se o código está correto de acordo com o enunciado, e se ele resolve o problema proposto no enunciado.
    O código que será analisado é o seguinte:{codigo}.
    Caso o código esteja correto, diga de forma resumida a conclusão final e apresente pontos de melhoria se houver.
    Caso esteja errado instrua o aluno para o resultado correto sem dar a resposta explicitamente.
    Responda sempre em português
    """
)

# Adiciona um título usando streamlit
st.title("Corretor de Código")

# Recebe a exercicio usando o streamlit
enunciado = st.text_input("Insira o enunciado do exercicio: ")

# Recebe a linguagem de programação usando o streamlit
linguagem = st.selectbox("Selecione a linguagem: ", ["Python", "JavaScript", "Java", "C++", "C#", "GoLang"])

# Recebe o código da viagem usando o streamlit
codigo = st.text_input("Insira o código desenvolvido: ")


# Verifica se o usuário inseriu os dados
if enunciado and codigo:
    # Chama o modelo passando a pergunta
    response = llm.invoke(prompt_template.format(
        enunciado=enunciado,
        linguagem=linguagem,
        codigo=codigo,
        ))

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)