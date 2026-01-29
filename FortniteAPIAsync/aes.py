import datetime

class AESKeys:
    def __init__(self, data: dict) -> None:
        self.build = data.get('build')
        self.main_key = data.get('mainKey')

        self.updated = datetime.datetime.fromisoformat(
            data.get('updated').replace('Z', '+00:00')
        )
        self.dynamic_keys = [
            DynamicAESKey(key) for key in data.get('dynamicKeys', [])
        ]


class DynamicAESKey:
    def __init__(self, data: dict) -> None:
        self.filename = data.get('pakFilename')
        self.guid = data.get('pakGuid')
        self.key = data.get('key')