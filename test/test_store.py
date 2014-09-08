# -*- coding: utf-8 -*-
"""Test the Store object."""

import pytest
from mock import MagicMock, call
from parker import store
from test_mediafile import mediafile_fixture, client_fixture

TEST_BUCKET = 'test_bucket.test.parker.python'
TEST_FILENAME = 'BIG/FAT/TEST_FILE_0'
EXPECTED_FILENAME = '/tmp/BIG/FAT/TEST_FILE_0'


@pytest.fixture(scope="function")
def s3store_fixture(monkeypatch):
    """Test fixture to ensure correct mocking for mediafile."""
    monkeypatch.setattr(
        store.boto,
        'connect_s3',
        MagicMock()
    )
    test_store = store.get_s3store_instance(
        bucket=TEST_BUCKET
    )
    monkeypatch.setattr(
        store,
        'Key',
        MagicMock()
    )

    return test_store


def test_store_media_sets_contents_from_temp_filename(
    s3store_fixture, mediafile_fixture
):
    s3store = s3store_fixture
    s3store.store_media(
        TEST_FILENAME,
        mediafile_fixture
    )

    kall = call().set_contents_from_filename(
        EXPECTED_FILENAME
    )

    assert store.Key.mock_calls[1] == kall.call_list()[1]
