from loguru import logger
from dataiku_mlops.dssclient import DSSClient
from dataiku_mlops.utils import MLOpsUtils


class DSSDeployer:
    """
    Handle to interact with the DSS Deployer
    """

    def __init__(self, host, api_key, project_key, infra_id, bundle_id):
        self.client = DSSClient(host, api_key).dssclient()
        self.project_key = project_key
        self.infra_id = infra_id
        self.bundle_id = bundle_id

    def deploy(self) -> object:
        """
        Create a deployment
        """
        deployment = MLOpsUtils(
            self.client, self.project_key, self.infra_id
        ).get_deployment()

        if deployment is not None:
            logger.info(f"Deployment found: {deployment}")

            settings = deployment.get_settings()
            previous_bundle_id = settings.get_raw()["bundleId"]
            logger.info(f"Previous bundle id: {previous_bundle_id}")
            settings.get_raw()["bundleId"] = self.bundle_id
        else:
            logger.info("No deployment found. Creating a new one.")
            # TODO create deployment

        return "deploy"

    def rollback(self) -> object:
        """
        Rollback to the previous deployment
        """

        # TODO get previous bundle id

        # TODO update deployment

        return "rollback"
