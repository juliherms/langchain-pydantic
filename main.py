from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from dotenv import load_dotenv

from langchain_core.globals import set_debug
from pydantic import Field, BaseModel
import os

# O comando debug pode ajudar a monitorar tokens
#set_debug(True)

# Carrega e atribui variaveis de ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Classe criada para descrever o formato de saida
# com objetivo de ter um padrão
# o uso do pydantic ajuda a formatar a saida e ter um maior controle
class Destino(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("motivo pelo qual é interessante visitar essa cidade")
# faz um parser da resposta
parseador = JsonOutputParser(pydantic_object=Destino)


# Template do prompt considernado as variáveis acima
prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saide}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saide": parseador.get_format_instructions() }
)

# configura o modelo
modelo = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

# monta da cadeia baseada por prompt, modelo e saida
cadeia = prompt_cidade | modelo | parseador

#Invoca o modelo
resposta = cadeia.invoke(
    {
        "interesse": "praias"
    }
)

print(resposta)
