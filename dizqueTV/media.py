import json

import dizqueTV.helpers as helpers
from dizqueTV.exceptions import NotRemoteObjectError


def _check_for_dizque_instance(func):
    """
    Check if an object has a _dizque_instance attribute before executing function
    :param func: Function to execute if object does have a _dizque_instance attribute
    :return: Result of func
    """

    def inner(obj, **kwargs):
        if obj._dizque_instance:
            return func(obj, **kwargs)
        raise NotRemoteObjectError(object_type=type(obj).__name__)

    return inner


class BaseMediaItem:
    def __init__(self, data: json, dizque_instance, channel_instance=None):
        self._data = data
        self._dizque_instance = dizque_instance
        self.type = data.get('type')
        self.isOffline = data.get('isOffline')
        self.duration = data.get('duration')

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.type}>"


class MediaItem(BaseMediaItem):
    def __init__(self, data: json, dizque_instance, channel_instance=None):
        super().__init__(data=data, dizque_instance=dizque_instance, channel_instance=channel_instance)
        self.title = data.get('title')
        self.key = data.get('key')
        self.ratingKey = data.get('ratingKey')
        self.duration = data.get('duration')
        self.icon = data.get('icon')
        self.summary = data.get('summary')
        self.date = data.get('date')
        self.year = data.get('year')
        self.plexFile = data.get('plexFile')
        self.file = data.get('file')
        self.showTitle = data.get('showTitle')
        self.episode = data.get('episode')
        self.season = data.get('season')
        self.serverKey = data.get('serverKey')

        self.showIcon = data.get('showIcon')
        self.episodeIcon = data.get('episodeIcon')
        self.seasonIcon = data.get('seasonIcon')

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.title}>"


class Redirect(BaseMediaItem):
    def __init__(self, data: json, dizque_instance, channel_instance):
        super().__init__(data=data, dizque_instance=dizque_instance)
        self._channel_instance = channel_instance
        self.channel = data.get('channel')

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.channel}>"


class Program(MediaItem, Redirect):
    def __init__(self, data: json, dizque_instance, channel_instance):
        super().__init__(data=data, dizque_instance=dizque_instance, channel_instance=channel_instance)
        self.rating = data.get('rating')

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.title}>"

    @_check_for_dizque_instance
    def delete(self) -> bool:
        """
        Delete this program
        :return: True if successful, False if unsuccessful
        """
        return self._channel_instance.delete_program(program=self)


class FillerItem(MediaItem):
    def __init__(self, data: json, dizque_instance, filler_list_instance):
        super().__init__(data=data, dizque_instance=dizque_instance)
        self._filler_list_instance = filler_list_instance

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.title}>"

    @_check_for_dizque_instance
    def delete(self) -> bool:
        """
        Delete this filler
        :return: True if successful, False if unsuccessful
        """
        return self._filler_list_instance.delete_filler(filler=self)
