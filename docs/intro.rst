Getting started
===============

Installation
------------

**FortniteAPIAsync requires Python 3.9 or higher**

**Windows**

.. code:: sh

    py -3 -m pip install FortniteAPIAsync

**Linux**

.. code:: sh

    python3 -m pip install FortniteAPIAsync


Basic example
-------------

.. code-block:: python3

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