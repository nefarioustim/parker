# -*- coding: utf-8 -*-
"""Storage class for ConsumeModel objects."""

import os.path
import fileops
import store
from consumemodel import ConsumeModel

UNCLASSIFIED_PREFIX = 'unclassified'
_instances = dict()


def get_instance(
    model, method="file",
    img_dir=None, data_dir=None
):
    """Return an instance of ConsumeStore."""
    global _instances
    if not isinstance(model, ConsumeModel):
        raise TypeError(
            "get_instance() expects a parker.ConsumeModel derivative."
        )

    if method == "file":
        my_store = store.get_filestore_instance(
            img_dir=img_dir,
            data_dir=data_dir
        )
    else:
        raise ValueError("Unexpected method value, '%s'." % method)

    key = "%s:%s" % (repr(model), repr(method))

    try:
        instance = _instances[key]
    except KeyError:
        instance = ConsumeStore(model, my_store)
        _instances[key] = instance

    return instance


class ConsumeStore(object):

    """An object to store our ConsumeModel."""

    def __init__(self, model, store):
        """Constructor."""
        self.model = model
        self.store = store

    def save_media(self):
        """Store any media within model.media_list."""
        chunk_path = fileops.get_chunk_path_from_string(
            self.model.unique_field
        )

        for i, mediafile in enumerate(self.model.media_list):
            filename = os.path.join(
                self._get_prefix(),
                chunk_path,
                "%s_%d" % (self.model.unique_field, i)
            )
            self.store.store_media(filename, mediafile)

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

    def _get_prefix(self):
        prefix_list = [self.model.site]
        if self.model.classification:
            prefix_list.insert(0, self.model.classification)

        return os.path.join(
            *prefix_list
        )
