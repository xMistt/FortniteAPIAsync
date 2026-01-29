from .cosmetics import CosmeticType, Rarity, Series, Introduction, Set

class Banner:
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
    def __init__(self, data: dict) -> None:
        self.raw: dict = data

        self.id: str = data.get('id')
        self.color: str = data.get('color')
        self.category: str = data.get('category')
        self.sub_category_group: str = data.get('subCategoryGroup')