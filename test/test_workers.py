# -*- coding: utf-8 -*-
"""Test the worker methods."""

import os.path
import shutil
import pytest
from parker import fileops
from parker.workers import consumer, crawler, killer, get_site_sets
from parker.queues import crawl_q, consume_q
from test_client import client_fixture, client_fixture_crawl
import utils

TEST_URI = "http://www.staples.co.uk/full-strip-stapler/cbs/412852.html"
TEST_URI_CRAWL = "http://www.staples.co.uk/"
TEST_SITE = "staples"
TEST_CLASSIFICATION = "supplies"
TEST_METHOD = "file"
EXPECTED_FILE = os.path.join(
    fileops.DATA_DIR,
    TEST_CLASSIFICATION,
    TEST_SITE,
    TEST_SITE + '.data'
)
EXPECTED_DATA_DICT = {
    'title': 'Full Strip Stapler',
    'sku': 'WW-412852'
}
EXPECTED_MEDIA_FILE = os.path.join(
    fileops.IMG_DIR,
    TEST_CLASSIFICATION,
    TEST_SITE,
    'WW-',
    '412',
    '852',
    'WW-412852_0.jpg'
)
EXPECTED_JOBS = 298
EXPECTED_TTL = 259200


def test_consumer_writes_data_to_file(client_fixture):
    """Test workers.consumer writes correct data to file system."""
    consumer(TEST_SITE, TEST_URI)

    assert os.path.isfile(EXPECTED_MEDIA_FILE)

    assert os.path.exists(EXPECTED_FILE)
    assert os.path.isfile(EXPECTED_FILE)

    line = fileops.get_line_from_file(EXPECTED_FILE).next()

    for key, value in EXPECTED_DATA_DICT.iteritems():
        assert value in line

    os.remove(EXPECTED_FILE)
    shutil.rmtree(os.path.join(
        fileops.IMG_DIR,
        TEST_CLASSIFICATION,
        TEST_SITE
    ))


@pytest.mark.skipif(not utils.is_online(), reason="Currently offline.")
def test_crawler_adds_links_to_crawl_queue(client_fixture_crawl):
    """Test workers.crawler adds links to the crawl queue."""
    killer(TEST_SITE)
    crawler(TEST_SITE, TEST_URI_CRAWL)

    assert len(crawl_q.jobs) == EXPECTED_JOBS
    assert len(consume_q.jobs) == 0

    killer(TEST_SITE)


@pytest.mark.skipif(not utils.is_online(), reason="Currently offline.")
def test_crawler_adds_links_to_consume_queue(client_fixture):
    """Test workers.crawler adds links to the consume queue."""
    killer(TEST_SITE)
    crawler(TEST_SITE, TEST_URI)

    assert len(crawl_q.jobs) == 0
    assert len(consume_q.jobs) == 1

    killer(TEST_SITE)


@pytest.mark.skipif(not utils.is_online(), reason="Currently offline.")
def test_crawler_obtains_expiry_from_config(client_fixture):
    killer(TEST_SITE)
    crawler(TEST_SITE, TEST_URI)
    visited_set, visited_uri_set, consume_set, crawl_set = get_site_sets(
        TEST_SITE
    )

    assert visited_set.ttl() <= EXPECTED_TTL
    assert visited_uri_set.ttl() <= EXPECTED_TTL
    assert consume_set.ttl() <= EXPECTED_TTL
    assert crawl_set.ttl() <= EXPECTED_TTL