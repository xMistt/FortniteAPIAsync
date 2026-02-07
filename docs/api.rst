.. currentmodule:: FortniteAPIAsync

API Reference
=============


APIClient
~~~~~~~~~~~

.. attributetable:: APIClient

.. autoclass:: APIClient()
    :members:


Cosmetics
~~~~~~~~~~~

.. attribute:: APIClient.cosmetics

    Provides access to cosmetic-related API endpoints.

    .. autoclass:: Cosmetics()
        :members:


Enumerations
------------

.. class:: AccountType

    An enumeration for supported account types.

    .. attribute:: EPIC

        Epic Games account.
    .. attribute:: PLAYSTATION

        PlayStation Network account.
    .. attribute:: XBOX

        Xbox Live account.

.. class:: StatsTimeWindow

    An enumeration for available statistics time windows.

    .. attribute:: SEASON

        Statistics scoped to the current season.
    .. attribute:: LIFETIME

        Statistics scoped to the entire account lifetime.

.. class:: StatsImage

    An enumeration for available statistics input images.

    .. attribute:: ALL

        Statistics aggregated across all input types.
    .. attribute:: KEYBOARD_AND_MOUSE

        Statistics for keyboard and mouse input.
    .. attribute:: CONTROLLER

        Statistics for controller input.
    .. attribute:: TOUCH

        Statistics for touch input.
    .. attribute:: NONE

        No input image applied.

.. class:: AESKeyFormat

    An enumeration for AES key output formats.

    .. attribute:: HEX

        AES key encoded in hexadecimal format.
    .. attribute:: BASE64

        AES key encoded in base64 format.

.. class:: ResponseFlags

    An enumeration of flags used to opt-in to additional API response properties.

    These flags will be automatically combined using bitwise operations.

    .. attribute:: NONE

        Do not include any optional response properties.
    .. attribute:: INCLUDE_PATHS

        Include file path related properties in the response.
    .. attribute:: INCLUDE_GAMEPLAY_TAGS

        Include gameplay tags in the response.
    .. attribute:: INCLUDE_SHOP_HISTORY

        Include shop history information in the response.



Data Models
---------------


BRCosmetic
~~~~~~~~~~

.. attributetable:: BRCosmetic

.. autoclass:: BRCosmetic()
    :members:


CosmeticType
~~~~~~~~~~~~

.. attributetable:: CosmeticType

.. autoclass:: CosmeticType()
    :members:


Rarity
~~~~~~

.. attributetable:: Rarity

.. autoclass:: Rarity()
    :members:


Series
~~~~~~

.. attributetable:: Series

.. autoclass:: Series()
    :members:


Introduction
~~~~~~~~~~~~

.. attributetable:: Introduction

.. autoclass:: Introduction()
    :members:


Set
~~~

.. attributetable:: Set

.. autoclass:: Set()
    :members:


TrackDifficulty
~~~~~~~~~~~~~~~

.. attributetable:: TrackDifficulty

.. autoclass:: TrackDifficulty()
    :members:


TrackCosmetic
~~~~~~~~~~~~~

.. attributetable:: TrackCosmetic

.. autoclass:: TrackCosmetic()
    :members:


InstrumentCosmetic
~~~~~~~~~~~~~~~~~~

.. attributetable:: InstrumentCosmetic

.. autoclass:: InstrumentCosmetic()
    :members:


CarCosmetic
~~~~~~~~~~~

.. attributetable:: CarCosmetic

.. autoclass:: CarCosmetic()
    :members:


LegoCosmetic
~~~~~~~~~~~~

.. attributetable:: LegoCosmetic

.. autoclass:: LegoCosmetic()
    :members:


LegoKitCosmetic
~~~~~~~~~~~~~~~

.. attributetable:: LegoKitCosmetic

.. autoclass:: LegoKitCosmetic()
    :members:


BeanCosmetic
~~~~~~~~~~~~

.. attributetable:: BeanCosmetic

.. autoclass:: BeanCosmetic()
    :members:


AllCosmetics
~~~~~~~~~~~~

.. attributetable:: AllCosmetics

.. autoclass:: AllCosmetics()
    :members:


NewCosmeticsType
~~~~~~~~~~~~~~~~

.. attributetable:: NewCosmeticsType

.. autoclass:: NewCosmeticsType()
    :members:


NewCosmetics
~~~~~~~~~~~~

.. attributetable:: NewCosmetics

.. autoclass:: NewCosmetics()
    :members:


AESKeys
~~~~~~~

.. attributetable:: AESKeys

.. autoclass:: AESKeys()
    :members:


DynamicAESKey
~~~~~~~~~~~~~

.. attributetable:: DynamicAESKey

.. autoclass:: DynamicAESKey()
    :members:


Banner
~~~~~~

.. attributetable:: Banner

.. autoclass:: Banner()
    :members:


BannerColor
~~~~~~~~~~~

.. attributetable:: BannerColor

.. autoclass:: BannerColor()
    :members:


CreatorCode
~~~~~~~~~~~

.. attributetable:: CreatorCode

.. autoclass:: CreatorCode()
    :members:


Map
~~~

.. attributetable:: Map

.. autoclass:: Map()
    :members:


POI
~~~

.. attributetable:: POI

.. autoclass:: POI()
    :members:


News
~~~~

.. attributetable:: News

.. autoclass:: News()
    :members:


NewsPost
~~~~~~~~

.. attributetable:: NewsPost

.. autoclass:: NewsPost()
    :members:


Playlist
~~~~~~~~

.. attributetable:: Playlist

.. autoclass:: Playlist()
    :members:


GamemodeStats
~~~~~~~~~~~~~

.. attributetable:: GamemodeStats

.. autoclass:: GamemodeStats()
    :members:


Stats
~~~~~

.. attributetable:: Stats

.. autoclass:: Stats()
    :members:


ShopBundle
~~~~~~~~~~

.. attributetable:: ShopBundle

.. autoclass:: ShopBundle()
    :members:


ShopBanner
~~~~~~~~~~

.. attributetable:: ShopBanner

.. autoclass:: ShopBanner()
    :members:


OfferTag
~~~~~~~~

.. attributetable:: OfferTag

.. autoclass:: OfferTag()
    :members:


Layout
~~~~~~

.. attributetable:: Layout

.. autoclass:: Layout()
    :members:


Colors
~~~~~~

.. attributetable:: Colors

.. autoclass:: Colors()
    :members:


MaterialInstances
~~~~~~~~~~~~~~~~~

.. attributetable:: MaterialInstances

.. autoclass:: MaterialInstances()
    :members:


RenderImages
~~~~~~~~~~~~

.. attributetable:: RenderImages

.. autoclass:: RenderImages()
    :members:


NewDisplayAsset
~~~~~~~~~~~~~~~

.. attributetable:: NewDisplayAsset

.. autoclass:: NewDisplayAsset()
    :members:


ShopEntry
~~~~~~~~~

.. attributetable:: ShopEntry

.. autoclass:: ShopEntry()
    :members:


Shop
~~~~

.. attributetable:: Shop

.. autoclass:: Shop()
    :members:


Exceptions
----------

.. autoexception:: FortniteAPIException

.. autoexception:: InvalidParameters

.. autoexception:: NotFound

.. autoexception:: Private

.. autoexception:: UnknownHTTPException
