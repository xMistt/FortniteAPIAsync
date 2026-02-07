from . import __version__
from .exceptions import InvalidParameters, NotFound, Private

from typing import Any, Dict, Union

import aiohttp
import json


class HTTPClient:
    def __init__(self,
                 base: str = 'https://fortnite-api.com',
                 headers: dict = None,
                 session: aiohttp.ClientSession = None
                 ) -> None:
        self.base = base

        self.session = session

        self.headers = headers or {}
        self.headers.setdefault(
            'User-Agent',
            f'FortniteAPIAsync/{__version__}'
        )

    async def close(self) -> None:
        if self.session:
            await self.session.close()
            self.session = None

    async def set_session(self) -> None:
        self.session = aiohttp.ClientSession(
            headers=self.headers
        )

    async def api_request(self,
                      url: str,
                      method: str = 'GET',
                      params: dict = None,
                      **kwargs: Any
                      ) -> dict:
        if not self.session:
            await self.set_session()

        async with self.session.request(
            method=method,
            url=f'{self.base}{url}',
            params=params,
            **kwargs
        ) as request:
            raw = await request.json()
            data = raw['data'] if 'data' in raw else raw

            if request.status == 400:
                raise InvalidParameters(data.get('error'))
            elif request.status == 404:
                raise NotFound(data.get('error'))
            elif request.status == 403:
                raise Private(data.get('error'))

            return data