# -*- coding: utf-8 -*-
"""Storage class for ConsumeModel objects."""

import os.path
import fileops
from consumemodel import ConsumeModel

_instances = dict()


def get_instance(model):
    """Return an instance of ConsumeStore."""
    global _instances
    if not isinstance(model, ConsumeModel):
        raise TypeError(
            "get_instance() expects a parker.ConsumeModel derivative."
        )

    try:
        instance = _instances[repr(model)]
    except KeyError:
        instance = ConsumeStore(model)
        _instances[repr(model)] = instance

    return instance


class ConsumeStore(object):

    """An object to store our ConsumeModel."""

    def __init__(self, model):
        """Constructor."""
        self.model = model

    def save_media(self, path=fileops.IMG_DIR):
        """Store any media within model.media_list."""
        path = fileops.get_chunk_path_from_string(
            self.model.unique_field,
            prefix=os.path.join(
                path,
                self.model.site
            )
        )

        for i, mediafile in enumerate(self.model.media_list):
            if not os.path.exists(path):
                fileops.create_dirs(path)

            filename = os.path.join(
                path,
                "%s_%d" % (self.model.unique_field, i)
            )
            mediafile.fetch_to_file(filename)

    def save_data(self, path=fileops.DATA_DIR):
        """Store data as a JSON dump."""
        path = os.path.join(
            path,
            self.model.classification,
            self.model.site + '.data'
        ) if self.model.classification is not None else os.path.join(
            path,
            self.model.site + '.data'
        )
        fileops.dump_dict_to_file(
            self.model.get_dict(),
            path
        )
