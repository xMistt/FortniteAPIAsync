import datetime


class News:
    """Represents Fortnite news.

    Attributes
    ----------
    hash: :class:`str`
        Hash of the news data used for change detection.
    image: :class:`str`
        An animated gif of the current news posts.
    updated: :class:`datetime.datetime`
        Datetime when the news was last updated.
    posts: :class:`list`[:class:`NewsPost`]
        List of news posts.
    """

    def __init__(self, data: dict) -> None:
        self.hash = data.get('hash')
        self.image = data.get('image')
        self.updated = datetime.datetime.fromisoformat(
            data.get('date').replace('Z', '+00:00')
        )

        self.posts = [NewsPost(raw_post) for raw_post in data.get('motds', [])]


class NewsPost:
    """Represents a news post.

    Attributes
    ----------
    id: :class:`str`
        The ID of the news post.
    title: :class:`str`
        The title of the news post.
    tab_title: :class:`str`
        The tab title of the news post.
    body: :class:`str`
        The body text of the news post.
    image: :class:`str`
        The image associated with the news post.
    tile_image: :class:`str`
        The tile image of the news post.
    sorting_priority: :class:`int`
        The sorting priority of the news post.
    hidden: :class:`bool`
        Whether the news post is hidden.
    """

    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.title = data.get('title')
        self.tab_title = data.get('tabTitle')
        self.body = data.get('body')
        self.image = data.get('image')
        self.tile_image = data.get('tileImage')
        self.sorting_priority = data.get('sortingPriority')
        self.hidden = data.get('hidden')