# FortniteAPIAsync
Python wrapper for Fortnite-API.

[![Downloads](https://pepy.tech/badge/fortniteapiasync)](https://pepy.tech/project/fortniteapiasync)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/fortniteapiasync.svg)](https://pypi.org/project/fortniteapiasync/)
[![FortniteAPIAsync Version: 1.0.1](https://img.shields.io/pypi/v/fortniteapiasync.svg)](https://pypi.org/project/fortniteapiasync/)

## Installing:
Windows: ``py -3 -m pip install FortniteAPIAsync``<br>
Linux/macOS: ``python3 -m pip install FortniteAPIAsync``

## Examples:
```python
import FortniteAPIAsync
import asyncio


async def fnapi_search() -> None:
    result = await FortniteAPIAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name="Ghoul Trooper"
    )

    print(result.id)


loop = asyncio.get_event_loop()
loop.run_until_complete(fnapi_search())
loop.close()
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

fortnitepy example:
```python
import fortnitepy
import FortniteAPIAsync

from fortnitepy.ext import commands


bot = commands.Bot(
    command_prefix='!',
    auth=fortnitepy.AuthorizationCodeAuth(
        code=input('Enter authorization code: ')
    )
)


@bot.command()
async def skin(ctx: fortnitepy.ext.commands.Context, *, content: str) -> None:
    try:
        cosmetic = await FortniteAPIAsync.get_cosmetic(
            matchMethod="contains",
            name=content,
            backendType="AthenaCharacter"
        )

        await ctx.send(f'Skin set to {cosmetic.id}.')
        print(f"Set skin to: {cosmetic.id}.")
        await client.party.me.set_outfit(asset=cosmetic.id)

    except FortniteAPIAsync.exceptions.NotFound:
        await ctx.send(f"Failed to find a skin with the name: {content}.")
        print(f"Failed to find a skin with the name: {content}.")


bot.run()
```