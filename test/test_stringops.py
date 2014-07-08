# -*- coding: utf-8 -*-
"""Test the string operations."""

import parker.stringops

TEST_STRING = 'MAGICUNICORNS'
TEST_NUM_CHARS = 3
EXPECTED_CHUNKS = [
    'MAG',
    'ICU',
    'NIC',
    'ORN',
    'S'
]


def test_generate_chunks_yields_correct_chunks():
    """Test stringops.generate_chunks yields the expected chunks."""
    for i, chunk in enumerate(
        parker.stringops.generate_chunks(TEST_STRING, TEST_NUM_CHARS)
    ):
        assert chunk == EXPECTED_CHUNKS[i]
