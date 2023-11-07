from loguru import logger
from dataiku_mlops.dssclient import DSSClient


class DSSDeployer:
    """
    Handle to interact with the DSS Deployer
    """

    def __init__(self, host, api_key, project_key, infra_id, bundle_id):
        self.client = DSSClient.dssclient(host, api_key)
        self.project_key = project_key
        self.infra_id = infra_id
        self.bundle_id = bundle_id

    def deploy(self) -> object:
        """
        Create a deployment
        """

        # TODO get deployment id
        logger.info("Getting deployment id")

        # TODO update deployment

        # TODO create deployment

        return "deploy"

    def rollback(self) -> object:
        """
        Rollback to the previous deployment
        """

        # TODO get previous bundle id

        # TODO update deployment

        return "rollback"
