import pytest
from unittest.mock import patch
from dataiku_mlops.dssclient import DSSClient


@patch("dataikuapi.DSSClient")
def test_dssclient_with_valid_api_key(mock_DSSClient):
    # Test with valid host and API key
    client = DSSClient("host", "api_key")
    assert client.dssclient() is not None
    mock_DSSClient.assert_called_once_with("host", "api_key")


def test_dssclient_with_none_api_key():
    # Test with None API key
    client = DSSClient("host", None)
    with pytest.raises(ValueError):
        client.dssclient()
