import datetime

from .cosmetics import (
    BRCosmetic,
    TrackCosmetic,
    InstrumentCosmetic,
    CarCosmetic,
    LegoKitCosmetic
)


class ShopBundle:
    """Represents a shop bundle.

    Attributes
    ----------
    name: :class:`str`
        The name of the bundle.
    info: :class:`str`
        Additional information about the bundle.
    image: :class:`str`
        The image associated with the bundle.
    """

    def __init__(self, data: dict) -> None:
        self.name = data.get('name')
        self.info = data.get('info')
        self.image = data.get('image')


class ShopBanner:
    """Represents a shop banner.

    Attributes
    ----------
    value: :class:`str`
        The banner value.
    intensity: :class:`str`
        The banner intensity.
    backend_value: :class:`str`
        The backend value of the banner.
    """

    def __init__(self, data: dict) -> None:
        self.value = data.get('value')
        self.intensity = data.get('intensity')
        self.backend_value = data.get('backendValue')


class OfferTag:
    """Represents an offer tag.

    Attributes
    ----------
    id: :class:`str`
        The ID of the offer tag.
    text: :class:`str`
        The text of the offer tag.
    """

    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.text = data.get('text')


class Layout:
    """Represents a shop layout.

    Attributes
    ----------
    id: :class:`str`
        The ID of the layout.
    name: :class:`str`
        The name of the layout.
    category: :class:`str`
        The category of the layout.
    index: :class:`int`
        The index of the layout.
    rank: :class:`int`
        The rank of the layout.
    show_ineligible_offers: :class:`bool`
        Whether ineligible offers are shown.
    background: :class:`str`
        The background of the layout.
    use_wide_preview: :class:`bool`
        Whether wide preview is used.
    display_type: :class:`str`
        The display type of the layout.
    texture_metadata: :class:`list`
        List of texture metadata.
    string_metadata: :class:`list`
        List of string metadata.
    text_metadata: :class:`list`
        List of text metadata.
    """

    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.name = data.get('name')
        self.category = data.get('category')
        self.index = data.get('index')
        self.rank = data.get('rank')
        self.show_ineligible_offers = data.get('showIneligibleOffers')
        self.background = data.get('background')
        self.use_wide_preview = data.get('useWidePreview')
        self.display_type = data.get('displayType')

        self.texture_metadata = data.get('textureMetadata', [])
        self.string_metadata = data.get('stringMetadata', [])
        self.text_metadata = data.get('textMetadata', [])


class Colors:
    """Represents colour configuration.

    Attributes
    ----------
    color_1: :class:`str`
        The primary colour.
    color_2: :class:`str`
        The secondary colour.
    color_3: :class:`str`
        The tertiary colour.
    text_background_color: :class:`str`
        The text background colour.
    """

    def __init__(self, data: dict) -> None:
        self.color_1: str = data.get('color1')
        self.color_2: str = data.get('color2')
        self.color_3: str = data.get('color3')
        self.text_background_color: str = data.get('textBackgroundColor')


class MaterialInstances:
    """Represents a material instance.

    Attributes
    ----------
    id: :class:`str`
        The ID of the material instance.
    primary_mode: :class:`str`
        The primary mode of the material instance.
    product_tag: :class:`str`
        The product tag associated with the material instance.
    images: :class:`dict`
        Image data for the material instance.
    colors: :class:`dict`
        Color data for the material instance.
    scalings: :class:`dict`
        Scaling data for the material instance.
    flags: :class:`dict`
        Flag data for the material instance.
    """

    def __init__(self, data: dict) -> None:
        self.id: str = data.get('id')
        self.primary_mode: str = data.get('primaryMode')
        self.product_tag: str = data.get('productTag')
        self.images: dict = data.get('Images')
        self.colors: dict = data.get('Colors')
        self.scalings: dict = data.get('Scalings')
        self.flags: dict = data.get('Flags')


class RenderImages:
    """Represents a render image.

    Attributes
    ----------
    product_tag: :class:`str`
        The product tag associated with the render image.
    file_name: :class:`str`
        The file name of the render image.
    image: :class:`str`
        The render image URL.
    """

    def __init__(self, data: dict) -> None:
        self.product_tag: str = data.get('productTag')
        self.file_name: str = data.get('fileName')
        self.image: str = data.get('image')


class NewDisplayAsset:
    """Represents a new display asset.

    Attributes
    ----------
    id: :class:`str`
        The ID of the display asset.
    cosmetic_id: :class:`str`
        The associated cosmetic ID.
    material_instances: :class:`list`[:class:`MaterialInstances`]
        List of material instances.
    render_images: :class:`list`[:class:`RenderImages`]
        List of render images.
    """

    def __init__(self, data: dict) -> None:
        self.id: str = data.get('id')
        self.cosmetic_id: str = data.get('cosmeticId')
        self.material_instances: list[MaterialInstances] = [
            MaterialInstances(raw_material_instance)
            for raw_material_instance in data.get('materialInstances', [])
        ]
        self.render_images: list[RenderImages] = [
            RenderImages(raw_render_images)
            for raw_render_images in data.get('renderImages', [])
        ]


class ShopEntry:
    """Represents a shop entry.

    Attributes
    ----------
    regular_price: :class:`int`
        The regular price of the offer.
    final_price: :class:`int`
        The final price of the offer.
    dev_name: :class:`str`
        The developer name of the offer.
    offer_id: :class:`str`
        The offer ID.
    in_date: :class:`datetime.datetime`
        Datetime when the offer becomes available.
    out_date: :class:`datetime.datetime`
        Datetime when the offer is removed.
    bundle: :class:`ShopBundle`
        Bundle information for the offer.
    banner: :class:`ShopBanner`
        Banner information for the offer.
    offer_tag: :class:`OfferTag`
        Offer tag associated with the entry.
    giftable: :class:`bool`
        Whether the offer is giftable.
    refundable: :class:`bool`
        Whether the offer is refundable.
    sort_priority: :class:`int`
        The sorting priority of the offer.
    layout_id: :class:`str`
        The layout ID of the offer.
    layout: :class:`Layout`
        Layout information for the offer.
    colors: :class:`Colors`
        Color configuration for the offer.
    tile_background_material: :class:`str`
        The tile background material.
    tile_size: :class:`str`
        The tile size.
    display_asset_path: :class:`str`
        The display asset path.
    new_display_asset_path: :class:`str`
        The new display asset path.
    new_display_asset: :class:`NewDisplayAsset`
        New display asset information.
    br_items: :class:`list`[:class:`BRCosmetic`]
        List of Battle Royale cosmetics included.
    tracks: :class:`list`[:class:`TrackCosmetic`]
        List of track cosmetics included.
    instruments: :class:`list`[:class:`InstrumentCosmetic`]
        List of instrument cosmetics included.
    cars: :class:`list`[:class:`CarCosmetic`]
        List of car cosmetics included.
    lego_kits: :class:`list`[:class:`LegoKitCosmetic`]
        List of LEGO kit cosmetics included.
    """

    def __init__(self, data: dict) -> None:
        self.regular_price = data.get('regularPrice')
        self.final_price = data.get('finalPrice')
        self.dev_name = data.get('devName')
        self.offer_id = data.get('offerId')

        self.in_date: datetime.datetime = datetime.datetime.fromisoformat(
            data.get('inDate', '1970-01-01T00:00:00Z').replace('Z', '+00:00')
        )
        self.out_date: datetime.datetime = datetime.datetime.fromisoformat(
            data.get('outDate', '1970-01-01T00:00:00Z').replace('Z', '+00:00')
        )

        self.bundle: ShopBundle = ShopBundle(data.get('bundle', {}))
        self.banner: ShopBanner = ShopBanner(data.get('banner', {}))
        self.offer_tag: OfferTag = OfferTag(data.get('offerTag', {}))

        self.giftable: bool = data.get('giftable')
        self.refundable: bool = data.get('refundable')
        self.sort_priority: int = data.get('sortPriority')
        self.layout_id: str = data.get('layoutId')
        self.layout: Layout = Layout(data.get('layout', {}))
        self.colors: Colors = Colors(data.get('colors', {}))

        self.tile_background_material: str = data.get('tileBackgroundMaterial')
        self.tile_size: str = data.get('tileSize')
        self.display_asset_path: str = data.get('displayAssetPath')
        self.new_display_asset_path: str = data.get('newDisplayAssetPath')

        self.new_display_asset: NewDisplayAsset = NewDisplayAsset(
            data.get('newDisplayAsset', {})
        )

        self.br_items:  list[BRCosmetic] = [
            BRCosmetic(cosmetic_data)
            for cosmetic_data in data.get('brItems', [])
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
        self.lego_kits: list[LegoKitCosmetic] = [
            LegoKitCosmetic(cosmetic_data)
            for cosmetic_data in data.get('legoKits', [])
        ]


class Shop:
    """Represents the Fortnite item shop.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    hash: :class:`str`
        Hash of the shop data used for change detection.
    date: :class:`datetime.datetime`
        Datetime when the shop data was generated.
    vbuck_icon: :class:`str`
        The V-Bucks icon image.
    entries: :class:`list`[:class:`ShopEntry`]
        List of shop entries.
    """

    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.hash: str = data.get('hash')
        self.date: datetime.datetime = datetime.datetime.fromisoformat(
            data.get('date', '1970-01-01T00:00:00Z').replace('Z', '+00:00')
        )
        self.vbuck_icon: str = data.get('vbuckIcon')
        self.entries = [
            ShopEntry(raw_entry) for raw_entry in data.get('entries', [])
        ]

