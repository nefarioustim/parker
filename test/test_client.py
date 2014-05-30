"""Test the HTTP client."""
# -*- coding: utf-8 -*-

from ..factories import ClientFactory
from ..client import Client


def test_client_factory():
    """Test client factory creates a client object."""
    client_factory = ClientFactory()
    test_client = client_factory.get()

    assert isinstance(test_client, Client) is True
