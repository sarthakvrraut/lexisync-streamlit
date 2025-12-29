# integrations/google_docs.py

from googleapiclient.discovery import build
from google.oauth2 import service_account
from config.gcp_config import GCPConfig


class GoogleDocsExporter:
    def __init__(self):
        creds = GCPConfig.get_credentials()
        self.service = build(
            "docs",
            "v1",
            credentials=creds
        )

    def create_document(self, title: str, content: str) -> str:
        """
        Creates a Google Doc and writes content
        Returns document ID
        """
        doc = self.service.documents().create(
            body={"title": title}
        ).execute()

        doc_id = doc["documentId"]

        requests = [
            {
                "insertText": {
                    "location": {"index": 1},
                    "text": content
                }
            }
        ]

        self.service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests}
        ).execute()

        return doc_id
