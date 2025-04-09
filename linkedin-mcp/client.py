import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def main():
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "linkedin-mcp"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)
            result = await session.call_tool("linkedin_analyze", {"url": "https://www.linkedin.com/in/cmpxchg16", "cookies": """[]"""})
            print(result)

asyncio.run(main())
