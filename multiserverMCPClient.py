import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("MCP_BEARER_TOKEN")

async def main():
    # Define MCP server configuration with Bearer token
    # MultiServerMCPClient expects a dictionary where keys are server names
    servers = {
        "local-mcp": {  # identifier for the server as key
            "transport": "streamable_http",
            "url": "http://0.0.0.0:8001/mcp",
            "headers": {
                "Authorization": f"Bearer {BEARER_TOKEN}"
            },
        }
    }

    # Initialize MultiServerMCPClient with your server dict
    client = MultiServerMCPClient(connections=servers)

    tools = await client.get_tools()
    print("Available tools:", tools)
    


if __name__ == "__main__":
    asyncio.run(main())
