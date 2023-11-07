import dataikuapi


class DSSClient:
    """Entry point for the Dataiku API client."""

    def __init__(self, host, api_key):
        """Initialize the DSSClient with the host and API key."""
        self.host = host
        self.api_key = api_key

    def dssclient(self) -> object:
        return dataikuapi.DSSClient(self.host, self.api_key)
