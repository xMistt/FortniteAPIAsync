class CreatorCode:
    def __init__(self, data: dict) -> None:
        self.code = data.get('code')

        self.account_id = data.get('account', {}).get('id')
        self.display_name = data.get('account', {}).get('name')

        self.status = data.get('status')
        self.verified = data.get('verified')