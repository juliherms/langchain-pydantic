from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "praia"

# Template do prompt considernado as variáveis acima
modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias, 
    para uma família com {numero_criancas} crianças,
    que gostam de {atividade}
    """
)

# formatação do template e aplicação das variáveis
prompt = modelo_de_prompt.format(
    dias=numero_dias,
    numero_criancas = numero_criancas,
    atividade=atividade
)

# apresenta o prompt
print("Prompt : \n", prompt)

# configura o modelo
modelo = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

# executa o modelo com o prompt gerado
resposta = modelo.invoke(prompt)
print(resposta.content)
