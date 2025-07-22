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
    input_variables=["company","position","strengths","weaknesses"],
    template="""
    You are a career coach. Provide tailored interview tips for the
    position of {position} at {company}.
    Highlight your strengths in {strengths} and prepare for questions
    about your weaknesses such as {weaknesses}.
    Answer in Brazilian Portuguese.
    """
)

# Adiciona um título usando streamlit
st.title("Gerador de dicas para entrevistas")

# Recebe a empresa usando o streamlit
company = st.text_input("Nome da empresa: ")

# Recebe o cargo/posição usando o streamlit
position = st.text_input("Insira seu cargo/posição: ")

# Recebe os pontos fortes usando o streamlit
strengths = st.text_area("Insira seus pontos fortes: ", height=100)

# Recebe os pontos fracos usando o streamlit
weaknesses = st.text_area("Insira seus pontos fracos: ", height=100)

# Verifica se o usuário inseriu os dados
if company and position and strengths and weaknesses:
    # Chama o modelo passando a pergunta
    response = llm.invoke(prompt_template.format(
        company=company,
        position=position,
        strengths=strengths,
        weaknesses=weaknesses
        ))

    # Apresenta a resposta na tela usando o streamlit
    st.write(response.content)