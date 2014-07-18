# -*- coding: utf-8 -*-
"""Test the CrawlModel object."""

from parker import crawlmodel
from test_client import client_fixture_crawl
from test_page import page_fixture_crawl
from test_crawlpage import crawlpage_fixture


def test_get_instance_creates_crawlmodel_object(crawlpage_fixture):
    """Test crawlmodel.get_instance creates a CrawlModel object."""
    test_crawlmodel = crawlmodel.get_instance(crawlpage_fixture)

    assert isinstance(test_crawlmodel, crawlmodel.CrawlModel)
