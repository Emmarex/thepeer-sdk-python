import json

from requests import Response, request

from thepeer_sdk import __api_version__, exceptions
from thepeer_sdk.exceptions import (ThepeerSDKForbiddenException,
                                    ThepeerSDKInvalidPayloadException,
                                    ThepeerSDKInvalidResourceException,
                                    ThepeerSDKServerErrorException,
                                    ThepeerSDKServiceUnavailableException,
                                    ThepeerSDKUnauthorizedException)


class ApiClient(object):
    """
    Thepeer Python SDK API Client
    """

    def __init__(self, secret_key: str):
        """
        Create and instance of Thepeer's API Client
        This API CLient will be used to make calls to Thepeer's API
        """
        self.__baseHeaders = {
            'User-Agent': f'Thepeer Python SDK v{__api_version__}',
            'x-sdk-type': 'Python',
            'x-sdk-version': __api_version__,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Api-Key': secret_key
        }

    def _process_response(self, response: Response) -> dict:
        response_json = response.json()
        if response.status_code == 201 or response.status_code == 200:
            return response_json
        elif response.status_code == 401:
            raise ThepeerSDKUnauthorizedException(
                f'{response.reason}: {response_json["message"]}')
        elif response.status_code == 403:
            raise ThepeerSDKForbiddenException(
                f'{response.reason}: {response_json["message"]}')
        elif response.status_code == 404:
            raise ThepeerSDKInvalidResourceException(
                f'{response.reason}: {response_json["message"]}')
        elif response.status_code == 422:
            for item in response_json['errors'].values():
                raise ThepeerSDKInvalidPayloadException(item[0])
            raise
        elif response.status_code == 406:
            raise ThepeerSDKForbiddenException(
                f'{response.reason}: {response_json["message"]}')
        elif response.status_code == 503:
            raise ThepeerSDKServiceUnavailableException(
                f'{response.reason}: {response_json["message"]}')
        else:
            raise ThepeerSDKServerErrorException(
                f'{response.reason}: {response_json["message"]}')

    def _make_request(self, method: str, route: str, payload: dict, query_params: dict = {}, request_files: list = None) -> dict:
        response = request(
            method=method,
            url=route,
            headers=self.__baseHeaders,
            files=request_files,
            data=payload if request_files is not None else json.dumps(payload),
            params=query_params
        )
        return self._process_response(response)

    def make_post(self, url: str, params: dict = {}, data: dict = {}, files: list = None) -> dict:
        return self._make_request(
            method="POST",
            route=url,
            payload=data,
            query_params=params,
            request_files=files
        )

    def make_get(self, url: str, params: dict = {}, data: dict = {}) -> dict:
        return self._make_request(
            method="GET",
            route=url,
            payload=data,
            query_params=params
        )

    def make_put(self, url: str, params: dict = {}, data: dict = {}, files=None) -> dict:
        return self._make_request(
            method="PUT",
            route=url,
            payload=data,
            query_params=params,
            request_files=files
        )

    def make_delete(self, url: str, params: dict = {}) -> dict:
        return self._make_request(
            method="DELETE",
            route=url,
            payload={},
            query_params=params
        )
