# -*- coding: utf-8 -*-
"""Test the Store object."""

import pytest
from mock import MagicMock, call
from parker import store
from test_mediafile import mediafile_fixture, client_fixture

TEST_BUCKET = 'test_bucket.test.parker.python'
TEST_FILENAME = 'BIG/FAT/TEST_FILE_0'
TEST_DICT = {
    "foo": "bar",
    "fuzzy": "duck",
    "big": {
        "data": "google",
        "butts": "sir mixalot"
    },
    "list": [
        "barney",
        "fred"
    ]
}
EXPECTED_FILENAME = '/tmp/BIG/FAT/TEST_FILE_0'
EXPECTED_JSON = '{"fuzzy": "duck", "foo": "bar", "list": ["barney", "fred"], "big": {"data": "google", "butts": "sir mixalot"}}'


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
        EXPECTED_FILENAME + '.jpg'
    )

    assert store.Key.mock_calls[1] == kall.call_list()[1]


def test_store_json_sets_contents_as_json_dumps(
    s3store_fixture
):
    s3store = s3store_fixture
    s3store.store_json(
        TEST_FILENAME,
        TEST_DICT
    )

    kall = call().set_contents_from_string(
        EXPECTED_JSON
    )

    assert store.Key.mock_calls[1] == kall.call_list()[1]
