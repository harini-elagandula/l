from phi.agent import Agent
from phi.model.groq import Groq

# Create agent properly (NOT function)
finance_agent = Agent(
    name="Finance AI Agent",
    role="Analyze financial data and give smart suggestions",
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=[
        "Analyze user spending",
        "Calculate total expenses",
        "Detect overspending",
        "Give savings suggestions"
    ],
    show_tool_calls=False,
    markdown=True
)