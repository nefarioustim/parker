# -*- coding: utf-8 -*-
"""Test the MediaFile object."""

from parker import mediafile, client

TEST_URI = "//www.staples.co.uk/content/images/product/uk_412852_1_xnl.jpg"


def test_get_instance_creates_mediafile_object():
    """Test mediafile.get_instance creates a MediaFile object."""
    test_mediafile = mediafile.get_instance(TEST_URI)
    expected_repr = "<class 'parker.mediafile.MediaFile'>(%s)" % (
        TEST_URI
    )

    assert isinstance(test_mediafile, mediafile.MediaFile)
    assert isinstance(test_mediafile.client, client.Client)
    assert test_mediafile.__repr__() == expected_repr
