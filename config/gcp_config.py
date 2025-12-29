# config/gcp_config.py

import os
from google.oauth2 import service_account


class GCPConfig:
    """
    Google Cloud configuration for:
    - Chirp 2 (Speech-to-Text)
    - Gemini (Vertex AI)
    """

    PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    LOCATION = os.getenv("GCP_LOCATION", "us-central1")

    SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    @staticmethod
    def get_credentials():
        """
        Load service account credentials
        """
        if not GCPConfig.SERVICE_ACCOUNT_FILE:
            raise EnvironmentError(
                "GOOGLE_APPLICATION_CREDENTIALS not set"
            )

        return service_account.Credentials.from_service_account_file(
            GCPConfig.SERVICE_ACCOUNT_FILE
        )

    @staticmethod
    def validate():
        """
        Validate required GCP settings
        """
        if not GCPConfig.PROJECT_ID:
            raise EnvironmentError("GCP_PROJECT_ID is missing")

        if not GCPConfig.SERVICE_ACCOUNT_FILE:
            raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS is missing")
