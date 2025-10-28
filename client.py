import asyncio 
from fastmcp import Client, FastMCP 
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import os
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("MCP_BEARER_TOKEN")
# Configure transport with Bearer token authentication
transport = StreamableHttpTransport(
    "http://0.0.0.0:8001/mcp",
    headers={"Authorization": f"Bearer {BEARER_TOKEN}"}
)


client = Client(transport=transport) 
async def main(): 
    async with client: 
        # Ensure client can connect await client.ping() 
        # # List available operations 
        tools = await client.list_tools() 
        print("Available tools:", tools)
        resources = await client.list_resources() 
        prompts = await client.list_prompts() 
        # Ex. execute a tool call 
        result = await client.call_tool("get_weather", {"city": "ahmedabad"}) 
        print(result) 

asyncio.run(main())