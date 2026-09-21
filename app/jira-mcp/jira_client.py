import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()


class JiraClient:

    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.auth = HTTPBasicAuth(
            os.getenv("JIRA_EMAIL"),
            os.getenv("JIRA_TOKEN")
        )

        self.headers = {
            "Accept": "application/json"
        }

    def get_projects(self):
        url = f"{self.base_url}/rest/api/3/project"
        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )
        response.raise_for_status()
        return response.json()

    def search_issues(self, jql: str):

        url = f"{self.base_url}/rest/api/3/search/jql"

        params = {
            "jql": jql,
            "maxResults": 50
        }

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth,
            params=params
        )

        print("STATUS:", response.status_code)
        print(response.text)

        return response.json()

    def get_issue(self, issue_id: str):
        url = f"{self.base_url}/rest/api/3/issue/{issue_id}"
        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )
        print("STATUS:", response.status_code)
        # print(response.text)
        response.raise_for_status()
        return response.json()