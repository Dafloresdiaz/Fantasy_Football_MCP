import asyncio
from fastmcp import Client

client = Client("main.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result.data)

asyncio.run(call_tool("Ford"))