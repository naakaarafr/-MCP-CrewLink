import warnings
import os
from pydantic import PydanticDeprecatedSince20
from mcp.client.stdio import StdioServerParameters
from crewai import Agent, Task, Crew

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)

# Filesystem server configuration
server_params = StdioServerParameters(
    command="npx",
    args=[
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/tylerreed/Downloads",
    ]
)

# Brave search server configuration
brave_search_params = StdioServerParameters(
    command="npx",
    args=[
        "-y",
        "@modelcontextprotocol/server-brave-search",
    ],
    env={"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
)

# Image server configuration
image_server_params = StdioServerParameters(
    command="python3",
    args=[
        "servers/image_server.py",
    ],
    env={
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"), 
        "OPENAI_ORGANIZATION": os.getenv("OPENAI_ORGANIZATION")
    }
)

# Example usage (you'll need to implement your server connection logic)
if __name__ == "__main__":
    print("Server parameters configured successfully")
    print(f"Filesystem server: {server_params}")
    print(f"Brave search server: {brave_search_params}")
    print(f"Image server: {image_server_params}")
    
    # TODO: Initialize MCP tools here
    # For now, using empty list to prevent NameError
    tools = []  # Replace with actual MCP tools when implemented
    
    # Example: Using the tools from the Stdio MCP server in a CrewAI Agent
    agent = Agent(
        role="Creator",
        goal="You are an amazing AI Creator who uses MCP Tools.",
        backstory="An AI that can create images via an MCP tool.",
        tools=tools,
        verbose=True,
    )
    
    task = Task(
        description="""I need you to research Model Context Protocol and create an in-depth diagram on how it works.""",
        expected_output="A summary of the brave search results and a successful image creation.",
        agent=agent,
    )
    
    summary_task = Task(
        description="Summarize the results of the task and create a text file in the downloads folder (check allowed folders) and save it.",
        expected_output="A summary of the brave search results in a text file in the downloads folder.",
        agent=agent,
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[task, summary_task],
        verbose=True,
    )
    
    result = crew.kickoff()
    print(result)