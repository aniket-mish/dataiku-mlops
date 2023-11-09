from loguru import logger
from dataiku_mlops.dssclient import DSSClient
from dataiku_mlops.utils import DSSHelper


class DSSDeployer:
    """
    Handle to interact with the DSS Deployer
    """

    def __init__(self, host, api_key, project_key, infra_id, bundle_id):
        self.client = DSSClient(host, api_key).dssclient()
        self.project_key = project_key
        self.infra_id = infra_id
        self.bundle_id = bundle_id
        self.utils = DSSHelper(self.client, self.project_key, self.infra_id)

    def deploy(self) -> object:
        """
        Create a deployment
        """
        deployment = DSSHelper(
            self.client, self.project_key, self.infra_id
        ).get_deployment()

        if deployment is not None:
            logger.info(f"Deployment found: {deployment}")

            settings = deployment.get_settings()
            previous_bundle_id = settings.get_raw()["bundleId"]
            logger.info(f"Previous bundle id: {previous_bundle_id}")
            settings.get_raw()["bundleId"] = self.bundle_id

            settings.save()
        else:
            logger.info("No deployment found. Creating a new one.")

            deployment = self.utils.create_deployment(
                deployment_id=f"{self.project_key}-on-{self.infra_id}",
                project_key=self.project_key,
                infra_id=self.infra_id,
                bundle_id=self.bundle_id,
            )

        logger.info(f"Deployment ready to update: {deployment.id}")
        update_execution = deployment.start_update()
        logger.info(f"Deployment updated: {update_execution.get_state()}")
        update_execution.wait_for_result()
        deployment_result = update_execution.get_result()
        logger.info(f"Deployment result: {deployment_result}")

        return deployment
