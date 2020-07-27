from .http import HTTPClient
from .cosmetics import Cosmetics


class APIClient:
    def __init__(self, api_key: str = None) -> None:
        self.http = HTTPClient(
            headers={
                "x-api-key": api_key
            } if api_key is not None else {}
        )

        self.cosmetics = Cosmetics(self)
