"""Salesforce Streaming API client for asyncio"""
import logging

from aiosfstream_ng._metadata import VERSION as __version__  # noqa: F401
from aiosfstream_ng.client import Client, SalesforceStreamingClient  # noqa: F401
from aiosfstream_ng.client import ReplayMarkerStoragePolicy  # noqa: F401
from aiosfstream_ng.auth import PasswordAuthenticator  # noqa: F401
from aiosfstream_ng.auth import RefreshTokenAuthenticator  # noqa: F401
from aiosfstream_ng.replay import ReplayMarker, ReplayOption  # noqa: F401
from aiosfstream_ng.replay import MappingStorage  # noqa: F401
from aiosfstream_ng.replay import DefaultMappingStorage  # noqa: F401
from aiosfstream_ng.replay import ConstantReplayId  # noqa: F401
from aiosfstream_ng.replay import ReplayMarkerStorage  # noqa: F401

# Create a default handler to avoid warnings in applications without logging
# configuration
logging.getLogger(__name__).addHandler(logging.NullHandler())
