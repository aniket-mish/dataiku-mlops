from unittest.mock import patch, MagicMock
from dataiku_mlops.deploy import DSSDeployer


@patch("dataiku_mlops.deploy.DSSClient")
@patch("dataiku_mlops.deploy.MLOpsUtils")
def test_deploy_with_existing_deployment(mock_MLOpsUtils, mock_DSSClient):
    # Mock the DSSClient and MLOpsUtils
    mock_client = MagicMock()
    mock_DSSClient.return_value.dssclient.return_value = mock_client
    mock_deployment = MagicMock()
    mock_MLOpsUtils.return_value.get_deployment.return_value = mock_deployment

    # Test with existing deployment
    deployer = DSSDeployer("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment = deployer.deploy()
    assert deployment is not None
    mock_deployment.get_settings.assert_called_once()


@patch("dataiku_mlops.deploy.DSSClient")
@patch("dataiku_mlops.deploy.MLOpsUtils")
def test_deploy_with_no_existing_deployment(mock_MLOpsUtils, mock_DSSClient):
    # Mock the DSSClient and MLOpsUtils
    mock_client = MagicMock()
    mock_DSSClient.return_value.dssclient.return_value = mock_client
    mock_MLOpsUtils.return_value.get_deployment.return_value = None

    # Test with no existing deployment
    deployer = DSSDeployer("host", "api_key", "project_key", "infra_id", "bundle_id")
    deployment = deployer.deploy()
    assert deployment is not None
    mock_MLOpsUtils.create_deployment.assert_called_once()