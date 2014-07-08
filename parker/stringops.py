# -*- coding: utf-8 -*-
"""String functions for Parker."""


def generate_chunks(string, num_chars):
    """Yield num_chars-character chunks from string."""
    for start in range(0, len(string), num_chars):
        yield string[start:start+num_chars]
