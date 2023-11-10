import pytest
from unittest.mock import patch
from dataiku_mlops.client import Client


@patch("dataikuapi.DSSClient")
def test_client_creation_with_valid_api_key(mock_DSSClient):
    # Test with valid host and API key
    client = Client("host", "api_key")
    dss_client = client.client()
    assert dss_client is not None
    mock_DSSClient.assert_called_once_with("host", "api_key")


def test_client_creation_with_empty_api_key():
    # Test with empty API key
    client = Client("host", None)
    with pytest.raises(ValueError):
        client.client()
