from agno.models.groq import Groq
from agno.models.message import Message

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.1-8b-instant")

msg = Message(
    role="user",
    content=[
        {
            "type": "text",
            "text": "Olá, meu nome é Cassius!"
        }
    ]
)

assistant_msg = Message(
    role="assistant"
)

response = model.invoke([msg], assistant_message=assistant_msg)

print(response.content)