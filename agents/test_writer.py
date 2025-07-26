def generate_unit_tests(api_path):
    return f"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_{api_path.strip('/').replace('/', '_')}():
    response = client.get("{api_path}")
    assert response.status_code == 200
"""
