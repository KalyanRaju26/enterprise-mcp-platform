from fastmcp import FastMCP

from elastic_client import ElasticClient

mcp = FastMCP("Elastic MCP")

client = ElasticClient()


@mcp.tool()
def hello():
    """
    Health check.
    """
    return "Elastic MCP is running"


@mcp.tool()
def search_by_x_request_id(
    environment: str,
    x_request_id: str
):
    """
    Search logs using X-Request-ID.
    """
    return client.search_by_x_request_id(
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


@mcp.tool()
def get_transaction_trace(
    environment: str,
    x_request_id: str
):
    """
    Get transaction flow using X-Request-ID.
    """
    return client.get_transaction_trace(
        environment=environment,
        x_request_id=x_request_id
    )


@mcp.tool()
def get_request_payload(
    environment: str,
    x_request_id: str
):
    """
    Retrieve request payload.
    """
    return client.get_request_payload(
        environment=environment,
        x_request_id=x_request_id
    )


@mcp.tool()
def get_response_payload(
    environment: str,
    x_request_id: str
):
    """
    Retrieve response payload.
    """
    return client.get_response_payload(
        environment=environment,
        x_request_id=x_request_id
    )


@mcp.tool()
def get_endpoint_details(
    environment: str,
    x_request_id: str
):
    """
    Retrieve endpoint, method and query params.
    """
    return client.get_endpoint_details(
        environment=environment,
        x_request_id=x_request_id
    )


@mcp.tool()
def get_error_details(
    environment: str,
    x_request_id: str
):
    """
    Retrieve exception information.
    """
    return client.get_error_details(
        environment=environment,
        x_request_id=x_request_id
    )


if __name__ == "__main__":
    mcp.run()