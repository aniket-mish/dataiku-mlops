from loguru import logger
from dataiku_mlops.utils import MLOpsUtils
from dataiku_mlops.dssclient import DSSClient


class DSSRollback:
    def __init__(self, host, api_key, project_key, infra_id):
        self.client = DSSClient(host, api_key).dssclient()
        self.project_key = project_key
        self.infra_id = infra_id

    def rollback(self) -> str:
        """
        Rollback to the previous deployment
        """

        previous_bundle_id = MLOpsUtils(
            self.client, self.project_key, self.infra_id
        ).get_previous_bundle_id()

        if previous_bundle_id is not None:
            raise Exception("Rollback not possible. Please fix it manually.")

        else:
            logger.info("Rollback to the previous deployment")
            MLOpsUtils.set_bundle_id(previous_bundle_id)
            deployment = MLOpsUtils.get_deployment()
            update_execution = deployment.start_update()
            update_execution.wait_for_result()
            logger.info(f"Deployment updated: {update_execution.get_state()}")
            deployment_result = update_execution.get_result()
            logger.info(f"Deployment result: {deployment_result}")
            return "Rollback done"
