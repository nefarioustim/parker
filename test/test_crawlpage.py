# -*- coding: utf-8 -*-
"""Test the CrawlPage object."""

import pytest
from parker import parser, crawlpage, parsedpage
from test_client import client_fixture_crawl
from test_page import page_fixture_crawl
import utils

TEST_URI = "http://www.staples.co.uk/"
EXPECTED_URI_COUNT = 300
EXPECTED_URIS = set(utils.load_stub_as_json('expecteduris.json'))


@pytest.fixture(scope="function")
def crawlpage_fixture(page_fixture_crawl):
    """Test fixture to ensure correct mocking for crawlpage."""
    return crawlpage.get_instance(
        page_fixture_crawl
    )


def test_get_instance_creates_crawlpage_object(page_fixture_crawl):
    """Test crawlpage.get_instance creates a CrawlPage object."""
    test_crawlpage = crawlpage.get_instance(
        page_fixture_crawl
    )
    expected_repr = "<class 'parker.crawlpage.CrawlPage'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_crawlpage, crawlpage.CrawlPage)
    assert isinstance(test_crawlpage.parsedpage, parsedpage.ParsedPage)
    assert test_crawlpage.__repr__() == expected_repr


def test_get_instance_raises_typeerror_unexpected_parameter_type():
    """Test crawlpage.get_instance throws TypeError on unexpected param."""
    with pytest.raises(TypeError):
        test_crawlpage = crawlpage.get_instance(None)


def test_get_uris_returns_list_of_internal_uris(crawlpage_fixture):
    """Test crawlpage.get_uris returns a set of internal URIs."""
    test_crawlpage = crawlpage_fixture
    uris = test_crawlpage.get_uris(TEST_URI)

    assert isinstance(uris, set)
    assert len(uris) == EXPECTED_URI_COUNT
    assert uris == EXPECTED_URIS
