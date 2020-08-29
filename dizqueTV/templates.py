from typing import List

PLEX_SETTINGS_TEMPLATE = {
    "name": str,
    "uri": str,
    "accessToken": str,
    "index": int,
    "arChannels": bool,
    "arGuide": bool,
    "_id": str
}

CHANNEL_SETTINGS_TEMPLATE = {
    "programs": List,
    "fillerContent": List,
    "fillerRepeatCooldown": int,
    "fallback": [],
    "icon": str,
    "disableFillerOverlay": bool,
    "iconWidth": int,
    "iconDuration": int,
    "iconPosition": str,
    "startTime": str,
    "offlinePicture": str,
    "offlineSoundtrack": str,
    "offlineMode": str,
    "number": int,
    "name": str,
    "duration": int,
    "_id": str,
    "overlayIcon": bool
}

REDIRECT_PROGRAM_TEMPLATE = {
    "isOffline": bool,
    "type": str,
    "duration": int,
    "channel": int
}

MOVIE_PROGRAM_TEMPLATE = {
    "title": str,
    "key": str,
    "ratingKey": str,
    "icon": str,
    "type": str,
    "duration": int,
    "summary": str,
    "rating": str,
    "date": str,
    "year": int,
    "plexFile": str,
    "file": str,
    "showTitle": str,
    "episode": int,
    "season": int,
    "serverKey": str
}

EPISODE_PROGRAM_TEMPLATE = {
    "title": str,
    "key": str,
    "ratingKey": str,
    "icon": str,
    "type": str,
    "duration": int,
    "summary": str,
    "rating": str,
    "date": str,
    "year": int,
    "plexFile": str,
    "file": str,
    "showTitle": str,
    "episode": int,
    "season": int,
    "serverKey": str,
    "showIcon": str,
    "episodeIcon": str,
    "seasonIcon": str
}

FILLER_ITEM_TEMPLATE = {
    "title": str,
    "key": str,
    "ratingKey": str,
    "icon": str,
    "type": str,
    "duration": int,
    "summary": str,
    "date": str,
    "year": int,
    "plexFile": str,
    "file": str,
    "showTitle": str,
    "episode": int,
    "season": int,
    "serverKey": str
}
