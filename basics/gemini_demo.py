# Importa a biblioteca OS para lidar com arquivos e diretórios
import os

# Importa a biblioteca para poder interagir com o modelo de llm da google
from langchain_google_genai import ChatGoogleGenerativeAI

import dotenv

dotenv.load_dotenv()


# Seta a chave de API da Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Instanciando o modelo de llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

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