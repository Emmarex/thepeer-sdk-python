from thepeer_sdk.exceptions import ThepeerSDKException


class Send():

    def __init__(self) -> None:
        if hasattr(self, "api_client"):
            self.api_client = self.api_client
        else:
            raise ThepeerSDKException("api_client instance is required")

        if hasattr(self, "API_BASE_URL"):
            self.API_BASE_URL = self.api_client
        else:
            raise ThepeerSDKException("API_BASE_URL is required")

    def verify_receipt(self, receipt_ref: str) -> dict:
        """
        Verify a particular receipt.
        A receipt is an identifier for a pending transaction.

        :param receipt_ref: str
            reference of the receipt to process
        """

        if not receipt_ref or receipt_ref.strip() == "":
            raise ThepeerSDKException(
                "`receipt_ref` cannot be an empty string")

        return self.api_client.make_get(
            url=f'{self.API_BASE_URL}/send/{receipt_ref}',
        )

    def process_receipt(self, receipt_ref: str, event: str) -> dict:
        """
        Process receipts generated from Thepeer inline.

        :param receipt_ref: str
            reference of the receipt to process

        :param event: str
            possible values - "success" or "insufficient_funds"
        """

        if not receipt_ref or receipt_ref.strip() == "":
            raise ThepeerSDKException(
                "`receipt_ref` cannot be an empty string")

        if event not in ["success", "insufficient_funds"]:
            raise ThepeerSDKException(
                "Invalid `event`. Possible values are 'success' and 'insufficient_funds' ")

        return self.api_client.make_post(
            url=f'{self.API_BASE_URL}/send/{receipt_ref}',
            data={
                "event": event
            }
        )
