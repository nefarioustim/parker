# -*- coding: utf-8 -*-
"""Model object for consumed pages in Parker."""

from datetime import datetime
import os.path
import consumepage
import fileops

_instances = dict()


def get_instance(page_to_consume):
    """Return an instance of ConsumeModel."""
    if isinstance(page_to_consume, basestring):
        uri = page_to_consume
        page_to_consume = consumepage.get_instance(uri)
    elif isinstance(page_to_consume, consumepage.ConsumePage):
        uri = page_to_consume.uri
    else:
        raise TypeError(
            "get_instance() expects a parker.ConsumePage "
            "or basestring derivative."
        )

    try:
        instance = _instances[uri]
    except KeyError:
        instance = ConsumeModel(page_to_consume)
        _instances[uri] = instance

    return instance


class ConsumeModel(object):

    """Model representing a consumed page."""

    def __init__(self, consumepage):
        """Constructor."""
        self.consumepage = consumepage
        self.uri = consumepage.uri
        self.hash = consumepage.hash
        self.unique_field = None
        self.site = None
        self.data_dict = None
        self.key_value_dict = None
        self.crumb_list = None
        self.media_list = None

    def save_to_file(self, file_path):
        """Save model to file."""
        data_dict = self._get_prepped_data_for_dump()
        fileops.dump_dict_to_file(
            data_dict,
            file_path
        )

    def save_media_to_file(self, file_path):
        """Save media to file."""
        path = fileops.get_chunk_path_from_string(
            self.unique_field,
            prefix=os.path.join(
                file_path,
                self.site,

            )
        )

        for i, mediafile in enumerate(self.media_list):
            if not os.path.exists(path):
                fileops.create_dirs(path)

            filename = os.path.join(
                path,
                "%s_%d" % (self.unique_field, i)
            )
            mediafile.fetch_to_file(filename)

    def load_from_config(self, config):
        """Load model from passed configuration."""
        self.site = config.get("id", False)
        specific_data_config = config.get("specific_data", False)
        self._load_data(
            specific_data_config
        )
        self._load_key_value(
            config.get("key_value_data", False)
        )
        self._load_crumb(
            config.get("crumbs", False)
        )
        self._load_media_list(
            config.get("media", False)
        )
        self.unique_field = self.data_dict.get(
            config.get("unique_field", False),
            False
        )
        self._post_process_data(specific_data_config)

    def _load_data(self, data_config):
        self.data_dict = self.consumepage.get_data_dict_from_config(
            data_config
        ) if data_config else None

    def _load_key_value(self, key_value_config):
        self.key_value_dict = self.consumepage.get_key_value_dict_by_selectors(
            key_value_config["key_selector"],
            key_value_config["value_selector"]
        ) if (
            key_value_config
            and key_value_config.get("key_selector", False)
            and key_value_config.get("value_selector", False)
        ) else None

    def _load_crumb(self, crumb_config):
        self.crumb_list = self.consumepage.get_crumb_list_by_selector(
            crumb_config["selector"]
        ) if (
            crumb_config
            and crumb_config.get("selector", False)
        ) else None

    def _load_media_list(self, media_config):
        self.media_list = self.consumepage.get_media_list_by_selector(
            media_config["selector"],
            media_config["attribute"],
        ) if (
            media_config
            and media_config.get("selector", False)
            and media_config.get("attribute", False)
        ) else None

    def _get_prepped_data_for_dump(self):
        data = self.data_dict.copy()
        data['key_value_data'] = self.key_value_dict
        data['crumbs'] = self.crumb_list if len(self.crumb_list) > 0 else None
        data['media'] = [
            mediafile.filename
            if mediafile.filename is not None
            else mediafile.uri
            for mediafile in self.media_list
        ] if len(self.media_list) > 0 else None

        data.update({
            "uri": self.uri,
            "crawled": datetime.utcnow().isoformat(),
        })

        return data

    def _post_process_data(self, config):
        for key, item in config.iteritems():
            kv_ref = item.get('kv_ref', False)
            value = self.key_value_dict.get(kv_ref, False)
            if kv_ref and value:
                self.data_dict[key] = self.key_value_dict.pop(kv_ref)
