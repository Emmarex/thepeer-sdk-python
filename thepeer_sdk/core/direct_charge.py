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

    def charge_link(self, link_id: str, amount: int, remark: str) -> dict:
        """
        Charge your user's linked account at any time

        :param link_id: str
            id of the link to charge

        :param amount: int
            amount to charge

        :param remark: str
            narration of the charge
        """

        return self.api_client.make_post(
            url=f'{self.API_BASE_URL}/link/{link_id}/charge',
            data={
                "amount": amount,
                "remark": remark
            }
        )

    def authorize_charge(self, charge_ref: str, event: str) -> dict:
        """
        authorize direct charge request via webhooks

        :param charge_ref: str
            direct charge reference

        :param event: str
            possible values - "success", "insufficient_funds", "business_decline" or
            "user_decline"
        """

        if not charge_ref or charge_ref.strip() == "":
            raise ThepeerSDKException(
                "`charge_ref` cannot be an empty string")

        if event not in ["success", "insufficient_funds", "business_decline", "user_decline"]:
            raise ThepeerSDKException(
                "Invalid `event`.")

        return self.api_client.make_post(
            url=f'{self.API_BASE_URL}/debit/{charge_ref}',
            data={
                "event": event
            }
        )
