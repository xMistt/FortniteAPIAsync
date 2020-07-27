from .enums import *
from .exceptions import *

import datetime

from typing import Optional, List


class BRCosmetic:
    """Represents a Fortnite cosmetic.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    id: :class:`str`:
        The ID of the cosmetic.
    name: :class:`str`:
        The name of the cosmetic.
    type: :class:`dict`:
        Dictionary containing information on cosmetic type.
    rarity: :class:`dict`:
        Dictionary containing information on cosmetic rarity.
    series: :class:`dict`:
        Dictionary containing information on cosmetic series.
    set: :class:`dict`:
        Dictionary containing information on cosmetic set.
    introduction: :class`dict`:
        Dictionary containing information on cosmetic introduction.
    images: :class`dict`:
        Dictionary containing the images of the cosmetic.
    variants: :class`dict`:
        Dictionary containing information on cosmetic variants.
    gameplay_tags: :class`list`:
        List of the cosmetics gameplay tags.
    showcase_video: :class`str`:
        Represents a YouTube video id of a video showcasing the cosmetic.
    display_asset_path: :class`str`:
        File path of the display asset.
    definition_path: :class`str`:
        File path of the cosmetic definition
    path: :class`str`:
        File path of cosmetic.
    added: :class`datetime.datetime`:
        Datetime object which represents when the cosmetic was added to the API.
    shop_history: :class`list`:
        List of datetime objects which represent a shop release.

    """

    def __init__(self, data: dict) -> None:
        self.raw = data

        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.rarity = data.get('rarity')
        self.series = data.get('series')
        self.set = data.get('set')
        self.introduction = data.get('introduction')
        self.images = data.get('images')
        self.variants = data.get('variants')
        self.gameplay_tags = data.get('gameplayTags')
        self.showcase_video = data.get('showcaseVideo')
        self.display_asset_path = data.get('displayAssetPath')
        self.definition_path = data.get('definitionPath')
        self.path = data.get('path')
        self.added = datetime.datetime.strptime(data.get('added'), "%Y-%m-%dT%H:%M:%SZ")
        self.shop_history = [datetime.datetime.strptime(
            date, "%Y-%m-%dT%H:%M:%SZ"
        ) for date in data.get('shopHistory')] if data.get('shopHistory') is not None else None


class Cosmetics:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_cosmetic(self, **params: dict) -> BRCosmetic:
        """|coro|

        Fetches first cosmetic matching parameters. All parameters are optional but at least 1 is required.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        searchLanguage: Optional[:class:`str`]
            Sets the search language.
        matchMethod: Optional[:class:`str`]
            Sets the match method for strings (full/contains/starts/ends).
        id: Optional[:class:`str`]
            Sets the id.
        name: Optional[:class:`str`]
            Sets the name.
        description: Optional[:class:`str`]
            Sets the description.
        type: Optional[:class:`str`]
            Sets the type.
        displayType: Optional[:class:`str`]
            Sets the display type.
        backendType: Optional[:class:`str`]
            Sets the backend type.
        rarity: Optional[:class:`str`]
            Sets the rarity.
        displayRarity: Optional[:class:`str`]
            Sets the display rarity.
        backendRarity: Optional[:class:`str`]
            Sets the backend rarity.
        hasSeries: Optional[:class:`bool`]
            Sets whether there is a series.
        series: Optional[:class:`str`]
            Sets the series.
        backendSeries: Optional[:class:`str`]
            Sets the backend series.
        hasSet: Optional[:class:`bool`]
            Sets whether there is a set.
        set: Optional[:class:`str`]
            Sets the set.
        setText: Optional[:class:`str`]
            Sets the set text.
        backendSet: Optional[:class:`str`]
            Sets the backend set.
        hasIntroduction: Optional[:class:`bool`]
            Sets whether there is an introduction.
        introductionChapter: Optional[:class:`str`]
            Sets the introduction chapter.
        introductionSeason: Optional[:class:`str`]
            Sets the introduction season.
        hasFeaturedImage: Optional[:class:`bool`]
            Sets whether there is a featured image.
        hasVariants: Optional[:class:`bool`]
            Sets whether there are variants.
        hasGameplayTags: Optional[:class:`bool`]
            Sets whether there are gameplay tags.
        gameplayTag: Optional[:class:`str`]
            Sets the gameplay tag.
        added: Optional[:class:`int`]
            Sets the added date.
        addedSince: Optional[:class:`int`]
            Sets teh date since it was added.
        unseenFor: Optional[:class:`int`]
            Sets for how long its unseen.
        lastAppearance: Optional[:class:`int`]
            Sets the last appearance date.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.

        """

        if not params:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.http.request(
            method="GET",
            url="/v2/cosmetics/br/search",
            params=params
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] == 404:
            raise NotFound(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400, 404):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return BRCosmetic(data['data'])

    async def get_cosmetics(self, **params: dict) -> List[BRCosmetic]:
        """|coro|

        Fetches all cosmetics matching parameters. All parameters are optional but at least 1 is required.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        searchLanguage: Optional[:class:`str`]
            Sets the search language.
        matchMethod: Optional[:class:`str`]
            Sets the match method for strings (full/contains/starts/ends).
        id: Optional[:class:`str`]
            Sets the id.
        name: Optional[:class:`str`]
            Sets the name.
        description: Optional[:class:`str`]
            Sets the description.
        type: Optional[:class:`str`]
            Sets the type.
        displayType: Optional[:class:`str`]
            Sets the display type.
        backendType: Optional[:class:`str`]
            Sets the backend type.
        rarity: Optional[:class:`str`]
            Sets the rarity.
        displayRarity: Optional[:class:`str`]
            Sets the display rarity.
        backendRarity: Optional[:class:`str`]
            Sets the backend rarity.
        hasSeries: Optional[:class:`bool`]
            Sets whether there is a series.
        series: Optional[:class:`str`]
            Sets the series.
        backendSeries: Optional[:class:`str`]
            Sets the backend series.
        hasSet: Optional[:class:`bool`]
            Sets whether there is a set.
        set: Optional[:class:`str`]
            Sets the set.
        setText: Optional[:class:`str`]
            Sets the set text.
        backendSet: Optional[:class:`str`]
            Sets the backend set.
        hasIntroduction: Optional[:class:`bool`]
            Sets whether there is an introduction.
        introductionChapter: Optional[:class:`str`]
            Sets the introduction chapter.
        introductionSeason: Optional[:class:`str`]
            Sets the introduction season.
        hasFeaturedImage: Optional[:class:`bool`]
            Sets whether there is a featured image.
        hasVariants: Optional[:class:`bool`]
            Sets whether there are variants.
        hasGameplayTags: Optional[:class:`bool`]
            Sets whether there are gameplay tags.
        gameplayTag: Optional[:class:`str`]
            Sets the gameplay tag.
        added: Optional[:class:`int`]
            Sets the added date.
        addedSince: Optional[:class:`int`]
            Sets teh date since it was added.
        unseenFor: Optional[:class:`int`]
            Sets for how long its unseen.
        lastAppearance: Optional[:class:`int`]
            Sets the last appearance date.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic object containing information of the cosmetics.

        """

        if not params:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.http.request(
            method="GET",
            url="/v2/cosmetics/br/search/all",
            params=params
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] == 404:
            raise NotFound(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400, 404):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data['data']]

    async def search_cosmetic_ids(self, fortnite_ids: str = None, language: str = 'en') -> BRCosmetic:
        """|coro|

        Fetches all cosmetics from id/s.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        fortnite_ids: Optional[:class:`str`]
            Sets the cosmetic id (can be multiple).

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.

        """

        if not fortnite_ids:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.http.request(
            method="GET",
            url="/v2/cosmetics/br/search/ids",
            params={
                "language": language,
                "id": fortnite_ids
            }
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] == 404:
            raise NotFound(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400, 404):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data['data']]

    async def get_all_cosmetics(self, language: str = 'en') -> List[BRCosmetic]:
        """|coro|

        Fetches all cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Raises
        ------
        InvalidParameters
            If the parameters are invalid.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic object containing information of the cosmetics.

        """

        data = await self.http.request(
            method="GET",
            url="/v2/cosmetics/br/",
            params={
                "language": language
            }
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data['data']]

    async def get_new_cosmetics(self, language: str = 'en') -> List[BRCosmetic]:
        """|coro|

        Fetches all new cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.

        Raises
        ------
        InvalidParameters
            If the parameters are invalid.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic object containing information of the cosmetics.

        """

        data = await self.http.request(
            method="GET",
            url="/v2/cosmetics/br/new",
            params={
                "language": language
            }
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data['data']['items']]

    async def get_cosmetic_from_id(self, fortnite_id: str = None, language: str = 'en') -> BRCosmetic:
        """|coro|

        Fetches cosmetic from id.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        fortnite_id: Optional[:class:`str`]
            Sets the cosmetic id (can be multiple).

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameters are provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.

        """

        if not fortnite_id:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.http.request(
            method="GET",
            url=f"/v2/cosmetics/br/{fortnite_id}",
            params={
                "language": language
            }
        )

        if data['status'] == 400:
            raise InvalidParameters(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] == 404:
            raise NotFound(f"{data['error'][0].upper()}{data['error'][1:]}.")
        elif data['status'] not in (200, 400, 404):
            raise UnknownHTTPException(f"{data['error'][0].upper()}{data['error'][1:]}.")

        return BRCosmetic(data['data'])
