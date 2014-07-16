# -*- coding: utf-8 -*-
"""Test the Page object."""

import pytest
from parker import page, client
from test_client import client_fixture, client_fixture_crawl
import utils

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_URI_CRAWL = "http://www.staples.co.uk/"
TEST_CONTENT = utils.load_stub_as_string('staples-stapler.html')
TEST_HASH = "0dde441f3c6bf49ce133c7aedf8e11b734b56926b487574654715bf97ff87dec"


def _fixture(fixture, uri):
    test_page = page.get_instance(
        uri=uri
    )
    test_page.client = fixture

    return test_page


@pytest.fixture(scope="function")
def page_fixture(client_fixture):
    """Test fixture to ensure correct mocking for page."""
    return _fixture(client_fixture, TEST_URI)


@pytest.fixture(scope="function")
def page_fixture_crawl(client_fixture_crawl):
    """Test fixture to ensure correct mocking for page."""
    return _fixture(client_fixture_crawl, TEST_URI_CRAWL)


def test_get_instance_creates_page_object():
    """Test page.get_instance creates a Page object."""
    test_page = page.get_instance(TEST_URI)
    expected_repr = "<class 'parker.page.Page'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_page, page.Page)
    assert isinstance(test_page.client, client.Client)
    assert test_page.__repr__() == expected_repr


def test_fetch_populates_page_content(page_fixture):
    """Test page.fetch populates page.content."""
    test_page = page_fixture
    test_page.fetch()

    assert test_page.content == TEST_CONTENT
    assert test_page.hash == TEST_HASH
