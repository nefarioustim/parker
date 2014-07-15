# -*- coding: utf-8 -*-
"""Test the CrawlPage object."""

import pytest
from parker import parser, crawlpage, parsedpage
from test_client import client_fixture_crawl
from test_page import page_fixture_crawl

TEST_URI = "http://www.staples.co.uk/"


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
