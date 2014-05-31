# -*- coding: utf-8 -*-
"""Test the HTTP client."""

from parker import client


def test_client_creation():
    """Test client factory creates a client object."""
    test_client = client.get_instance()
    expected_repr = "<class 'parker.client.Client'>(%s)" % (
        test_client.headers["user_agent"]
    )

    assert isinstance(test_client, client.Client) is True
    assert test_client.__repr__() == expected_repr
