import aiohttp
import json
from typing import Any, Dict, Union


async def json_or_text(response: aiohttp.ClientResponse) -> Union[str, dict]:
    text = await response.text(encoding='utf-8')
    if 'application/json' in response.headers.get('content-type', ''):
        return json.loads(text)
    return text


class HTTPClient:
    def __init__(self,
                 connector: aiohttp.connector.BaseConnector = None,
                 base: str = 'https://fortnite-api.com',
                 headers: dict = {}
                 ) -> None:
        self.connector = connector
        self.base = base

        self.headers = headers
        self.headers['User-Agent'] = 'FortniteAPIAsync/1.0.0'

    async def request(self,
                      url: str,
                      method: str = 'GET',
                      params: dict = None,
                      **kwargs: Any
                      ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=method,
                    url=f'{self.base}{url}',
                    params=params,
                    headers=self.headers,
                    **kwargs
            ) as request:
                return await json_or_text(request)
