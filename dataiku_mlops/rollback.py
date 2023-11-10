from loguru import logger
from dataiku_mlops.utils import Helper
from dataiku_mlops.client import Client


class Rollback:
    def __init__(
        self, host: str, api_key: str, project_key: str, infra_id: str, bundle_id: str
    ):
        self.client = Client(host, api_key).client()
        self.project_key = project_key
        self.infra_id = infra_id
        self.utils = Helper(self.client, self.project_key, self.infra_id, bundle_id)

    def rollback(self) -> str:
        """
        Rollback to the previous deployment
        """
        previous_bundle_id = self.utils.get_previous_bundle_id()
        if previous_bundle_id is not None:
            raise Exception("Rollback not possible. Please fix it manually.")
        else:
            logger.info("Rollback to the previous deployment")
            self.utils.set_bundle_id(previous_bundle_id)
            deployment = self.utils.get_deployment()
            update_execution = deployment.start_update()
            update_execution.wait_for_result()
            logger.info(f"Deployment updated: {update_execution.get_state()}")
            deployment_result = update_execution.get_result()
            logger.info(f"Deployment result: {deployment_result}")
            return "Rollback done"
