import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command="uv", args=["run", "minimal_server.py"])


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"{tools = }")

            result = await session.call_tool("date")
            result_structured = result.structuredContent
            print(f"{result_structured = }")


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
