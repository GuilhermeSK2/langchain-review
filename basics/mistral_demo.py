# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm que está rodando localmente
from langchain_community.chat_models import ChatOllama

# Instanciando o modelo de llm
llm = ChatOllama(model="mistral")

while True:
    # Recebe a pergunta do usuário
    question = input("Insira a pergunta: ")
    
    # Se a pergunta for vazia ou a palavra "sair", sai do loop
    if question == "" or question == "sair" or question == "Sair":
        break
    
    # Chama o modelo passando a pergunta
    response = llm.invoke(question)

    # Apresenta a resposta na tela
    print(response)