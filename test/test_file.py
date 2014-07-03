# -*- coding: utf-8 -*-
"""Test the file methods."""

import os
import parker.file

TEST_FILE_PATH = "/tmp/test/file/path"
TEST_FILE = "/tmp/test.log"
TEST_STRING = "This is a string."
TEST_DICT = {
    "this": "dict"
}
TEST_DICT_LINE = '{"this": "dict"}'


def test_create_dirs_actually_creates_dirs():
    """Test file.create_dirs actually creates all dirs in path."""
    parker.file.create_dirs(TEST_FILE_PATH)

    assert os.path.isdir(TEST_FILE_PATH)

    os.removedirs(TEST_FILE_PATH)


def test_dump_string_to_file_dumps_to_file():
    """Test string is output, and get_line_from_file loads it back in."""
    parker.file.dump_string_to_file(TEST_STRING, TEST_FILE)
    line = parker.file.get_line_from_file(TEST_FILE).next()

    assert line == TEST_STRING

    os.remove(TEST_FILE)


def test_dump_dict_to_file():
    """Test dict is output, and get_line_from_file loads it back in."""
    parker.file.dump_dict_to_file(TEST_DICT, TEST_FILE)
    line = parker.file.get_line_from_file(TEST_FILE).next()

    assert line == TEST_DICT_LINE

    os.remove(TEST_FILE)
