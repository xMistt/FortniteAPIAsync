from .enums import *
from .exceptions import *

from typing import Optional


class BRStats:
    pass


class Stats:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_stats_from_name(self,
                                  name: str = None,
                                  account_type: Optional[AccountType] =
                                  AccountType.EPIC,
                                  time_window: Optional[StatsTimeWindow] =
                                  StatsTimeWindow.LIFETIME,
                                  image: Optional[StatsImage] =
                                  None) -> BRStats:
        if not name:
            raise InvalidParameters("Missing name parameter.")

        data = await self.http.request(
            method="GET",
            url="/v1/stats/br/v2",
            params={
                "name": name,
                "accountType": account_type.value,
                "timeWindow": time_window.value,
                "image": image.value if image is not None else "none"
            }
        )

        if data['status'] == 404:
            raise NotFound(f"{data['error'][0].upper()}"
                           f"{data['error'][1:]}.")

        return None


raise NotImplementedError('Stats is not ready yet.')

