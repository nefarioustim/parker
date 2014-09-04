# -*- coding: utf-8 -*-
"""File functions for Parker."""

import json
import os
from configloader import load_config
from stringops import generate_chunks

_config = load_config("parker")

VAR_DIR = _config.get(
    "storage-directory",
    os.path.join(
        os.environ.get('PROJECT'),
        'var'
    )
)
LOG_DIR = os.path.join(VAR_DIR, 'log')
DATA_DIR = os.path.join(VAR_DIR, 'data')
IMG_DIR = os.path.join(VAR_DIR, 'img')


def create_dirs(path):
    """Create all directories in @path."""
    try:
        os.makedirs(path)
    except OSError, error:
        if error.errno != 17:
            raise


def dump_string_to_file(string, filepath):
    """Dump @string as a line to @filepath."""
    create_dirs(
        os.path.dirname(filepath)
    )

    with open(filepath, 'a') as outfile:
        outfile.write(string)
        outfile.write('\n')


def dump_dict_to_file(dictionary, filepath):
    """Dump @dictionary as a line to @filepath."""
    create_dirs(
        os.path.dirname(filepath)
    )

    with open(filepath, 'a') as outfile:
        json.dump(dictionary, outfile)
        outfile.write('\n')


def get_line_from_file(filename):
    """Generator to return a file line by line."""
    for row in open(filename, 'rU'):
        yield row.strip()


def get_chunk_path_from_string(string, prefix=None, chunk=3):
    """Return a chunked path from string."""
    path = os.path.join(
        *list(generate_chunks(
            string,
            chunk
        ))
    )

    if prefix is not None:
        path = os.path.join(
            prefix,
            path
        )

    return path
