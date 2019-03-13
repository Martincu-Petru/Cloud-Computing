import json
import re

date_regex = re.compile(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))")


def validate_json_users(data):
    users = json.loads(data)

    if "users" not in users:
        return "Invalid JSON"

    for user in users["users"]:
        if "user_id" not in user:
            return "Invalid JSON"
        elif is_number(user["user_id"]) is False:
            return "Invalid data"
        if "first_name" not in user:
            return "Invalid JSON"
        if "last_name" not in user:
            return "Invalid JSON"
        if "date_of_birth" not in user:
            return "Invalid JSON"
        elif is_date(user["date_of_birth"]) is False:
            return "Invalid data"
        if "is_premium" not in user:
            return "Invalid JSON"
        elif is_boolean(user["is_premium"]) is False:
            return "Invalid data"

    return True


def validate_json_artists(data):
    artists = json.loads(data)

    if "artists" not in artists:
        return "Invalid JSON"

    for artist in artists["artists"]:
        if "artist_id" not in artist:
            return "Invalid JSON"
        elif is_number(artist["artist_id"]) is False:
            return "Invalid data"
        if "artist_name" not in artist:
            return "Invalid JSON"

    return True


def validate_json_tracks(data):
    tracks = json.loads(data)

    if "tracks" not in tracks:
        return "Invalid JSON"

    for track in tracks["tracks"]:
        if "track_id" not in track:
            return "Invalid JSON"
        elif is_number(track["track_id"]) is False:
            return "Invalid data"
        if "track_name" not in track:
            return "Invalid JSON"
        if "artist_id" not in track:
            return "Invalid JSON"
        elif is_number(track["artist_id"]) is False:
            return "Invalid data"

    return True


def is_number(number):
    try:
        int(number)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def is_date(date):
    if date_regex.match(date) is None:
        return False
    else:
        return True


def is_boolean(boolean):
    if boolean == "True" or boolean == "False":
        return True
    else:
        return False
