from fastmcp import FastMCP
from jira_client import JiraClient

mcp = FastMCP("Jira MCP")

client = JiraClient()


@mcp.tool()
def hello():
    return "Jira MCP is running"


@mcp.tool()
def get_projects():
    return client.get_projects()


@mcp.tool()
def search_issues(jql: str):
    return client.search_issues(jql)


@mcp.tool()
def get_issue(issue_id: str):
    return client.get_issue(issue_id)


if __name__ == "__main__":
    mcp.run()