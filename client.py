import asyncio 
from fastmcp import Client, FastMCP 
client = Client("https://alive-maroon-tern.fastmcp.app/mcp") 
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