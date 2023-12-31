class Helper:
    """
    This class contains utility methods
    """

    def __init__(
        self, client: object, project_key: str, infra_id: str, bundle_id: str
    ) -> None:
        self.client = client
        self.project_key = project_key
        self.infra_id = infra_id
        self.bundle_id = bundle_id

    def get_deployment(self) -> object:
        """
        Get the recent deployment
        """
        proj_deployer = self.client.get_projectdeployer()
        project = proj_deployer.get_project(self.project_key)
        deployments = project.get_status().get_deployments(self.infra_id)
        return deployments[0]

    def get_settings(self) -> object:
        """
        Get the settings of the deployment
        """
        return self.get_deployment().get_settings()

    def get_projectdeployer(self) -> object:
        """
        Get the project deployer
        """
        return self.client.get_projectdeployer()

    def set_bundle_id(self) -> None:
        """
        Set the bundle id
        """
        self.get_deployment().get_settings().get_raw()["bundleId"] = self.bundle_id

    def get_previous_bundle_id(self) -> str:
        """
        Get the previous bundle id
        """
        return self.get_deployment().get_settings().get_raw()["bundleId"]

    def create_deployment(self) -> object:
        """
        Create a deployment
        """
        project_deployer = self.get_projectdeployer()
        project = project_deployer.get_project(self.project_key)
        return project.create_deployment(self.infra_id, self.bundle_id)
