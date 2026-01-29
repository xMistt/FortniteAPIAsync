class Map:
    def __init__(self, data: dict) -> None:
        self.blank_image = data.get('images', {}).get('blank')
        self.pois_image  = data.get('images', {}).get('pois')

        self.pois = [POI(raw_poi) for raw_poi in data.get('pois')]


class POI:
    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.name = data.get('name')

        self.x = float(data.get('location', {}).get('x'))
        self.y = float(data.get('location', {}).get('y'))
        self.z = float(data.get('location', {}).get('z'))