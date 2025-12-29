# integrations/jira.py

import os
import requests
from requests.auth import HTTPBasicAuth


class JiraClient:
    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.email = os.getenv("JIRA_EMAIL")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY")

        if not all([self.base_url, self.email, self.api_token, self.project_key]):
            raise EnvironmentError("Jira environment variables not set")

        self.auth = HTTPBasicAuth(self.email, self.api_token)

    def create_issue(self, summary: str, description: str, issue_type="Task"):
        url = f"{self.base_url}/rest/api/3/issue"

        payload = {
            "fields": {
                "project": {"key": self.project_key},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [{
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}]
                    }]
                },
                "issuetype": {"name": issue_type}
            }
        }

        response = requests.post(
            url,
            json=payload,
            auth=self.auth,
            headers={"Accept": "application/json"}
        )

        response.raise_for_status()
        return response.json()["key"]
