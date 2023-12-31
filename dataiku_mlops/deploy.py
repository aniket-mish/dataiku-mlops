from loguru import logger
from dataiku_mlops.client import Client
from dataiku_mlops.utils import Helper


class Deploy:
    """
    Handle to interact with the DSS Deployer
    """

    def __init__(
        self, host: str, api_key: str, project_key: str, infra_id: str, bundle_id: str
    ):
        self.client = Client(host, api_key).client()
        self.project_key = project_key
        self.infra_id = infra_id
        self.bundle_id = bundle_id
        self.utils = Helper(self.client, project_key, infra_id, bundle_id)

    def get_deployment_status(self, deployment) -> object:
        """
        Get the deployment status
        """
        logger.info(f"Deployment ready to update: {deployment.id}")
        update_execution = deployment.start_update()
        logger.info(f"Deployment updated: {update_execution.get_state()}")
        update_execution.wait_for_result()
        deployment_result = update_execution.get_result()
        logger.info(f"Deployment result: {deployment_result}")
        return deployment_result

    def deploy(self) -> object:
        """
        Create a deployment
        """
        deployment = self.utils.get_deployment()
        if deployment is not None:
            logger.info(f"Deployment found: {deployment}")
            settings = deployment.get_settings()
            previous_bundle_id = settings.get_raw()["bundleId"]
            logger.info(f"Previous bundle id: {previous_bundle_id}")
            settings.get_raw()["bundleId"] = self.bundle_id
            settings.save()
            deployment_result = self.get_deployment_status(deployment)
        else:
            logger.info("No deployment found. Creating a new one.")
            deployment = self.utils.create_deployment()
            deployment_result = self.get_deployment_status(deployment)
        return deployment_result
