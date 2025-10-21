from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()


async def main():
    # Step 1: Define your remote MCP server(s)
    mcp_servers = {
    "weather-mcp": {  # server name as key
        "url": "https://alive-maroon-tern.fastmcp.app/mcp",
        "transport":"streamable_http"  # optional
    }
}
    # Read API key
    api_key = os.getenv("GOOGLE_API_KEY")
    # Create Gemini client
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",   # or "gemini-1.5-pro"
        temperature=0.7,
        google_api_key=api_key   # or set GOOGLE_API_KEY in env
    )
    # Step 2: Initialize MultiServerMCPClient
    mcp_client = MultiServerMCPClient(mcp_servers)
    
    # Step 3: Fetch all tools from the MCP servers
    tools = await mcp_client.get_tools()  # returns a list of tool objects

    print("Discovered MCP tools:", [tool.name for tool in tools])

    # Step 4: Create a LangGraph React agent with these tools
    agent = create_agent(
        name="weather-agent",
        model=llm,
        #description="Agent that can answer weather questions using remote MCP tools",
        tools=tools,  # Pass tools retrieved from MCP client
    )

    # Step 5: Ask the agent a question
    user_query = "What's the weather in Ahmedabad right now?"
    response = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": user_query}
        ]
    })

    print("Agent response:", response["messages"][-1].content)

import asyncio
asyncio.run(main())