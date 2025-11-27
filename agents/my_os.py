from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from dotenv import load_dotenv
load_dotenv()

assistant = Agent(
    name="My first assistant",
    model=OpenAIChat(id="gpt-4.1-mini"),
    instructions="You are a helpful AI assistant.",
    markdown=True
)

agent_os = AgentOS(
    id="my-first-os",
    description="An OS to manage my first assistant",
    assistants=[assistant]
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="my_os:app", host="0.0.0.0", reload=True)