from thepeer_sdk.exceptions import ThepeerSDKException


class Users():

    def __init__(self) -> None:
        if hasattr(self, "api_client"):
            self.api_client = self.api_client
        else:
            raise ThepeerSDKException("api_client instance is required")

        if hasattr(self, "API_BASE_URL"):
            self.API_BASE_URL = self.api_client
        else:
            raise ThepeerSDKException("API_BASE_URL is required")

    def index_user(self, name: str, identifier: str, email: str) -> dict:
        """
        Index a particular user on Thepeer

        :param name: str

        :param identifier: str
            unique user identifier

        :param email: str

        """
        return self.api_client.make_post(
            url=f'{self.API_BASE_URL}/users',
            data={
                "name": name,
                "identifier": identifier,
                "email": email
            }
        )

    def list_users(self, page: int = 1, perPage: int = 10) -> dict:
        """
        Get the list of all indexed users

        :param page: int
            page number to return

        :param perPage: int
            amount of records to return per page
        """
        return self.api_client.make_get(
            url=f'{self.API_BASE_URL}/users',
        )

    def update_user(self, user_ref: str, user_identifier: str) -> dict:
        """
        Update your user's identifier when they make a profile update
        to their identifier on your platform.

        :param user_ref: str
            the reference returned when the user was indexed

        :param user_identifier: str
            unique user identifier
            **NOTE**: You cannot update an identifier from username to email and vice versa
        """

        if not user_ref or user_ref.strip() == "":
            raise ThepeerSDKException(
                "`user_ref` cannot be an empty string")

        if not user_identifier or user_identifier.strip() == "":
            raise ThepeerSDKException(
                "`user_identifier` cannot be an empty string")

        return self.api_client.make_put(
            url=f'{self.API_BASE_URL}/users/{user_ref}',
            data={
                "identifier": user_identifier
            }
        )

    def delete_user(self, user_ref: str) -> dict:
        """
        Delete a user in the event that a user deactivates their
        account on your platform

        :param user_ref: str
            the reference returned when the user was indexed
        """

        return self.api_client.make_delete(
            url=f'{self.API_BASE_URL}/users/{user_ref}',
        )
