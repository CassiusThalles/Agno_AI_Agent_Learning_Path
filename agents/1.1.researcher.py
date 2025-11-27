from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

agent = Agent(
    model=model,
    tools = [
        TavilyTools()
    ]
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Duque de Caxias - RJ.")