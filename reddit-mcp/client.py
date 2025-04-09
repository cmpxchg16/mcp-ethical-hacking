import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def main():
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "reddit-mcp"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)
            result = await session.call_tool("reddit_extract", {"url": "https://www.reddit.com/r/ChatGPTCoding/comments/1jgmri6/the_ai_coding_war_is_getting_interesting/"})
            print(result)


asyncio.run(main())
