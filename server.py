#!/usr/bin/env python3
"""server supplying data to the statusbar widget"""

from datetime import datetime
import functools
import json
from typing import Dict
from subprocess import PIPE, run

from flask import Flask
from spotipy import Spotify, util
import yaml

def _get_config(file_handle: str) -> Dict:
    """Read and return the config file."""
    with open(file_handle) as file_:
        configuration = yaml.load(file_)
    return configuration


def _get_spotify(username, client_id, client_secret, redirect_uri) -> Spotify:
    """Initialize and return a Spotify client."""
    scope = "user-read-currently-playing"  # only need to read current track
    token = util.prompt_for_user_token(username, scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    return Spotify(auth=token)


def populate_bar(spotify_client) -> str:
    """Return the JSON payload with all information."""
    payload = {
        "time": get_time(),
        "track": get_spotify_playing(spotify_client),
        "battery": get_battery_stats()
    }
    return json.dumps(payload)


def get_battery_stats() -> Dict:
    """Get some battery statistics."""
    battery = run(["pmset", "-g", "batt"], stdout=PIPE)
    battery_info = battery.stdout.decode("utf-8")

    info = battery_info.strip().split("\n")[1]
    _, levels = info.split("\t")
    percent, status, time, *_ = levels.split()

    statistics = {
        "percent": percent[:-1],
        "status": status[:-1],
        "time": time
    }

    return statistics


def get_time() -> str:
    """Grab the current time."""
    time = datetime.now()
    return time.strftime("%a %b %d %H:%M:%S CST %Y")

# TODO: make this asycnchronous, and call it first in the update so we
# get a full second to make the Spotify call
def get_spotify_playing(spotify_client) -> Dict:
    """Query Spotify API for currently playing track."""
    track: Dict = spotify_client.current_user_playing_track()
    album = track["item"]["album"]["name"]
    # TODO: collate all artists
    artist = track["item"]["artists"][0]["name"]
    name = track["item"]["name"]

    #spotify_string = ""
    track_info = {}
    if track["is_playing"]:
        track_info = {
            "name": name,
            "album": album,
            "artist": artist
        }

    return track_info


def main():
    """Run the server."""
    app = Flask(__name__)
    config = _get_config("config.yaml")
    spotify = _get_spotify(config["username"], config["client_id"],
                           config["client_secret"], config["redirect_uri"])

    # supply the main endpoint with the spotify client
    endpoint = functools.partial(populate_bar, spotify)
    app.add_url_rule('/', 'populate_bar', endpoint)

    app.run()


if __name__ == "__main__":
    main()
