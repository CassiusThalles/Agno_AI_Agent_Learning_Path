from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.agent import Agent
from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

agent = Agent(
    model=model,
    tools=[
        YFinanceTools()
    ],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto"
)

agent.print_response("Use suas ferramentas para pesquisas o preço atual da empresa brasileira Vale S.A.")