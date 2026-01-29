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
        """|coro|

        Return information about the current build including
        the main aes key and all dynamic keys.

        Parameters
        ----------
        key_format: :class:`AESKeyFormat`
            Sets the AES key format, defaults to `AESKeyFormat.HEX`.

        Returns
        -------
        :class:`AESKeys`
        """
        data = await self.http.api_request(
            url='/v2/aes',
            params={
                "keyFormat": key_format.value
            }
        )
        return AESKeys(data)

    async def get_creator_code(self, name: str) -> CreatorCode:
        """|coro|

        Return all information about a specific Creator Code such as owner's
        Epic account, whether its verified and whether its active.

        Parameters
        ----------
        name: :class:`str`
            The creator code to get information for.

        Returns
        -------
        :class:`CreatorCode`
        """
        data = await self.http.api_request(
            url='/v2/creatorcode',
            params={
                "name": name
            }
        )
        return CreatorCode(data)

    async def get_map(self, language: str = "en") -> Map:
        """|coro|

        Returns information about the current Battle Royale map.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        :class:`Map`
        """
        data = await self.http.api_request(
            url='/v1/map',
            params={
                "language": language
            }
        )
        return Map(data)

    async def get_news(self, language: str = "en") -> News:
        """|coro|

        Get the current news posts.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        :class:`News`
        """
        data = await self.http.api_request(
            url='/v2/news/br',
            params={
                "language": language
            }
        )
        return News(data)

    async def get_playlists(self, language: str = "en") -> list[Playlist]:
        """|coro|

        Get all playlists currently in the game (old in-active playlists
        will not appear)

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        list[:class:`Playlist`]:
        """
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
        """|coro|

        Get information about a specific playlist by playlist id
        (old in-active playlists will not be searchable appear)

        Parameters
        ----------
        playlist_id: :class:`str`
            The playlist id to search for.
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        :class:`Playlist`
        """
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
        """|coro|

        Gets Battle Royale stats for the provided username on the provided
        platform.

        Parameters
        ----------
        name: :class:`str`
            The username to search for.
        account_type: Optional[:class:`AccountType`]
            The platform to search the provided name on.
        time_window: Optional[:class:`StatsTimeWindow`]
            Stats time window to fetch (lifetime or seasonal).
        image: Optional[:class:`StatsImage`]
            Which input to create the image for, if not provided an image
            won't be generated.

        Returns
        -------
        :class:`Stats`
        """
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
        """|coro|

        Gets Battle Royale stats for the provided account id.

        Parameters
        ----------
        account_id: :class:`str`
            The Epic account id to fetch stats for.
        time_window: Optional[:class:`StatsTimeWindow`]
            Stats time window to fetch (lifetime or seasonal).
        image: Optional[:class:`StatsImage`]
            Which input to create the image for, if not provided an image
            won't be generated.

        Returns
        -------
        :class:`Stats`
        """
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
        """|coro|

        Gets information about all banners.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        list[:class:`Banners`]:
        """
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
        """|coro|

        Gets information about all banner colours.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        list[:class:`BannerColor`]:
        """
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
        """|coro|

        Gets the current Battle Royale shop.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Returns
        -------
        :class:`Shop`
        """
        data = await self.http.api_request(
            url=f'/v2/shop',
            params={
                "language": language
            }
        )
        return Shop(data)