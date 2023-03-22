import pytest
import json

# tests/test_counters.py
def test_get_counters(client):
    response = client.get('/counters')
    assert response.status_code == 200
    counters = json.loads(response.data)
    assert isinstance(counters, list)
    for counter in counters:
        assert "id" in counter
        assert "Name" in counter
        assert "Count" in counter
