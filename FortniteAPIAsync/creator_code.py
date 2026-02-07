class CreatorCode:
    """Represents a creator code.

    Attributes
    ----------
    code: :class:`str`
        The creator code.
    account_id: :class:`str`
        The account ID of the account associated with the creator code.
    display_name: :class:`str`
        The display name of the account associated with the creator code.
    status: :class:`str`
        The status of the creator code.
    verified: :class:`bool`
        Whether the creator code is verified.
    """

    def __init__(self, data: dict) -> None:
        self.code = data.get('code')

        self.account_id = data.get('account', {}).get('id')
        self.display_name = data.get('account', {}).get('name')

        self.status = data.get('status')
        self.verified = data.get('verified')