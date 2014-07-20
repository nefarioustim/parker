# -*- coding: utf-8 -*-
"""Module for loading JSON configuration."""

import json
import os

_path = os.path.abspath(__file__)
_dir_path = os.path.dirname(_path)

CONFIG_EXT = ".json"
CONFIG_PATH = os.path.join(
    _dir_path,
    'config'
)
CONFIG_SITES_PATH = 'sites'


def _load_config_json(file_path):
    """Load the passed file as JSON."""
    return json.load(open(file_path))


def load_config(name):
    """Load and return configuration as a dict."""
    return _load_config_json(
        os.path.join(
            CONFIG_PATH,
            name + CONFIG_EXT
        )
    )


def load_site_config(name):
    """Load and return site configuration as a dict."""
    return _load_config_json(
        os.path.join(
            CONFIG_PATH,
            CONFIG_SITES_PATH,
            name + CONFIG_EXT
        )
    )
