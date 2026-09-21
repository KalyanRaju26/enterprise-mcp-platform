import os
from urllib.parse import quote

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()


class ConfluenceClient:

    def __init__(self):
        self.base_url = os.getenv("CONFLUENCE_BASE_URL")

        self.auth = HTTPBasicAuth(
            os.getenv("ATLASSIAN_EMAIL"),
            os.getenv("ATLASSIAN_TOKEN")
        )

    def list_spaces(self):
        url = f"{self.base_url}/rest/api/space"

        response = requests.get(
            url,
            auth=self.auth
        )

        response.raise_for_status()

        data = response.json()

        return [
            {
                "id": space["id"],
                "name": space["name"],
                "key": space["key"]
            }
            for space in data["results"]
        ]

    def get_page(self, page_id: str):
        url = (
            f"{self.base_url}/rest/api/content/"
            f"{page_id}?expand=body.storage"
        )

        response = requests.get(
            url,
            auth=self.auth
        )

        response.raise_for_status()

        page = response.json()

        return {
            "id": page["id"],
            "title": page["title"],
            "content": page["body"]["storage"]["value"]
        }

    def search_pages(self, title: str):
        url = (
            f"{self.base_url}/rest/api/content"
            f"?title={title}&expand=space"
        )

        response = requests.get(
            url,
            auth=self.auth
        )

        response.raise_for_status()

        data = response.json()

        return [
            {
                "id": page["id"],
                "title": page["title"]
            }
            for page in data["results"]
        ]

    def search_content(self, text: str):
        cql = quote(f'text~"{text}"')

        url = (
            f"{self.base_url}/rest/api/content/search"
            f"?cql={cql}"
        )

        response = requests.get(
            url,
            auth=self.auth
        )

        response.raise_for_status()

        data = response.json()

        return [
            {
                "id": page["id"],
                "title": page["title"]
            }
            for page in data["results"]
        ]