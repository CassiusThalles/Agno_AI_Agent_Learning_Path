from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
load_dotenv()

model = OpenAIChat(id='gpt-4.1-mini')

def celsius_to_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit.
    
    Args:
        celsius (float): Temperatura em graus Celsius.
    
    Returns:
        float: Temperatura em graus Fahrenheit.
    """
    return (celsius * 9/5) + 32

agent = Agent(
    model=model,
    tools = [
        TavilyTools(),
        celsius_to_fahrenheit
    ],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Duque de Caxias - RJ em Fahrenheit.")