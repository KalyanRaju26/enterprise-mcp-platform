from fastmcp import FastMCP

from confluence_client import ConfluenceClient

mcp = FastMCP("Confluence MCP")

client = ConfluenceClient()


@mcp.tool()
def hello():
    return "Confluence MCP is running"


@mcp.tool()
def list_spaces():
    return client.list_spaces()


@mcp.tool()
def search_pages(title: str):
    return client.search_pages(title)

@mcp.tool()
def get_page(page_id: str):
    return client.get_page(page_id)

@mcp.tool()
def search_content(text: str):
    return client.search_content(text)


if __name__ == "__main__":
    mcp.run()