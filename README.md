# langchain-pydantic

Projeto de estudo em Python que usa **LangChain** para orquestrar chamadas a modelos da OpenAI a partir de um `PromptTemplate`. Atualmente é um único script (`main.py`) que monta um prompt de roteiro de viagem e envia para um modelo de chat da OpenAI.

> O nome do projeto sugere uso de **Pydantic** para validação/saída estruturada, mas isso ainda não está implementado em `main.py` (veja [Próximos passos](#próximos-passos)).

## Como funciona

`main.py`:

1. Carrega a `OPENAI_API_KEY` de um arquivo `.env` via `python-dotenv`.
2. Monta um `PromptTemplate` com variáveis (`dias`, `numero_criancas`, `atividade`).
3. Formata o prompt e imprime no console.
4. Envia o prompt para um `ChatOpenAI` (`gpt-4o-mini`) e imprime a resposta.

## Requisitos

- Python 3.11+
- Uma chave de API da OpenAI

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/Mac

pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e preencha sua chave:

```bash
copy .env.example .env
```

```
OPENAI_API_KEY=sk-...
```

## Uso

```bash
python main.py
```

Isso imprime o prompt gerado e a resposta do modelo no console. Para gerar roteiros diferentes, edite as variáveis `numero_dias`, `numero_criancas` e `atividade` no topo de `main.py`.

## Dependências

| Pacote | Versão | Uso |
|---|---|---|
| `openai` | 3.13.0 | SDK oficial da OpenAI (dependência do `langchain-openai`) |
| `langchain` | 1.4.0 | Núcleo de orquestração (prompts, chains) |
| `langchain-openai` | 1.6.2 | Integração LangChain ↔ OpenAI (`ChatOpenAI`) |
| `langchain-community` | 0.4.2 | Integrações da comunidade (loaders, vector stores, etc.) |
| `langgraph` | 1.2.11 | Orquestração de agentes/fluxos com estado (não usado em `main.py` ainda) |
| `pydantic` | 2.13.5 | Validação de dados / saída estruturada (não usado em `main.py` ainda) |
| `python-dotenv` | 1.2.3 | Carrega variáveis de ambiente do `.env` |
| `faiss-cpu` | 1.15.0 | Busca vetorial local para RAG (não usado em `main.py` ainda) |
| `pypdf` | 6.18.1 | Leitura de PDFs (não usado em `main.py` ainda) |

### ⚠️ Nota sobre a atualização do LangChain (0.3 → 1.x)

O `requirements.txt` original fixava `langchain==0.3.25`. A versão atual (`1.4.0`) é uma major release com mudanças que quebram compatibilidade:

- `langchain.prompts` **não existe mais** — `PromptTemplate` agora vem de `langchain_core.prompts` (já ajustado em `main.py`).
- O pacote `langchain` de topo ficou enxuto e voltado a agentes (`create_agent`); chains legadas (`LLMChain`, etc.) migraram para o pacote `langchain-classic`, que só é necessário se você depender dessas classes antigas.
- `langchain-community` 0.4.x e `langgraph` 1.2.x já são compatíveis com `langchain` 1.4.x (testado localmente sem conflitos de dependência).

Também troquei o modelo padrão de `gpt-3.5-turbo` (legado, sendo descontinuado pela OpenAI) para `gpt-4o-mini`, mais barato e atual.

Se preferir não migrar agora, use a última versão estável da série 0.3: `langchain==0.3.27` + `langchain.prompts` (import original) continuam funcionando.

## Próximos passos

- Usar `pydantic.BaseModel` com `with_structured_output` do `ChatOpenAI` para obter o roteiro em formato estruturado (ex.: lista de dias com atividades) em vez de texto livre.
- Usar `langchain-community` + `faiss-cpu` + `pypdf` para RAG (ex.: gerar roteiros a partir de guias de viagem em PDF).
- Usar `langgraph` para transformar o fluxo em um agente com múltiplas etapas (ex.: pesquisar preços, sugerir hospedagem, revisar o roteiro).
