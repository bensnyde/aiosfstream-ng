aiosfstream-ng
===========

aicometd-ng is a Python 3.10+ compatible fork of https://github.com/robertmrk/aiosfstream

Usage
-----

.. code-block:: python

    import asyncio

    from aiosfstream-ng import SalesforceStreamingClient


    async def stream_events():
        # connect to Streaming API
        async with SalesforceStreamingClient(
                consumer_key="<consumer key>",
                consumer_secret="<consumer secret>",
                username="<username>",
                password="<password>") as client:

            # subscribe to topics
            await client.subscribe("/topic/one")
            await client.subscribe("/topic/two")

            # listen for incoming messages
            async for message in client:
                topic = message["channel"]
                data = message["data"]
                print(f"{topic}: {data}")

    if __name__ == "__main__":
        asyncio.run(stream_events())


Install
-------

.. code-block:: bash

    pip install aiosfstream-ng

Requirements
------------

- Python 3.6+
- aiohttp_
- aiocometd-ng_

.. _aiohttp: https://github.com/aio-libs/aiohttp/
.. _aiocometd-ng: https://github.com/robertmrk/aiocometd/
.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _api: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
.. _PushTopic: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/working_with_pushtopics.htm
.. _GenericStreaming: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/generic_streaming_intro.htm#generic_streaming_intro
.. _replay: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api_durability.htm
.. _PlatformEvents: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm
.. _ChangeDataCapture: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm
