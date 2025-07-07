import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ.get(
    "STAGE") == 'qa' else "https://release-gs.qa-playground.com/api/v1"


@pytest.fixture(scope="session")
def init_enviroment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}",
                 "X-Task-Id": "API-1"}
    )
    assert response.status_code == 205
