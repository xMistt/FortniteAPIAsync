from .http import HTTPClient
from .cosmetics import Cosmetics
from .enums import AESKeyFormat, StatsTimeWindow, StatsImage, AccountType

from .aes import AESKeys
from .creator_code import CreatorCode
from .map import Map
from .news import News
from .playlists import Playlist
from .stats import Stats
from .banners import Banner, BannerColor
from .shop import Shop


class APIClient:
    def __init__(self, api_key: str = None, **kwargs) -> None:
        self.http = HTTPClient(
            headers={
                "Authorization": api_key
            } if api_key is not None else {},
            **kwargs
        )

        self.cosmetics = Cosmetics(self)

    async def close(self) -> None:
        await self.http.close()

    async def get_aes(self,
                      key_format: AESKeyFormat = AESKeyFormat.HEX
                      ) -> AESKeys:
        data = await self.http.api_request(
            url='/v2/aes',
            params={
                "keyFormat": key_format.value
            }
        )
        return AESKeys(data)

    async def get_creator_code(self, name: str) -> CreatorCode:
        data = await self.http.api_request(
            url='/v2/creatorcode',
            params={
                "name": name
            }
        )
        return CreatorCode(data)

    async def get_map(self, language: str = "en") -> Map:
        data = await self.http.api_request(
            url='/v1/map',
            params={
                "language": language
            }
        )
        return Map(data)

    async def get_news(self, language: str = "en") -> News:
        data = await self.http.api_request(
            url='/v2/news/br',
            params={
                "language": language
            }
        )
        return News(data)

    async def get_playlists(self, language: str = "en") -> list[Playlist]:
        data = await self.http.api_request(
            url='/v1/playlists',
            params={
                "language": language
            }
        )
        return [Playlist(raw_playlist) for raw_playlist in data]

    async def get_playlist_by_id(self,
                                 playlist_id: str,
                                 language: str = "en"
                                 ) -> Playlist:
        data = await self.http.api_request(
            url=f'/v1/playlists/{playlist_id}',
            params={
                "language": language
            }
        )
        return Playlist(data)

    async def get_stats(
        self,
        name: str,
        account_type: AccountType = AccountType.EPIC,
        time_window: StatsTimeWindow = StatsTimeWindow.LIFETIME,
        image: StatsImage = StatsImage.NONE
    ) -> Stats:
        data = await self.http.api_request(
            url=f'/v2/stats/br/v2',
            params={
                "name": name,
                "accountType": account_type.value,
                "timeWindow": time_window.value,
                "image": image.value
            }
        )
        return Stats(data)

    async def get_stats_by_id(
        self,
        account_id: str,
        time_window: StatsTimeWindow = StatsTimeWindow.LIFETIME,
        image: StatsImage = StatsImage.NONE
    ) -> Stats:
        data = await self.http.api_request(
            url=f'/v2/stats/br/v2/{account_id}',
            params={
                "timeWindow": time_window.value,
                "image": image.value
            }
        )
        return Stats(data)

    async def get_banners(self,
                          language: str = "en"
                          ) -> list[Banner]:
        data = await self.http.api_request(
            url=f'/v1/banners',
            params={
                "language": language
            }
        )
        return [Banner(raw_banner) for raw_banner in data]

    async def get_banner_colors(self,
                                language: str = "en"
                                ) -> list[BannerColor]:
        data = await self.http.api_request(
            url=f'/v1/banners/colors',
            params={
                "language": language
            }
        )
        return [BannerColor(raw_colour) for raw_colour in data]

    async def get_shop(self,
                       language: str = "en"
                       ) -> Shop:
        data = await self.http.api_request(
            url=f'/v2/shop',
            params={
                "language": language
            }
        )
        return Shop(data)