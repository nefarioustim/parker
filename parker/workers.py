# -*- coding: utf-8 -*-
"""Worker methods for Parker."""

import os.path
import consumemodel
from configloader import load_site_config
from fileops import IMG_DIR, DATA_DIR


def consumer(site, uri):
    """Consume URI using site config."""
    site_config = load_site_config(site)
    model = consumemodel.get_instance(uri)
    model.load_from_config(site_config)
    model.save_media_to_file(IMG_DIR)
    model.save_to_file(
        os.path.join(
            DATA_DIR,
            site + '.data'
        )
    )
