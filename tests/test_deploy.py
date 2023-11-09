import itertools
from unittest.mock import patch, MagicMock
from dataiku_mlops.deploy import DSSDeployer


@patch("dataiku_mlops.deploy.DSSClient")
@patch("dataiku_mlops.deploy.DSSHelper")
def test_deploy_updates_existing_deployment(mock_DSSHelper, mock_DSSClient):
    # Mock the DSSClient and DSSHelper
    mock_client = MagicMock()
    mock_DSSClient.return_value.dssclient.return_value = mock_client
    mock_deployment = MagicMock()
    mock_DSSHelper.return_value.get_deployment.return_value = mock_deployment

    # Mock the update_execution
    mock_update_execution = MagicMock()
    mock_deployment.start_update.return_value = mock_update_execution

    # Test with existing deployment
    deployer = DSSDeployer("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment_result = deployer.deploy()
    assert deployment_result is not None
    mock_deployment.get_settings.assert_called_once()
    mock_deployment.start_update.assert_called_once()
    mock_update_execution.wait_for_result.assert_called_once()


@patch("dataiku_mlops.deploy.DSSClient")
@patch("dataiku_mlops.deploy.DSSHelper")
def test_deploy_creates_new_deployment(mock_DSSHelper, mock_DSSClient):
    # Mock the DSSClient and DSSHelper
    mock_client = MagicMock()
    mock_DSSClient.return_value.dssclient.return_value = mock_client
    mock_DSSHelper.return_value.get_deployment.side_effect = itertools.repeat(None)

    # Mock the new deployment and update_execution
    mock_new_deployment = MagicMock()
    mock_DSSHelper.return_value.create_deployment.return_value = mock_new_deployment
    mock_update_execution = MagicMock()
    mock_new_deployment.start_update.return_value = mock_update_execution

    # Test with no existing deployment
    deployer = DSSDeployer("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment_result = deployer.deploy()
    assert deployment_result is not None
    mock_DSSHelper.create_deployment.assert_called_once()
    mock_new_deployment.start_update.assert_called_once()
    mock_update_execution.wait_for_result.assert_called_once()
