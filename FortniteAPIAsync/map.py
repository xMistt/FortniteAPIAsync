class Map:
    """Represents the current Fortnite Battle Royale map.

    Attributes
    ----------
    blank_image: :class:`str`
        An image of the map without POIs labelled.
    pois_image: :class:`str`
        An image of the map with POIs labelled.
    pois: :class:`list`[:class:`POI`]
        List of points of interest on the map.
    """

    def __init__(self, data: dict) -> None:
        self.blank_image = data.get('images', {}).get('blank')
        self.pois_image  = data.get('images', {}).get('pois')

        self.pois = [POI(raw_poi) for raw_poi in data.get('pois')]


class POI:
    """Represents a point of interest on the map.

    Attributes
    ----------
    id: :class:`str`
        The ID of the POI.
    name: :class:`str`
        The name of the POI.
    x: :class:`float`
        The X coordinate of the POI.
    y: :class:`float`
        The Y coordinate of the POI.
    z: :class:`float`
        The Z coordinate of the POI.
    """

    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.name = data.get('name')

        self.x = float(data.get('location', {}).get('x'))
        self.y = float(data.get('location', {}).get('y'))
        self.z = float(data.get('location', {}).get('z'))