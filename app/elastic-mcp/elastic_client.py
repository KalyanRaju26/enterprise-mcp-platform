import os
import requests

from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT_INDEX = {
    "dev_i": "dev-nonprod-*",
    "dev_ii": "dev-dte2-service",
    "dev_iii": "dev-dte2-service-new",
    "sit_i": "sit-nonprod-*",
    "sit_ii": "sit-dte2-service",
    "sit_iii": "sit-dte2-service-new",
    "sit3_i": "sit3-nonprod-*",
    "sit3_ii": "sit3-dte2-service",
    "sit3_iii": "sit3-dte2-service-new",
    "devpp_i": "devpp-nonprod-*",
    "devpp_ii": "devpp-dte2-service",
    "uatpp_i": "uatpp-nonprod-*",
    "uatpp_ii": "uatpp-dte2-service"
}


class ElasticClient:

    def __init__(self):

        self.base_url = os.getenv("ELASTIC_URL")

        self.username = os.getenv("ELASTIC_USERNAME")

        self.password = os.getenv("ELASTIC_PASSWORD")

    def get_transaction_details(
        self,
        environment: str,
        x_request_id: str
    ):

        index_name = ENVIRONMENT_INDEX[environment]

        payload = {
            "batch": [
                {
                    "request": {
                        "params": {
                            "index": index_name,
                            "body": {
                                "sort": [
                                    {
                                        "@timestamp": {
                                            "order": "desc"
                                        }
                                    }
                                ],
                                "fields": [
                                    {
                                        "field": "*",
                                        "include_unmapped": True
                                    }
                                ],
                                "size": 500,
                                "query": {
                                    "bool": {
                                        "must": [],
                                        "filter": [
                                            {
                                                "multi_match": {
                                                    "type": "best_fields",
                                                    "query": x_request_id,
                                                    "lenient": True
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "options": {
                        "strategy": "ese",
                        "isSearchStored": False
                    }
                }
            ]
        }

        return {
            "environment": environment,
            "index": index_name,
            "x_request_id": x_request_id,
            "kibana_payload": payload
        }

    def search_logs(
        self,
        environment: str,
        query: str,
        size: int = 100
    ):

        return {
            "environment": environment,
            "index": ENVIRONMENT_INDEX[environment],
            "query": query,
            "size": size
        }

    def get_supported_environments(self):

        return list(ENVIRONMENT_INDEX.keys())