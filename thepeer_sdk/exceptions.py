
class ThepeerSDKException(Exception):
    """
    An Exception raised when the SDK is used incorrectly.
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKForbiddenException(Exception):
    """
    An Exception raised when your request is forbidden
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKUnauthorizedException(Exception):
    """
    An Exception raised when your request contains an invalid secret key
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKInvalidPayloadException(Exception):
    """
    An Exception raised when your request contains invalid payload
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKInvalidResourceException(Exception):
    """
    An Exception raised when your request is to an invalid URL
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKServiceUnavailableException(Exception):
    """
    An Exception raised when the server is not reachable
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]


class ThepeerSDKServerErrorException(Exception):
    """
    An Exception raised when there is a server error
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]
