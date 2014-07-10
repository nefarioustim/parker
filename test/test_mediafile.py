# -*- coding: utf-8 -*-
"""Test the MediaFile object."""

import os
import pytest
from parker import mediafile, client
from test_client import client_fixture
import utils

TEST_URI = "http://www.staples.co.uk/content/images/product/uk_412852_1_xnl.jpg"
TEST_FILE = "/tmp/somewhere"
EXPECTED_FILENAME = "/tmp/somewhere.jpg"


@pytest.fixture(scope="function")
def mediafile_fixture(client_fixture):
    """Test fixture to ensure correct mocking for mediafile."""
    test_mediafile = mediafile.get_instance(
        uri=TEST_URI
    )
    test_mediafile.client = client_fixture

    return test_mediafile


def test_get_instance_creates_mediafile_object():
    """Test mediafile.get_instance creates a MediaFile object."""
    test_mediafile = mediafile.get_instance(TEST_URI)
    expected_repr = "<class 'parker.mediafile.MediaFile'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_mediafile, mediafile.MediaFile)
    assert isinstance(test_mediafile.client, client.Client)
    assert test_mediafile.__repr__() == expected_repr


def test_fetch_to_file_downloads_to_file(mediafile_fixture):
    """Test mediafile.fetch_to_file downloads to file."""
    test_mediafile = mediafile_fixture
    test_mediafile.fetch_to_file(TEST_FILE)

    assert test_mediafile.filename == EXPECTED_FILENAME
    assert os.path.isfile(test_mediafile.filename)

    os.remove(test_mediafile.filename)
