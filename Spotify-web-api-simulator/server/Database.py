import mysql.connector
import json

database = mysql.connector.connect(
    host="localhost",
    user="cloud.computing",
    passwd="12345",
    auth_plugin='mysql_native_password',
    database="database_cloud_computing"
)


def get_users():
    users = {"users": []}
    cursor = database.cursor()

    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    if len(results) is 0:
        return None
    else:
        for row in results:
            user_data = {}

            user_id = row[0]
            first_name = row[1]
            last_name = row[2]
            date_of_birth = row[3]
            is_premium = row[4]

            user_data["user_id"] = user_id
            user_data["first_name"] = first_name
            user_data["last_name"] = last_name
            user_data["date_of_birth"] = str(date_of_birth)
            user_data["is_premium"] = str(bool(is_premium))

            users["users"].append(user_data)

        return json.dumps(users)


def get_user(user_id):
    cursor = database.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id, ))
    result = cursor.fetchone()

    if result is None:
        return result

    user_data = {
        "user_id": result[0],
        "first_name": result[1],
        "last_name": result[2],
        "date_of_birth": str(result[3]),
        "is_premium": str(bool(result[4]))
    }

    return json.dumps(user_data)


def get_user_playlists(user_id):
    cursor = database.cursor()

    cursor.execute("SELECT p.playlist_id, playlist_name "
                   "FROM playlist_user p "
                   "JOIN users u ON p.user_id = u.user_id "
                   "JOIN playlists p2 ON p.playlist_id = p2.playlist_id "
                   "WHERE p.user_id = %s", (user_id,))
    results = cursor.fetchall()

    if len(results) is 0:
        return None
    else:
        playlists = {"playlists": []}

        for row in results:

            playlist = {}

            playlist_id = row[0]
            playlist_name = row[1]

            playlist["playlist_id"] = playlist_id
            playlist["playlist_name"] = playlist_name

            playlists["playlists"].append(playlist)

        return json.dumps(playlists)


def get_user_playlist(user_id, playlist_id):
    cursor = database.cursor()

    cursor.execute("SELECT p.playlist_id, playlist_name "
                   "FROM playlist_user p "
                   "JOIN users u ON p.user_id = u.user_id "
                   "JOIN playlists p2 ON p.playlist_id = p2.playlist_id "
                   "WHERE p.user_id = %s "
                   "AND p.playlist_id = %s", (user_id, playlist_id))
    results = cursor.fetchone()

    if results is None:
        return None
    else:
        playlist_id = results[0]
        playlist_name = results[1]

        playlist = {str(playlist_id): playlist_name}

        return json.dumps(playlist)


def get_tracks():
    tracks = {"tracks": []}
    cursor = database.cursor()

    cursor.execute("SELECT * FROM tracks")
    results = cursor.fetchall()

    if len(results) is 0:
        return None
    else:
        for row in results:
            track_data = {}

            track_id = row[0]
            track_name = row[1]
            artist_id = row[2]

            track_data["track_id"] = track_id
            track_data["track_name"] = track_name
            track_data["artist_id"] = artist_id

            tracks["tracks"].append(track_data)

        return json.dumps(tracks)


def get_track(track_id):
    cursor = database.cursor()

    cursor.execute("SELECT * FROM tracks WHERE track_id = %s", (track_id, ))
    result = cursor.fetchone()

    if result is None:
        return result
    else:
        track_data = {
            "track_id": result[0],
            "track_name": result[1],
            "artist_id": result[2]
        }

        return json.dumps(track_data)


def get_user_playlist_tracks(playlist_id):
    cursor = database.cursor()
    tracks = {"tracks": []}

    cursor.execute("SELECT tracks.track_id, track_name, artist_id "
                   "FROM playlist_tracks "
                   "JOIN tracks ON playlist_tracks.track_id = tracks.track_id "
                   "WHERE playlist_id = %s",
                   (playlist_id, ))

    results = cursor.fetchall()

    if len(results) is 0:
        return None
    else:
        for row in results:
            track_data = {}

            track_id = row[0]
            track_name = row[1]
            artist_id = row[2]

            track_data["track_id"] = track_id
            track_data["track_name"] = track_name
            track_data["artist_id"] = artist_id

            tracks["tracks"].append(track_data)

        return json.dumps(tracks)


def get_artists():
    artists = {"artists": []}
    cursor = database.cursor()

    cursor.execute("SELECT * FROM artists")
    results = cursor.fetchall()

    if len(results) is 0:
        return None
    else:
        for row in results:
            artist_data = {}

            artist_id = row[0]
            artist_name = row[1]

            artist_data["artist_id"] = artist_id
            artist_data["artist_name"] = artist_name

            artists["artists"].append(artist_data)

        return json.dumps(artists)


def get_artist(artist_id):
    cursor = database.cursor()

    cursor.execute("SELECT * FROM artists WHERE artist_id = %s", (artist_id, ))
    result = cursor.fetchone()

    if result is None:
        return result

    artist_data = {
        "artist_id": result[0],
        "artist_name": result[1]
    }

    return json.dumps(artist_data)


def delete_user(user_id):
    cursor = database.cursor()

    if get_user(user_id) is None:
        return False
    else:
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id, ))
        database.commit()

        return True


def delete_users():
    cursor = database.cursor()

    if get_users() is None:
        return False
    else:
        cursor.execute("DELETE FROM users")
        database.commit()

        return True


def delete_artist(artist_id):
    cursor = database.cursor()

    if get_artist(artist_id) is None:
        return False
    else:
        cursor.execute("DELETE FROM artists WHERE artist_id = %s", (artist_id, ))
        database.commit()

        return True


def delete_artists():
    cursor = database.cursor()

    if get_artists() is None:
        return False
    else:
        cursor.execute("DELETE FROM artists")
        database.commit()

        return True


def delete_track(track_id):
    cursor = database.cursor()

    if get_track(track_id) is None:
        return False
    else:
        cursor.execute("DELETE FROM tracks WHERE track_id = %s", (track_id, ))
        database.commit()

        return True


def delete_tracks():
    cursor = database.cursor()

    if get_tracks() is None:
        return False
    else:
        cursor.execute("DELETE FROM tracks")
        database.commit()

        return True


def insert_users(users):
    cursor = database.cursor()

    for user in users["users"]:
        user_id = int(user["user_id"])
        first_name = user["first_name"]
        last_name = user["last_name"]
        date_of_birth = user["date_of_birth"]
        is_premium = int(bool(user["is_premium"]))

        if get_user(user_id) is not None:
            return False

        cursor.execute("INSERT INTO users (user_id, first_name, last_name, date_of_birth, is_premium) "
                       "VALUES (%s, %s, %s, %s, %s)",
                       (user_id, first_name, last_name, date_of_birth, is_premium))

    database.commit()

    return True


def insert_users_overwrite(users):
    cursor = database.cursor()

    for user in users["users"]:
        user_id = int(user["user_id"])
        first_name = user["first_name"]
        last_name = user["last_name"]
        date_of_birth = user["date_of_birth"]
        is_premium = int(bool(user["is_premium"]))

        if get_user(user_id) is not None:
            delete_user(user_id)

        cursor.execute("INSERT INTO users (user_id, first_name, last_name, date_of_birth, is_premium) "
                       "VALUES (%s, %s, %s, %s, %s)",
                       (user_id, first_name, last_name, date_of_birth, is_premium))

    database.commit()

    return True


def insert_artists(artists):
    cursor = database.cursor()

    for artist in artists["artists"]:
        artist_id = int(artist["artist_id"])
        artist_name = artist["artist_name"]

        if get_artist(artist_id) is not None:
            return False

        cursor.execute("INSERT INTO artists (artist_id, artist_name) "
                       "VALUES (%s, %s)",
                       (artist_id, artist_name))

    database.commit()

    return True


def insert_tracks(tracks):
    cursor = database.cursor()

    for track in tracks["tracks"]:
        track_id = int(track["track_id"])
        track_name = track["track_name"]
        artist_id = int(track["artist_id"])

        if get_artist(artist_id) is None:
            return False

        if get_track(track_id) is not None:
            return False

        cursor.execute("INSERT INTO tracks (track_id, track_name, artist_id) "
                       "VALUES (%s, %s, %s)",
                       (track_id, track_name, artist_id))

    database.commit()

    return True


def insert_tracks_overwrite(tracks):
    cursor = database.cursor()

    for track in tracks["tracks"]:
        track_id = int(track["track_id"])
        track_name = track["track_name"]
        artist_id = int(track["artist_id"])

        if get_artist(artist_id) is None:
            return False

        if get_track(track_id) is not None:
            delete_track(track_id)

        cursor.execute("INSERT INTO tracks (track_id, track_name, artist_id) "
                       "VALUES (%s, %s, %s)",
                       (track_id, track_name, artist_id))

    database.commit()

    return True


def insert_tracks_user_playlist(tracks, playlist_id):
    cursor = database.cursor()

    for track in tracks["tracks"]:
        track_id = int(track["track_id"])
        track_name = track["track_name"]
        artist_id = int(track["artist_id"])

        if get_artist(artist_id) is None:
            return False
        if get_track(track_id) is not None:
            return False

        cursor.execute("INSERT INTO tracks (track_id, track_name, artist_id) "
                       "VALUES (%s, %s, %s)",
                       (track_id, track_name, artist_id))

        cursor.execute("INSERT INTO playlist_tracks (playlist_id, track_id) "
                       "VALUES (%s, %s)",
                       (playlist_id, track_id))

    database.commit()

    return True
