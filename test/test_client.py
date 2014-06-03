# -*- coding: utf-8 -*-
"""Test the HTTP client."""

import pytest
from mock import Mock, MagicMock
from requests import Response
from parker import client
import utils

TEST_URI = 'http://httpbin.org/get'


@pytest.fixture(scope="function")
def client_fixture(monkeypatch):
    """Test fixture to mock the requests.get call within the HTTP client."""
    monkeypatch.setattr(
        client.requests,
        'get',
        MagicMock(
            return_value=Mock(
                spec=Response()
            )
        )
    )

    return client.get_instance()


def test_client_creation():
    """Test client.get_instance creates a Client object."""
    test_client = client.get_instance()
    expected_repr = "<class 'parker.client.Client'>(%s)" % (
        test_client.headers["user_agent"]
    )

    assert isinstance(test_client, client.Client) is True
    assert test_client.__repr__() == expected_repr


def test_client_get_calls_requests_get_with_correct_uri(client_fixture):
    """Test client.get calls Requests' get method with the correct URI."""
    test_client = client_fixture
    response = test_client.get(TEST_URI)

    called_uri = client.requests.get.call_args[0][0]

    assert called_uri == TEST_URI
