import datetime

class AESKeys:
    """Represents AES encryption keys.

    Attributes
    ----------
    build: :class:`str`
        The Fortnite build version the keys apply to.
    main_key: :class:`str`
        The main AES encryption key.
    updated: :class:`datetime.datetime`
        Datetime when the keys were last updated.
    dynamic_keys: :class:`list`[:class:`DynamicAESKey`]
        List of dynamic AES keys.
    """

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
    """Represents a dynamic AES key.

    Attributes
    ----------
    filename: :class:`str`
        The pak filename associated with the key.
    guid: :class:`str`
        The GUID of the pak file.
    key: :class:`str`
        The AES encryption key.
    """

    def __init__(self, data: dict) -> None:
        self.filename = data.get('pakFilename')
        self.guid = data.get('pakGuid')
        self.key = data.get('key')