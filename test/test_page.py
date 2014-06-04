# -*- coding: utf-8 -*-
"""Test the Page object."""

import pytest
from parker import page, client
from test_client import client_fixture
import utils

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_CONTENT = utils.load_stub_as_string('staples-stapler.html')


@pytest.fixture(scope="function")
def page_fixture(client_fixture):
    """Test fixture to ensure correct mocking for page."""
    return page.get_instance(
        uri=TEST_URI,
        page_client=client_fixture
    )


def test_page_get_instance_creates_page_object():
    """Test page.get_instance creates a Page object."""
    test_page = page.get_instance(TEST_URI)
    expected_repr = "<class 'parker.page.Page'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_page, page.Page) is True
    assert isinstance(test_page.client, client.Client) is True
    assert test_page.__repr__() == expected_repr


def test_page_fetch_populates_page_content(page_fixture):
    """Test page.fetch populates page.content."""
    test_page = page_fixture
    test_page.fetch()

    assert test_page.content == TEST_CONTENT
