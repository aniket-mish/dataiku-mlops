from unittest.mock import patch, MagicMock
from dataiku_mlops.deploy import Deploy


@patch("dataiku_mlops.deploy.Client")
@patch("dataiku_mlops.deploy.Helper")
def test_deploy_updates_existing_deployment(mock_Helper, mock_DSSClient):
    # Mock the Client and Helper
    mock_client = MagicMock()
    mock_DSSClient.return_value.client.return_value = mock_client
    mock_deployment = MagicMock()
    mock_Helper.return_value.get_deployment.return_value = mock_deployment

    # Mock the update_execution
    mock_update_execution = MagicMock()
    mock_deployment.start_update.return_value = mock_update_execution

    # Test with existing deployment
    deployer = Deploy("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment_result = deployer.deploy()
    assert deployment_result is not None
    mock_deployment.get_settings.assert_called_once()
    mock_deployment.start_update.assert_called_once()
    mock_update_execution.wait_for_result.assert_called_once()


@patch("dataiku_mlops.deploy.Client")
@patch("dataiku_mlops.deploy.Helper")
def test_deploy_creates_new_deployment(mock_Helper, mock_Client):
    # Mock the DSSClient and DSSHelper
    mock_client = MagicMock()
    mock_Client.return_value.client.return_value = mock_client

    # Mock the DSSHelper to return None for get_deployment
    mock_Helper.return_value.get_deployment.return_value = None

    # Test deploy with no existing deployment
    deployer = Deploy("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment_result = deployer.deploy()
    assert deployment_result is not None
    mock_Helper.return_value.get_deployment.assert_called_once()
    mock_Helper.return_value.create_deployment.assert_called_once()
