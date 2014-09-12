# -*- coding: utf-8 -*-
"""MediaFile object for Parker."""

import client

_instances = dict()
_content_type_map = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/gif': 'gif'
}


def get_instance(uri):
    """Return an instance of MediaFile."""
    global _instances
    try:
        instance = _instances[uri]
    except KeyError:
        instance = MediaFile(
            uri,
            client.get_instance()
        )
        _instances[uri] = instance

    return instance


class MediaFile(object):

    """A MediaFile, as fetched from a client."""

    def __init__(self, uri, client):
        """Constructor."""
        self.uri = uri
        self.client = client
        self.filename = None
        self.fileext = None

    def __repr__(self):
        """Return an unambiguous representation."""
        return "%s(%s)" % (self.__class__, self.uri)

    def fetch_to_file(self, filename):
        """Stream the MediaFile to the filesystem."""
        self.filename = filename
        stream = self.client.get_iter_content(self.uri)
        content_type = self.client.response_headers['content-type']

        if content_type in _content_type_map:
            self.fileext = _content_type_map[content_type]
            self.filename = "%s.%s" % (self.filename, self.fileext)

        with open(self.filename, 'wb') as file_handle:
            for chunk in stream:
                file_handle.write(chunk)
