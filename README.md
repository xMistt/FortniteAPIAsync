<div align="center">

# FortniteAPIAsync

Python wrapper for [Fortnite-API.com](https://fortnite-api.com).

[![Downloads](https://static.pepy.tech/badge/fortniteapiasync)](https://pepy.tech/project/fortniteapiasync)
[![Python](https://img.shields.io/badge/python-3.9%20%E2%80%93%203.14-blue?logo=python&logoColor=white)](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?logo=python&logoColor=white)
[![FortniteAPIAsync Version: 2.0.0](https://img.shields.io/pypi/v/fortniteapiasync.svg)](https://pypi.org/project/fortniteapiasync/)
[![PEP-8 Compliant](https://img.shields.io/badge/PEP8-compliant-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)
![Last Commit](https://img.shields.io/github/last-commit/xMistt/FortniteAPIAsync?logo=github)
[![Docs](https://img.shields.io/readthedocs/fortniteapiasync/latest?logo=readthedocs)](https://fortniteapiasync.readthedocs.io)

</div>


## Installation
```commandline
# windows
py -3 -m pip install -U FortniteAPIAsync

# linux/macos
python3 -m pip install -U FortniteAPIAsync
```

## Examples
### Standard example
```python
import FortniteAPIAsync
import asyncio


async def get_current_aes() -> None:
    client = FortniteAPIAsync.APIClient()
    
    aes = await client.get_aes()
    print(f'AES key for {aes.build} - {aes.main_key}')
    # outputs: AES key for ++Fortnite+Release-39.40-CL-50341043 - 67e127d5c846a0d426be...
    
    await client.close()


asyncio.run(get_current_aes())
```

### rebootpy example
```python
import rebootpy
import FortniteAPIAsync

from rebootpy.ext import commands


bot = commands.Bot(
    command_prefix='!',
    auth=rebootpy.AuthorizationCodeAuth(
        code=input('Enter authorization code: ')
    )
)
fortnite_api = FortniteAPIAsync.APIClient()


@bot.command()
async def skin(ctx: rebootpy.ext.commands.Context, *, content: str) -> None:
    try:
        cosmetic = await fortnite_api.get_cosmetic(
            matchMethod="contains",
            name=content,
            backendType="AthenaCharacter"
        )

        await bot.party.me.set_outfit(asset=cosmetic.id)
        await ctx.send(f'Skin set to {cosmetic.id}.')
    except FortniteAPIAsync.exceptions.NotFound:
        await ctx.send(f"Failed to find a skin with the name: {content}.")


bot.run()
```