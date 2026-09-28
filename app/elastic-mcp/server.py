from fastmcp import FastMCP

from elastic_client import ElasticClient

mcp = FastMCP("Elastic MCP")

client = ElasticClient()


@mcp.tool()
def hello():
    return "Elastic MCP is running"


@mcp.tool()
def get_supported_environments():
    return client.get_supported_environments()


@mcp.tool()
def get_transaction_details(
    environment: str,
    x_request_id: str
):
    """
    Search transaction details using X-Request-ID.
    """

    return client.get_transaction_details(
        environment=environment,
        x_request_id=x_request_id
    )


@mcp.tool()
def search_logs(
    environment: str,
    query: str,
    size: int = 100
):
    """
    Generic log search.
    """

    return client.search_logs(
        environment=environment,
        query=query,
        size=size
    )


if __name__ == "__main__":
    mcp.run()