import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Minimal Sample", json_response=True)


@mcp.tool()
def date() -> str:
    """Get the current date and time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    mcp.run(transport="stdio")
