# -*- coding: utf-8 -*-
"""Storage class for ConsumeModel objects."""

import os.path
import fileops
from consumemodel import ConsumeModel


def save_media(model, path=fileops.IMG_DIR):
    _raise_typeerror_on_bad_model(model)
    path = fileops.get_chunk_path_from_string(
        model.unique_field,
        prefix=os.path.join(
            path,
            model.site
        )
    )

    for i, mediafile in enumerate(model.media_list):
        if not os.path.exists(path):
            fileops.create_dirs(path)

        filename = os.path.join(
            path,
            "%s_%d" % (model.unique_field, i)
        )
        mediafile.fetch_to_file(filename)


def save_data(model, path=fileops.DATA_DIR):
    _raise_typeerror_on_bad_model(model)
    path = os.path.join(
        path,
        model.classification,
        model.site + '.data'
    ) if model.classification is not None else os.path.join(
        path,
        model.site + '.data'
    )
    fileops.dump_dict_to_file(
        model.get_dict(),
        path
    )


def _raise_typeerror_on_bad_model(model):
    if not isinstance(model, ConsumeModel):
        raise TypeError(
            "Expecting a ConsumeModel derivative."
        )
