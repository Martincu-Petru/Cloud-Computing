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

    if results is None:
        return results
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

    if results is None:
        return results
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

    if results is None:
        return results
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

    track_data = {
        "track_id": result[0],
        "track_name": result[1],
        "artist_id": result[2]
    }

    return json.dumps(track_data)


def get_artists():
    artists = {"artists": []}
    cursor = database.cursor()

    cursor.execute("SELECT * FROM artists")
    results = cursor.fetchall()

    if results is None:
        return results
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

def delete_users(user_id):
    cursor = database.cursor()
