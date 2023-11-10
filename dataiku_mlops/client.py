import dataikuapi


class Client:
    """
    Entry point for the Dataiku API client.
    """

    def __init__(self, host: str, api_key: str) -> None:
        """
        Initialize the Client with the host and API key.
        """
        self.host = host
        self.api_key = api_key

    def client(self) -> object:
        """
        Create the DSSClient object.
        """
        if self.api_key is not None:
            return dataikuapi.DSSClient(self.host, self.api_key)
        else:
            raise ValueError("API key is required.")
