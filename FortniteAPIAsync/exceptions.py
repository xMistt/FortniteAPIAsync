class FortniteAPIException(Exception):
    pass


class InvalidParameters(FortniteAPIException):
    pass


class NotFound(FortniteAPIException):
    pass


class UnknownHTTPException(FortniteAPIException):
    pass

