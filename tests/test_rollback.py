import pytest
from unittest.mock import patch, MagicMock
from dataiku_mlops.rollback import Rollback
from dataiku_mlops.utils import Helper
from dataiku_mlops.client import Client


@patch.object(Client, "client")
@patch.object(Helper, "get_previous_bundle_id")
@patch.object(Helper, "get_deployment")
def test_rollback_exception_raised(
    mock_get_deployment, mock_get_previous_bundle_id, mock_dssclient
):
    # Mock the Client and Helper
    mock_dssclient.return_value = MagicMock()
    mock_get_previous_bundle_id.return_value = "previous_bundle_id"

    # Test rollback with previous bundle
    rollback = Rollback("host", "api_key", "project_key", "infra_id", "bundle_id")
    with pytest.raises(
        Exception, match="Rollback not possible. Please fix it manually."
    ):
        rollback.rollback()


@patch.object(Client, "client")
@patch.object(Helper, "get_previous_bundle_id")
@patch.object(Helper, "set_bundle_id")
@patch.object(Helper, "get_deployment")
def test_rollback_successful(
    mock_get_deployment, mock_set_bundle_id, mock_get_previous_bundle_id, mock_dssclient
):
    # Mock the Client and Helper
    mock_dssclient.return_value = MagicMock()
    mock_get_previous_bundle_id.return_value = None
    mock_deployment = MagicMock()
    mock_get_deployment.return_value = mock_deployment
    mock_update_execution = MagicMock()
    mock_deployment.start_update.return_value = mock_update_execution

    # Test rollback without previous bundle
    rollback = Rollback("host", "api_key", "project_key", "infra_id", "bundle_id")
    result = rollback.rollback()
    assert result == "Rollback done"
    mock_set_bundle_id.assert_called_once()
    mock_deployment.start_update.assert_called_once()
    mock_update_execution.wait_for_result.assert_called_once()
