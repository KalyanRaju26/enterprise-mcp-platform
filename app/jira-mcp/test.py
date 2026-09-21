from jira_client import JiraClient

client = JiraClient()

# get projects
print("\nGET_PROJECTS")
projects = client.get_projects()
print(type(projects))
for project in projects:
    print(project["key"], "-", project["name"])

# search issues
print("\nSEARCH_ISSUES")
result = client.search_issues("project = KAN")
print("Issues Found:", len(result["issues"]))
for issue in result["issues"]:
    print(issue["id"])

# get issues
print("\nGET_ISSUES_WITH_ID")
issue = client.get_issue("10002")
print(issue["key"])
print(issue["fields"]["summary"])



