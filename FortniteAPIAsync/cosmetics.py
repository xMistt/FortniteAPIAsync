from .enums import *
from .exceptions import *
from .utils import combine_flags

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
        self.description = data.get('description')
        self.exclusive_description = data.get('exclusiveDescription')
        self.unlock_requirements = data.get('unlockRequirements')
        self.custom_exclusive_callout = data.get('customExclusiveCallout')

        self.type = CosmeticType(data.get('type', {}))
        self.rarity = Rarity(data.get('rarity', {}))
        self.series = Series(data.get('series', {}))
        self.set = Set(data.get('set', {}))
        self.introduction = Introduction(data.get('introduction', {}))
        self.images = data.get('images')
        self.variants = data.get('variants')

        self.built_in_emote_ids = data.get('builtInEmoteIds')
        self.search_tags = data.get('searchTags')
        self.gameplay_tags = data.get('gameplayTags')
        self.meta_tags = data.get('metaTags')
        self.showcase_video = data.get('showcaseVideo')
        self.dynamic_pak_id = data.get('dynamicPakId')
        self.item_preview_hero_path = data.get('itemPreviewHeroPath')
        self.display_asset_path = data.get('displayAssetPath')
        self.definition_path = data.get('definitionPath')
        self.path = data.get('path')
        self.added = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )
        self.shop_history = [
            datetime.datetime.fromisoformat(
                date.replace('Z', '+00:00')
            ) for date in data.get('shopHistory', [])
        ]


class CosmeticType:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.value: str = data.get('value')
        self.display_value: str = data.get('displayValue')
        self.backend_value: str = data.get('backendValue')


class Rarity:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.value: str = data.get('value')
        self.display_value: str = data.get('displayValue')
        self.backend_value: str = data.get('backendValue')


class Series:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.value: str = data.get('value')
        self.image: str = data.get('image')
        self.colors: list[str] = data.get('colors')
        self.backend_value: str = data.get('backendValue')


class Introduction:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.chapter: str = data.get('chapter')
        self.season: str = data.get('season')
        self.text: str = data.get('text')
        self.backend_value: str = data.get('backendValue')


class Set:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.value: str = data.get('value')
        self.text: str = data.get('text')
        self.backend_value: str = data.get('backendValue')


class TrackDifficulty:
    def __init__(self, data: dict) -> None:
        self.vocals: int = data.get('vocals')
        self.guitar: int = data.get('guitar')
        self.bass: int = data.get('bass')
        self.plastic_bass: int = data.get('plasticBass')
        self.drums: int = data.get('drums')
        self.plastic_drums: int = data.get('plasticDrums')


class TrackCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.id: str = data.get('id')
        self.dev_name: str = data.get('devName')
        self.title: str = data.get('title')
        self.artist: str = data.get('artist')
        self.album: str = data.get('album')
        self.release_year: int = data.get('releaseYear')
        self.bpm: int = data.get('bpm')
        self.duration: int = data.get('duration')
        self.difficulty: TrackDifficulty = TrackDifficulty(
            data.get('difficulty', {})
        )
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.genres: list[str] = data.get('genres')
        self.album_art: str = data.get('albumArt')

        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )
        self.shop_history: list[datetime.datetime] = [
            datetime.datetime.fromisoformat(
                date.replace('Z', '+00:00')
            ) for date in data.get('shopHistory', [])
        ]


class InstrumentCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.type: CosmeticType = CosmeticType(data.get('type'))
        self.rarity: Rarity = Rarity(data.get('rarity'))
        self.small_image: str = data.get('images', {}).get('small')
        self.large_image: str = data.get('images', {}).get('large')
        self.series: Series = Series(data.get('series', {}))
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.path: str = data.get('path')
        self.showcase_video: str = data.get('showcaseVideo')
        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )
        self.shop_history: list[datetime.datetime] = [
            datetime.datetime.fromisoformat(
                date.replace('Z', '+00:00')
            ) for date in data.get('shopHistory', [])
        ]


class CarCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.id: str = data.get('id')
        self.vehicle_id: str = data.get('vehicleId')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.type: CosmeticType = CosmeticType(data.get('type', {}))
        self.rarity: Rarity = Rarity(data.get('rarity', {}))
        self.small_image: str = data.get('image', {}).get('small')
        self.large_image: str = data.get('image', {}).get('large')
        self.series: Series = Series(data.get('series', {}))
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.path: str = data.get('path')
        self.showcase_video: str = data.get('showcaseVideo')

        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )
        self.shop_history: list[datetime.datetime] = [
            datetime.datetime.fromisoformat(
                date.replace('Z', '+00:00')
            ) for date in data.get('shopHistory', [])
        ]


class LegoCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.cosmetic_id: str = data.get('cosmeticId')
        self.sound_library_tags: list[str] = data.get('soundLibraryTags')
        self.small_image: str = data.get('images', {}).get('small')
        self.large_image: str = data.get('images', {}).get('large')
        self.wide_image:  str = data.get('images', {}).get('wide')
        self.path: str = data.get('path')
        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )


class LegoKitCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.type: CosmeticType = CosmeticType(data.get('type'))
        self.value: str = data.get('value')
        self.display_value: str = data.get('displayValue')
        self.backend_value: str = data.get('backendValue')
        self.series: Series = Series(data.get('series', {}))
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.small_image: str = data.get('images', {}).get('small')
        self.large_image: str = data.get('images', {}).get('large')
        self.wide_image: str = data.get('images', {}).get('wide')
        self.path: str = data.get('path')
        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )
        self.shop_history: list[datetime.datetime] = [
            datetime.datetime.fromisoformat(
                date.replace('Z', '+00:00')
            ) for date in data.get('shopHistory', [])
        ]


class BeanCosmetic:
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.cosmetic_id: str = data.get('cosmeticId')
        self.name: str = data.get('name')
        self.gender: str = data.get('gender')
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.small_image: str = data.get('images', {}).get('small')
        self.large_image: str = data.get('images', {}).get('large')
        self.path: str = data.get('path')
        self.added: datetime.datetime = datetime.datetime.fromisoformat(
            data['added'].replace('Z', '+00:00')
        )


class AllCosmetics:
    def __init__(self, data: dict) -> None:
        self.br: list[BRCosmetic] = [
            BRCosmetic(cosmetic_data)
            for cosmetic_data in data.get('br', [])
        ]
        self.tracks: list[TrackCosmetic] = [
            TrackCosmetic(cosmetic_data)
            for cosmetic_data in data.get('tracks', [])
        ]
        self.instruments: list[InstrumentCosmetic] = [
            InstrumentCosmetic(cosmetic_data)
            for cosmetic_data in data.get('instruments', [])
        ]
        self.cars: list[CarCosmetic] = [
            CarCosmetic(cosmetic_data)
            for cosmetic_data in data.get('cars', [])
        ]
        self.lego: list[LegoCosmetic] = [
            LegoCosmetic(cosmetic_data)
            for cosmetic_data in data.get('lego', [])
        ]
        self.lego_kits: list[LegoKitCosmetic] = [
            LegoKitCosmetic(cosmetic_data)
            for cosmetic_data in data.get('legoKits', [])
        ]
        self.beans: list[BeanCosmetic] = [
            BeanCosmetic(cosmetic_data)
            for cosmetic_data in data.get('beans', [])
        ]

class NewCosmeticsType:
    def __init__(self,
                 hash: str,
                 last_addition: str,
                 items: list,
                 type: 'Type'
                 ) -> None:
        self.hash = hash
        self.last_addition: datetime.datetime = datetime.datetime.fromisoformat(  # noqa
            last_addition.replace('Z', '+00:00')
        )
        self.items: list[type] = [
            type(cosmetic_data)
            for cosmetic_data in items
        ]


class NewCosmetics:
    def __init__(self, data: dict) -> None:
        self.date: datetime.datetime = datetime.datetime.fromisoformat(
            data.get('date', '1970-01-01T00:00:00Z').replace('Z', '+00:00')
        )

        self.hash = data.get('hashes', {}).get('all')
        self.last_addition = data.get('lastAdditions', {}).get('all')

        self.build = data.get('build')
        self.previous_build = data.get('previousBuild')

        self.br = NewCosmeticsType(
            hash=data.get('hashes', {}).get('br'),
            last_addition=data.get('lastAdditions').get(
                'br', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('br', []),
            type=BRCosmetic
        )
        self.tracks = NewCosmeticsType(
            hash=data.get('hashes', {}).get('tracks'),
            last_addition=data.get('lastAdditions').get(
                'tracks', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('tracks', []),
            type=TrackCosmetic
        )
        self.instruments = NewCosmeticsType(
            hash=data.get('hashes', {}).get('instruments'),
            last_addition=data.get('lastAdditions').get(
                'instruments', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('instruments', []),
            type=InstrumentCosmetic
        )
        self.cars = NewCosmeticsType(
            hash=data.get('hashes', {}).get('cars'),
            last_addition=data.get('lastAdditions').get(
                'cars', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('cars', []),
            type=CarCosmetic
        )
        self.lego = NewCosmeticsType(
            hash=data.get('hashes', {}).get('lego'),
            last_addition=data.get('lastAdditions').get(
                'lego', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('lego', []),
            type=LegoCosmetic
        )
        self.lego_kits = NewCosmeticsType(
            hash=data.get('hashes', {}).get('legoKits'),
            last_addition=data.get('lastAdditions').get(
                'legoKits', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('legoKits', []),
            type=LegoCosmetic
        )
        self.beans = NewCosmeticsType(
            hash=data.get('hashes', {}).get('beans'),
            last_addition=data.get('lastAdditions').get(
                'beans', '1970-01-01T00:00:00Z'
            ),
            items=data.get('items', {}).get('beans', []),
            type=BeanCosmetic
        )


class Cosmetics:
    def __init__(self, client: 'APIClient') -> None:
        self.client = client

    async def get_cosmetic(self,
                           flags: list[ResponseFlags] = [ResponseFlags.NONE],
                           **params: dict
                           ) -> BRCosmetic:
        """|coro|

        Fetches first cosmetic matching parameters.
        All parameters are optional but at least 1 is required.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.
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
        backendIntroduction: Optional[:class:`int`]
            Sets the introduction backend value.
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
        hasMetaTags: Optional[:class:`bool`]
            Sets whether there are meta tags.
        metaTag: Optional[:class:`str`]
            Sets the meta tag.
        hasDynamicPakId: Optional[:class:`bool`]
            Sets whether a dynamic pak id is set.
        dynamicPakId: Optional[:class:`str`]
            Sets the dynamic pak id.
        added: Optional[:class:`int`]
            Sets the added date.
        addedSince: Optional[:class:`int`]
            Sets the date since it was added.
        unseenFor: Optional[:class:`int`]
            Sets for how long its unseen.
        lastAppearance: Optional[:class:`int`]
            Sets the last appearance date.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameter is provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.
        """

        if not params:
            raise InvalidParameters(
                'No search parameters provided. At least 1 is required.'
            )

        params["responseFlags"] = int(combine_flags(flags))
        data = await self.client.http.api_request(
            url="/v2/cosmetics/br/search",
            params=params
        )
        return BRCosmetic(data)

    async def get_cosmetics(self,
                            flags: list[ResponseFlags] = [ResponseFlags.NONE],
                            **params: dict
                            ) -> list[BRCosmetic]:
        """|coro|

        Fetches all cosmetics matching parameters.
        All parameters are optional but at least 1 is required.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.
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
        backendIntroduction: Optional[:class:`int`]
            Sets the introduction backend value.
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
        hasMetaTags: Optional[:class:`bool`]
            Sets whether there are meta tags.
        metaTag: Optional[:class:`str`]
            Sets the meta tag.
        hasDynamicPakId: Optional[:class:`bool`]
            Sets whether a dynamic pak id is set.
        dynamicPakId: Optional[:class:`str`]
            Sets the dynamic pak id.
        added: Optional[:class:`int`]
            Sets the added date.
        addedSince: Optional[:class:`int`]
            Sets the date since it was added.
        unseenFor: Optional[:class:`int`]
            Sets for how long its unseen.
        lastAppearance: Optional[:class:`int`]
            Sets the last appearance date.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameter is provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic object containing information of the cosmetics.

        """

        if not params:
            raise InvalidParameters(
                'No search parameters provided. At least 1 is required.'
            )

        params["responseFlags"] = int(combine_flags(flags))
        data = await self.client.http.api_request(
            url="/v2/cosmetics/br/search/all",
            params=params
        )

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data]

    async def search_cosmetic_ids(
        self,
        fortnite_ids: str = None,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[BRCosmetic]:
        """|coro|

        Fetches all cosmetics from id/s.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        fortnite_ids: Optional[:class:`str`]
            Sets the cosmetic id (can be multiple).
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameter is provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.

        """

        if not fortnite_ids:
            raise InvalidParameters(
                'No search parameters provided. At least 1 is required.'
            )

        data = await self.client.http.api_request(
            url="/v2/cosmetics/br/search/ids",
            params={
                "language": language,
                "id": fortnite_ids,
                "responseFlags": combine_flags(flags)
            }
        )

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_br_cosmetics(self,
                                   language: str = 'en',
                                   flags: list[ResponseFlags] = [ResponseFlags.NONE]
                                   ) -> List[BRCosmetic]:
        """|coro|

        Fetches all cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        List[:class:`BRCosmetic`]:
            List of BRCosmetic object containing information of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/br/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [BRCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_new_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> NewCosmetics:
        """|coro|

        Fetches all new cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        NewCosmetics:
            NewCosmetics object containing information of each cosmetic types
            new items.
        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/new",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return NewCosmetics(data)

    async def get_cosmetic_from_id(
            self,
            fortnite_id: str = None,
            language: str = 'en',
            flags: list[ResponseFlags] = [ResponseFlags.NONE],
    ) -> BRCosmetic:
        """|coro|

        Fetches cosmetic from id.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.
        fortnite_id: Optional[:class:`str`]
            Sets the cosmetic id (can be multiple).

        Raises
        ------
        InvalidParameters
            If none or more than 1 parameter is provided.
        NotFound
            If no cosmetics are found matching parameters.

        Returns
        -------
        :class:`BRCosmetic`:
            BRCosmetic object containing information of the cosmetic.

        """

        if not fortnite_id:
            raise InvalidParameters('No search parameters provided. At least 1 is required.')

        data = await self.client.http.api_request(
            url=f"/v2/cosmetics/br/{fortnite_id}",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return BRCosmetic(data)

    async def get_all_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> AllCosmetics:
        """|coro|

        Fetches all cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        :class:`AllCosmetics`:
            AllCosmetics object containing all types cosmetics.
        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return AllCosmetics(data)

    async def get_all_track_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> List[TrackCosmetic]:
        """|coro|

        Fetches all track cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        List[:class:`TrackCosmetic`]:
            List of TrackCosmetic object containing information
            of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/tracks/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [TrackCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_instrument_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[InstrumentCosmetic]:
        """|coro|

        Fetches all instrument cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        list[:class:`InstrumentCosmetic`]:
            List of InstrumentCosmetic object containing information
            of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/instruments/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [InstrumentCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_car_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[CarCosmetic]:
        """|coro|

        Fetches all car cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        list[:class:`CarCosmetic`]:
            List of CarCosmetic object containing information
            of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/cars/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [CarCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_lego_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[LegoCosmetic]:
        """|coro|

        Fetches all lego cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        list[:class:`LegoCosmetic`]:
            List of LegoCosmetic object containing information
            of the cosmetics.
        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/lego/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [LegoCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_lego_kit_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[LegoKitCosmetic]:
        """|coro|

        Fetches all lego kit cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        list[:class:`LegoKitCosmetic`]:
            List of LegoKitCosmetic object containing information
            of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/lego/kits/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [LegoKitCosmetic(cosmetic_data) for cosmetic_data in data]

    async def get_all_bean_cosmetics(
        self,
        language: str = 'en',
        flags: list[ResponseFlags] = [ResponseFlags.NONE]
    ) -> list[BeanCosmetic]:
        """|coro|

        Fetches all bean cosmetics.

        Parameters
        ----------
        language: Optional[:class:`str`]
            Sets the output language.
        flags: Optional[:class:`list`[:class:`ResponseFlags`]]
            Opt-in for certain properties, defaults to `[ResponseFlags.NONE]`.

        Returns
        -------
        list[:class:`BeanCosmetic`]:
            List of BeanCosmetic object containing information
            of the cosmetics.

        """

        data = await self.client.http.api_request(
            url="/v2/cosmetics/beans/",
            params={
                "language": language,
                "responseFlags": combine_flags(flags)
            }
        )

        return [BeanCosmetic(cosmetic_data) for cosmetic_data in data]
