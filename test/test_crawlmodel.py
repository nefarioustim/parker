# -*- coding: utf-8 -*-
"""Test the CrawlModel object."""

import pytest
from parker import crawlmodel
from parker.configloader import load_site_config
from test_client import client_fixture_crawl
from test_page import page_fixture_crawl
from test_crawlpage import crawlpage_fixture
import utils

TEST_CONFIG_NAME = "staples"
TEST_CONFIG = load_site_config(TEST_CONFIG_NAME)
EXPECTED_URI_BASE = "http://www.staples.co.uk/"
uri_list = utils.load_stub_as_json('expecteduris.json')
uri_list.remove(
    "http://www.staples.co.uk/content/static/customerservice"
    "/aboutus/staples_soul.cshtml?icid=ft:sssl"
)
EXPECTED_URIS = set(uri_list)


@pytest.fixture(scope="function")
def crawlmodel_fixture(crawlpage_fixture):
    """Test fixture to ensure correct mocking for parsedpage."""
    return crawlmodel.get_instance(crawlpage_fixture)


def test_get_instance_creates_crawlmodel_object(crawlpage_fixture):
    """Test crawlmodel.get_instance creates a CrawlModel object."""
    test_crawlmodel = crawlmodel.get_instance(crawlpage_fixture)

    assert isinstance(test_crawlmodel, crawlmodel.CrawlModel)


def test_get_instance_raises_typeerror_unexpected_parameter_type():
    """Test crawlmodel.get_instance throws TypeError on unexpected param."""
    with pytest.raises(TypeError):
        test_crawlmodel = crawlmodel.get_instance(None)


def test_load_from_config_populates_model(crawlmodel_fixture):
    """Test crawlmodel.load_from_config populates the model members."""
    test_crawlmodel = crawlmodel_fixture
    test_crawlmodel.load_from_config(TEST_CONFIG)

    assert test_crawlmodel.site == TEST_CONFIG_NAME
    assert test_crawlmodel.uri_base == EXPECTED_URI_BASE
    assert test_crawlmodel.uris_to_crawl == EXPECTED_URIS
    assert not test_crawlmodel.is_consume_page
