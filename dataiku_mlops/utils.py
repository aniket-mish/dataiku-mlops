"""This file contains utility functions for the plugin."""


class MLOpsUtils:
    """
    Utility class for MLOps
    """

    def __init__(self, client, project_key, infra_id):
        self.client = client
        self.project_key = project_key
        self.infra_id = infra_id

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

    def set_bundle_id(self):
        """
        Set the bundle id
        """
        self.get_deployment().get_settings().get_raw()["bundleId"] = self.bundle_id

    def get_previous_bundle_id(self):
        """
        Get the previous bundle id
        """
        return self.get_deployment().get_settings().get_raw()["bundleId"]

    def create_deployment(self):
        """
        Create a deployment
        """
        pass

    def update_deployment(self):
        """
        Update a deployment
        """
        pass


class DSSInfoMessage:
    """
    Class to handle info messages
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"INFO: {self.message}"


class DSSProjectStatus:
    """
    Class to handle project status
    """

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f"Project status: {self.status}"
