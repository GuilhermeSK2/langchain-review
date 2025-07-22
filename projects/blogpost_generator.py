# Importa a biblioteca para poder interagir com o modelo de llm
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa a biblioteca para poder debugar o código
from langchain.globals import set_debug

# Importa a biblioteca para poder criar o prompt
from langchain.prompts import PromptTemplate

# Importa a biblioteca para poder criar o parser
from langchain_core.output_parsers import StrOutputParser


# Importa a biblioteca do streamlit para criar a interface
import streamlit as st

# Habilita/Desabilita o debug
set_debug(False)


# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are a professional blogger.
    Create an outline for a blog post on the following topic: {topic}
    The outline should include:
    - Introduction
    - 3 main points with subpoints
    - Conclusion
    """
)

introduction_prompt = PromptTemplate(
    input_variables=["outline"],
    template="""
    You are a professional blogger.
    Write an engaging introduction paragraph based on the following
    outline:{outline}
    The introduction should hook the reader and provide a brief
    overview of the topic.
    """
)

# Cria a primeira chain que vai gerar a base do post
first_chain = outline_prompt | llm | StrOutputParser()

# Cria a segunda chain qeu vai gerar o post
second_chain = introduction_prompt | llm

# Cria
overall_chain = first_chain | second_chain

# Cria um título para a aplicação
st.title("Gerador de post para blog")

# Cria um campo de texto para o usuário digitar o tópico
topic = st.text_input("Insira o tópico:")

# Verifica se o usuário digitou um tópico
if topic:
    # Invoca a chain
    response = overall_chain.invoke({"topic":topic})
    # Exibe a resposta
    st.write(response.content)