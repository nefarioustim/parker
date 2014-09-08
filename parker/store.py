# -*- coding: utf-8 -*-
"""Store Parker images and data on the filesystem."""

import abc
import os
import fileops

_instances = dict()


def get_filestore_instance(img_dir=None, data_dir=None):
    """Return an instance of FileStore."""
    global _instances

    key = "%s:%s" % (img_dir, data_dir)

    try:
        instance = _instances[key]
    except KeyError:
        instance = FileStore(
            img_dir=img_dir, data_dir=data_dir
        )
        _instances[key] = instance

    return instance


class StoreBase(object):

    """Base class for storage objects."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def store_media(self, filename, mediafile):
        """Store media files."""

    @abc.abstractmethod
    def store_json(self, filename, dict_to_store):
        """Store json files."""


class FileStore(StoreBase):

    """Class for file storage."""

    def __init__(self, img_dir=None, data_dir=None):
        """Constructor."""
        self.img_dir = img_dir or fileops.IMG_DIR
        self.data_dir = data_dir or fileops.DATA_DIR

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s:%s)" % (
            self.__class__, self.img_dir, self.data_dir
        )

    def store_media(self, filename, mediafile):
        filename = os.path.join(
            self.img_dir,
            filename
        )
        fileops.create_dirs(filename)
        mediafile.fetch_to_file(filename)

    def store_json(self, filename, dict_to_store):
        filename = os.path.join(
            self.data_dir,
            filename
        )
        fileops.dump_dict_to_file(
            dict_to_store,
            filename
        )


class S3Store(StoreBase):

    """Class for S3 storage."""

    def __init__(self, bucket):
        """Constructor."""
        self.bucket = bucket
        self.img_dir = img_dir or fileops.IMG_DIR
        self.data_dir = data_dir or fileops.DATA_DIR

    def store_media(self, filename, mediafile):
        """Store media files."""

    def store_json(self, filename, dict_to_store):
        """Store json files."""
