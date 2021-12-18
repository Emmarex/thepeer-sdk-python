from thepeer_sdk.exceptions import ThepeerSDKException


class Links():

    def __init__(self) -> None:
        if hasattr(self, "api_client"):
            self.api_client = self.api_client
        else:
            raise ThepeerSDKException("api_client instance is required")

        if hasattr(self, "API_BASE_URL"):
            self.API_BASE_URL = self.api_client
        else:
            raise ThepeerSDKException("API_BASE_URL is required")

    def get_user_links(self, user_ref: str) -> dict:
        """
        This returns all linked accounts associated with a user.

        :params user_ref: str
            the reference returned when the user was indexed
        """

        if not user_ref or user_ref.strip() == "":
            raise ThepeerSDKException(
                "`user_ref` cannot be an empty string")

        return self.api_client.make_get(
            url=f'{self.API_BASE_URL}/users/{user_ref}/links',
        )

    def get_link(self, link_id: str) -> dict:
        """
        Get a linked account details

        :params link_id: str
            link ID
        """

        if not link_id or link_id.strip() == "":
            raise ThepeerSDKException(
                "`link_id` cannot be an empty string")

        return self.api_client.make_get(
            url=f'{self.API_BASE_URL}/link/{link_id}',
        )
