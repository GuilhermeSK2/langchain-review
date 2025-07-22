# Importa a biblioteca para poder interagir com o modelo de llm
from langchain_google_genai import ChatGoogleGenerativeAI

# Importa a biblioteca para poder interagir com o modelo de llm que está rodando localmente
from langchain_ollama import ChatOllama

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


# Instanciando o primeiro modelo de llm a ser usado
llm_api = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Instanciando o segundo modelo de llm a ser usado
llm_local = ChatOllama(model="mistral")


title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an experienced speech writer.
    You need to craft an impactful title for a speech
    on the following topic: {topic}
    Answer exactly with one title. 
    """
)

speech_prompt = PromptTemplate(
    input_variables=["title"],
    template="""
    You need to write a powerful speech of 350 words
    for the following title: {title}
    """
)

# Cria a primeira chain que vai gerar o título
first_chain = title_prompt | llm_api | StrOutputParser() | (lambda title: (st.write(title),title)[1])

# Cria a segunda chain que vai gerar o discurso
second_chain = speech_prompt | llm_local

# Cria a chain final que vai receber o topico passar para a primeira que vai gerar o título e depois para a segunda que vai gerar o discurso
final_chain = first_chain | second_chain

# Cria um título para a aplicação
st.title("Gerador de discurso")

# Cria um campo de texto para o usuário digitar o tópico
topic = st.text_input("Insira o tópico:")

# Verifica se o usuário digitou um tópico
if topic:
    # Invoca a chain
    response = final_chain.invoke({"topic":topic})
    # Exibe a resposta
    st.write(response.content)