# -*- coding: utf-8 -*-
"""Test the HTTP client."""

import pytest
from mock import Mock, MagicMock
from requests import Response, exceptions
from parker import client
import utils

TEST_URI = 'http://httpbin.org/get'
TEST_CONSUME_CONTENT = utils.load_stub_as_string('staples-stapler.html')
TEST_CRAWL_CONTENT = utils.load_stub_as_string('staples-home.html')
TEST_STATUS_CODE = 200
TEST_BAD_STATUS_CODE = 410


def _fixture(content, status_code, monkeypatch):
    mocked_response = Mock(
        spec=Response()
    )
    mocked_response.content = content
    mocked_response.status_code = status_code
    mocked_response.iter_content.return_value = utils.load_stub_as_iterable(
        'stapler.jpg'
    )
    mocked_response.headers = {
        'content-type': 'image/jpeg'
    }

    monkeypatch.setattr(
        client.requests,
        'get',
        MagicMock(
            return_value=mocked_response
        )
    )

    return client.get_instance()


@pytest.fixture(scope="function")
def client_fixture(monkeypatch):
    """Test fixture to ensure correct mocking for client."""
    return _fixture(TEST_CONSUME_CONTENT, TEST_STATUS_CODE, monkeypatch)


@pytest.fixture(scope="function")
def client_fixture_crawl(monkeypatch):
    """Test fixture to ensure correct mocking for client."""
    return _fixture(TEST_CRAWL_CONTENT, TEST_STATUS_CODE, monkeypatch)


@pytest.fixture(scope="function")
def bad_client_fixture(monkeypatch):
    """Test fixture to ensure correct mocking for client."""
    return _fixture(TEST_CONSUME_CONTENT, TEST_BAD_STATUS_CODE, monkeypatch)


def test_get_instance_creates_client_object():
    """Test client.get_instance creates a Client object."""
    test_client = client.get_instance()
    expected_repr = "<class 'parker.client.Client'>(%s)" % (
        test_client.headers["user_agent"]
    )

    assert isinstance(test_client, client.Client)
    assert test_client.__repr__() == expected_repr


def test_get_calls_requests_get_with_correct_uri(client_fixture):
    """Test client.get calls requests.get with the correct URI."""
    test_client = client_fixture
    response = test_client.get(TEST_URI)

    called_uri = client.requests.get.call_args[0][0]

    assert called_uri == TEST_URI


def test_get_content_returns_stubbed_content(client_fixture):
    """Test client.get_content returns stubbed content."""
    test_client = client_fixture
    content = test_client.get_content(TEST_URI)

    assert content == TEST_CONSUME_CONTENT


def test_get_iter_content_calls_response_iter_content(client_fixture):
    """Test client.get_iter_content returns iterable content from stream."""
    test_client = client_fixture
    content = test_client.get_iter_content(TEST_URI)

    assert client.requests.get.call_args[1]['stream']


def test_get_content_throws_exception_when_bad_status(bad_client_fixture):
    """Test client.get_content throws exception on bad status code."""
    test_client = bad_client_fixture
    with pytest.raises(exceptions.HTTPError):
        content = test_client.get_content(TEST_URI)
