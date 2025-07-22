# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm da openai
from langchain_openai import ChatOpenAI

# Seta a chave de API da OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Instanciando o modelo de llm
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

while True:
    # Recebe a pergunta do usuário
    question = input("Insira a pergunta: ")
    
    # Se a pergunta for vazia ou a palavra "sair", sai do loop
    if question.lower() in ["", "sair", "exit"]:
        break
    
    # Chama o modelo passando a pergunta
    response = llm.invoke(question)

    # Apresenta a resposta na tela
    print(response)