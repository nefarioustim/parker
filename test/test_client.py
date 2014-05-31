# -*- coding: utf-8 -*-
"""Test the HTTP client."""

from parker import client


def test_client_creation():
    """Test client factory creates a client object."""
    test_client = client.get_instance()

    assert isinstance(test_client, client.Client) is True
