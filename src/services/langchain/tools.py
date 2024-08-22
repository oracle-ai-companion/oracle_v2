from langchain.agents import Tool
from langchain.utilities import DuckDuckGoSearchAPIWrapper

def get_tools():
    search = DuckDuckGoSearchAPIWrapper()
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events or the current state of the world"
        ),
        # Add more tools here as needed
    ]
    return tools
