from abc import ABC

class AzureServiceABC(ABC):
    def __init__(self, name, endpoint, credential):
        self.name = name
        self.endpoint = endpoint
        self.credential = credential
    
    class ApiRequestClient:
        @property
        def create_request(self):
            pass