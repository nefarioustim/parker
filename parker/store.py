# -*- coding: utf-8 -*-
"""Store Parker images and data on the filesystem."""

import abc
import json
import os
import time
import boto
from boto.s3.key import Key
import fileops

_filestore_instances = dict()
_s3store_instances = dict()


def get_filestore_instance(img_dir=None, data_dir=None):
    """Return an instance of FileStore."""
    global _filestore_instances

    key = "%s:%s" % (img_dir, data_dir)

    try:
        instance = _filestore_instances[key]
    except KeyError:
        instance = FileStore(
            img_dir=img_dir, data_dir=data_dir
        )
        _filestore_instances[key] = instance

    return instance


def get_s3store_instance(bucket):
    """Return an instance of S3Store."""
    global _s3store_instances

    key = "%s" % bucket

    try:
        instance = _s3store_instances[key]
    except KeyError:
        instance = S3Store(
            bucket=bucket
        )
        _s3store_instances[key] = instance

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
        """Store media files."""
        filename = os.path.join(
            self.img_dir,
            filename
        )
        fileops.create_dirs(
            os.path.dirname(filename)
        )
        mediafile.fetch_to_file(filename)

    def store_json(self, filename, dict_to_store):
        """Store json files."""
        filename = os.path.join(
            self.data_dir,
            filename + '.data'
        )
        fileops.dump_dict_to_file(
            dict_to_store,
            filename
        )


class S3Store(StoreBase):

    """Class for S3 storage."""

    def __init__(self, bucket):
        """Constructor."""
        conn = boto.connect_s3()
        self.bucket = conn.get_bucket(bucket)

    def store_media(self, filename, mediafile):
        """Store media files."""
        s3_key = Key(self.bucket)
        s3_key.key = os.path.join(
            '/images',
            filename
        )
        temp_filename = os.path.join(
            '/tmp',
            filename
        )
        fileops.create_dirs(
            os.path.dirname(temp_filename)
        )
        mediafile.fetch_to_file(temp_filename)
        s3_key.set_contents_from_filename(
            temp_filename
        )
        os.remove(mediafile.filename)

    def store_json(self, filename, dict_to_store):
        """Store json files."""
        epoch = int(time.time() * (10 ** 6))
        s3_key = Key(self.bucket)
        s3_key.key = os.path.join(
            '/data',
            "%s_%s.data" % (filename, epoch)
        )
        s3_key.set_contents_from_string(
            json.dumps(dict_to_store)
        )
