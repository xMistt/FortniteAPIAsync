from .cosmetics import CosmeticType, Rarity, Series, Introduction, Set

class Banner:
    """Represents a banner.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    id: :class:`str`
        The ID of the banner.
    dev_name: :class:`str`
        The developer name of the banner.
    name: :class:`str`
        The name of the banner.
    description: :class:`str`
        The description of the banner.
    category: :class:`str`
        The category of the banner.
    full_usage_rights: :class:`bool`
        Whether the banner has full usage rights.
    rarity: :class:`Rarity`
        Object containing information on banner rarity.
    series: :class:`Series`
        Object containing information on banner series.
    set: :class:`Set`
        Object containing information on banner set.
    introduction: :class:`Introduction`
        Object containing information on banner introduction.
    icon_image: :class:`str`
        The icon image of the banner.
    small_icon_image: :class:`str`
        The small icon image of the banner.
    gameplay_tags: :class:`list`[:class:`str`]
        List of the banner gameplay tags.
    path: :class:`str`
        File path of banner.
    """

    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.dev_name: str  = data.get('devName')
        self.name: str  = data.get('name')
        self.description: str  = data.get('description')
        self.category: str  = data.get('category')
        self.full_usage_rights: bool = data.get('fullUsageRights')
        self.rarity: Rarity = Rarity(data.get('rarity', {}))
        self.series: Series = Series(data.get('series', {}))
        self.set: Set = Set(data.get('set', {}))
        self.introduction: Introduction = Introduction(data.get('introduction', {}))
        self.icon_image: str  = data.get('images').get('icon')
        self.small_icon_image: str  = data.get('images').get('smallIcon')
        self.gameplay_tags: list[str] = data.get('gameplayTags')
        self.path: str  = data.get('path')


class BannerColor:
    """Represents a banner color.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    id: :class:`str`
        The ID of the banner color.
    color: :class:`str`
        The color value of the banner.
    category: :class:`str`
        The category of the banner color.
    sub_category_group: :class:`str`
        The sub-category group of the banner color.
    """

    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.color: str = data.get('color')
        self.category: str = data.get('category')
        self.sub_category_group: str = data.get('subCategoryGroup')