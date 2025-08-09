from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model = "gpt-4o-mini", temperature = 0.2)
parser = PydanticOutputParser(pydantic_object = ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Eres un asistente de investigación. Responde en español. "
     "Usa las herramientas disponibles cuando sea necesario. "
     "Devuelve SOLO el objeto en el siguiente formato:\n{format_instructions}"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions = parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools
)

agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)

query = input("¿Sobre qué tema te ayudo a investigar? ")
raw_response = agent_executor.invoke({"input": query})

try:
    # Note: AgentExecutor returns {"output": "<text>"}
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("Error al parsear:", e, "\nRaw response:", raw_response)