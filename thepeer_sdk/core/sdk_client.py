from thepeer_sdk.core.links import Links
from thepeer_sdk.core.users import Users
from thepeer_sdk.exceptions import ThepeerSDKException
from thepeer_sdk.utils import ApiClient


class ThepeerSdkClient(
    Users,
    Links
):
    """
    :param secret_key:
        secret_key to use with this API. **REQUIRED**
    """

    def __init__(self, secret_key: str):
        if not secret_key or secret_key.strip() == "":
            raise ThepeerSDKException("`secret_key` is required")
        self.API_BASE_URL = "https://api.thepeer.co"
        self.api_client = ApiClient(secret_key)
