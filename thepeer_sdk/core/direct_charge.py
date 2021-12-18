from thepeer_sdk.exceptions import ThepeerSDKException


class DirectCharge():

    def __init__(self) -> None:
        if hasattr(self, "api_client"):
            self.api_client = self.api_client
        else:
            raise ThepeerSDKException("api_client instance is required")

        if hasattr(self, "API_BASE_URL"):
            self.API_BASE_URL = self.api_client
        else:
            raise ThepeerSDKException("API_BASE_URL is required")
