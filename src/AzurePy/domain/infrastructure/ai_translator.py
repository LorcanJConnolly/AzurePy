from domain.azure_service import AzureServiceABC
from azure.ai.translation.text import TextTranslationClient

class AiTranslatorService(AzureServiceABC):
    def __init__(self, name, endpoint, credentials_kwargs):
        credentials = self.from_dict(**credentials_kwargs)
        super().__init__(name, endpoint, credentials=TextTranslationClient(credentials))
    

    def from_dict(self, credentials_kwargs):
        pass

    def authorise(self):
        # this class shouldnt hold authorisation methods
        return TextTranslationClient(credentials)

credentials = ("key", "region")
AiTranslatorService("name", "endpoint", credentials)