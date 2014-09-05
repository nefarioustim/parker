# -*- coding: utf-8 -*-
"""Test the file operations."""

import os
import parker.fileops

TEST_FILE_PATH = "/tmp/test/file/path"
TEST_FILE = "/tmp/test.log"
TEST_STRING = "This is a string."
TEST_DICT = {
    "this": "dict"
}
TEST_DICT_LINE = '{"this": "dict"}'
TEST_CHUNK_STRING = 'MAGICUNICORNS'
EXPECTED_CHUNK_PATH = 'MAG/ICU/NIC/ORN/S'


def test_create_dirs_actually_creates_dirs():
    """Test fileops.create_dirs actually creates all dirs in path."""
    parker.fileops.create_dirs(TEST_FILE_PATH)

    assert os.path.isdir(TEST_FILE_PATH)

    os.removedirs(TEST_FILE_PATH)


def test_dump_string_to_file_dumps_to_file():
    """Test string is output, and get_line_from_file loads it back in."""
    parker.fileops.dump_string_to_file(TEST_STRING, TEST_FILE)
    line = parker.fileops.get_line_from_file(TEST_FILE).next()

    assert line == TEST_STRING

    os.remove(TEST_FILE)


def test_dump_dict_to_file():
    """Test dict is output, and get_line_from_file loads it back in."""
    parker.fileops.dump_dict_to_file(TEST_DICT, TEST_FILE)
    line = parker.fileops.get_line_from_file(TEST_FILE).next()

    assert line == TEST_DICT_LINE

    os.remove(TEST_FILE)


def test_get_chunk_path_from_string():
    """Test fileops.get_chunk_path_from_string returns the expected path."""
    path = parker.fileops.get_chunk_path_from_string(
        TEST_CHUNK_STRING
    )

    assert path == EXPECTED_CHUNK_PATH
