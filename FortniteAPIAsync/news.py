import datetime


class News:
    def __init__(self, data: dict) -> None:
        self.hash = data.get('hash')
        self.image = data.get('image')
        self.updated = datetime.datetime.fromisoformat(
            data.get('date').replace('Z', '+00:00')
        )

        self.posts = [NewsPost(raw_post) for raw_post in data.get('motds', [])]


class NewsPost:
    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.title = data.get('title')
        self.tab_title = data.get('tabTitle')
        self.body = data.get('body')
        self.image = data.get('image')
        self.tile_image = data.get('tileImage')
        self.sorting_priority = data.get('sortingPriority')
        self.hidden = data.get('hidden')