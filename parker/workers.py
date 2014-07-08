# -*- coding: utf-8 -*-
"""Worker methods for Parker."""

import os.path
import consumemodel
from configloader import load_site_config
from fileops import DATA_DIR


def consumer(site, uri):
    """Consume URI using site config."""
    model = consumemodel.get_instance(uri)
    model.load_from_config(
        load_site_config(site)
    )
    model.save_to_file(
        os.path.join(
            DATA_DIR,
            site + '.data'
        )
    )
