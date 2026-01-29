import datetime

from .cosmetics import (
    BRCosmetic,
    TrackCosmetic,
    InstrumentCosmetic,
    CarCosmetic,
    LegoKitCosmetic
)


class ShopBundle:
    def __init__(self, data: dict) -> None:
        self.name = data.get('name')
        self.info = data.get('info')
        self.image = data.get('image')


class ShopBanner:
    def __init__(self, data: dict) -> None:
        self.value = data.get('value')
        self.intensity = data.get('intensity')
        self.backend_value = data.get('backendValue')


class OfferTag:
    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.text = data.get('text')


class Layout:
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
    def __init__(self, data: dict) -> None:
        self.color_1: str = data.get('color1')
        self.color_2: str = data.get('color2')
        self.color_3: str = data.get('color3')
        self.text_background_color: str = data.get('textBackgroundColor')


class MaterialInstances:
    def __init__(self, data: dict) -> None:
        self.id: str = data.get('id')
        self.primary_mode: str = data.get('primaryMode')
        self.product_tag: str = data.get('productTag')
        self.images: dict = data.get('Images')
        self.colors: dict = data.get('Colors')
        self.scalings: dict = data.get('Scalings')
        self.flags: dict = data.get('Flags')


class RenderImages:
    def __init__(self, data: dict) -> None:
        self.product_tag: str = data.get('productTag')
        self.file_name: str = data.get('fileName')
        self.image: str = data.get('image')


class NewDisplayAsset:
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

