#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import Database
import Strings
import re
import json
import Validation

SERVER_PORT = 8080

get_user_regex = re.compile(r"/users/(\d+)$")
get_user_playlists_regex = re.compile(r"/users/(\d+)/playlists$")
get_user_playlist_regex = re.compile(r"/users/(\d+)/playlists/(\d+)$")
get_user_playlist_tracks_regex = re.compile(r"/users/(\d+)/playlists/(\d+)/tracks$")
get_track_regex = re.compile(r"/tracks/(\d+)$")
get_artist_regex = re.compile(r"/artists/(\d+)$")
delete_user_regex = re.compile(r"/users/(\d+)$")
delete_artist_regex = re.compile(r"/artists/(\d+)$")
delete_track_regex = re.compile(r"/tracks/(\d+)$")
put_users_regex = re.compile(r"/users/(\d+)$")
post_user_tracks_in_playlist_regex = re.compile(r"/users/(\d+)/playlists/(\d+)$")
content_length_regex = re.compile(r"content-length: (\d+)")


class ServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if 'application/json' not in str(self.headers):
                self.send_error(415, Strings.message_415, Strings.message_explanation_415)

            if self.path == "/users":
                database_response = Database.get_users()

                if database_response is None:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_user_regex.match(str(self.path)):
                user_id = get_user_regex.match(str(self.path))[1]

                database_response = Database.get_user(user_id)

                if database_response is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_user_playlists_regex.match(str(self.path)):
                user_id = get_user_playlists_regex.match(str(self.path))[1]

                if Database.get_user(user_id) is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)

                database_response = Database.get_user_playlists(user_id)

                if database_response is None:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_user_playlist_regex.match(str(self.path)):
                user_id = get_user_playlist_regex.match(str(self.path))[1]
                playlist_id = get_user_playlist_regex.match(str(self.path))[2]

                database_response = Database.get_user_playlist(user_id, playlist_id)

                if database_response is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_user_playlist_tracks_regex.match(str(self.path)):
                user_id = get_user_playlist_tracks_regex.match(str(self.path))[1]
                playlist_id = get_user_playlist_tracks_regex.match(str(self.path))[2]

                database_response_user = Database.get_user(user_id)
                database_response_user_playlists = Database.get_user_playlist(user_id, playlist_id)
                database_response_user_playlists_tracks = Database.get_user_playlist_tracks(playlist_id)

                if database_response_user is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                elif database_response_user_playlists is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                elif database_response_user_playlists_tracks is None:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response_user_playlists_tracks.encode())

            elif self.path == "/tracks":
                database_response = Database.get_tracks()

                if database_response is None:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_track_regex.match(str(self.path)):
                track_id = get_track_regex.match(str(self.path))[1]

                database_response = Database.get_track(track_id)

                if database_response is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif self.path == "/artists":
                database_response = Database.get_artists()

                if database_response is None:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            elif get_artist_regex.match(str(self.path)):
                artist_id = get_artist_regex.match(str(self.path))[1]

                database_response = Database.get_artist(artist_id)

                if database_response is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(database_response.encode())

            else:
                self.send_error(404, Strings.message_404, Strings.message_explanation_404)
            return
        except:
            self.send_error(500, Strings.message_500, Strings.message_explanation_500)

    def do_POST(self):
        try:
            if 'Content-Type: application/json' not in str(self.headers):
                self.send_error(415, Strings.message_415, Strings.message_explanation_415)

            if self.path == "/users":
                content_length = int(content_length_regex.search(str(self.headers))[1])
                users = self.rfile.read(content_length).decode()

                validation = Validation.validate_json_users(users)

                if validation == "Invalid data":
                    self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                elif validation == "Invalid JSON":
                    self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                else:
                    database_response = Database.insert_users(json.loads(users))

                    if database_response is True:
                        self.send_error(204)
                    else:
                        self.send_error(409, Strings.message_409, Strings.message_explanation_409)

            elif post_user_tracks_in_playlist_regex.match(str(self.path)):
                content_length = int(content_length_regex.search(str(self.headers))[1])
                data = self.rfile.read(content_length).decode()
                user_id = post_user_tracks_in_playlist_regex.match(str(self.path))[1]
                playlist_id = post_user_tracks_in_playlist_regex.match(str(self.path))[2]

                if Database.get_user(user_id) is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)

                elif Database.get_user_playlist(user_id, playlist_id) is None:
                    self.send_error(404, Strings.message_404, Strings.message_explanation_404)
                else:
                    validation = Validation.validate_json_tracks(data)

                    if validation == "Invalid data":
                        self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                    elif validation == "Invalid JSON":
                        self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                    else:
                        database_response = Database.insert_tracks_user_playlist(json.loads(data), playlist_id)

                        if database_response is True:
                            self.send_error(204)
                        else:
                            self.send_error(409, Strings.message_409, Strings.message_explanation_409)

            elif self.path == "/artists":
                content_length = int(content_length_regex.search(str(self.headers))[1])
                artists = self.rfile.read(content_length).decode()

                validation = Validation.validate_json_artists(artists)

                if validation == "Invalid data":
                    self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                elif validation == "Invalid JSON":
                    self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                else:
                    database_response = Database.insert_artists(json.loads(artists))

                    if database_response is True:
                        self.send_error(204)
                    else:
                        self.send_error(409, Strings.message_409, Strings.message_explanation_409)

            elif self.path == "/tracks":
                content_length = int(content_length_regex.search(str(self.headers))[1])
                tracks = self.rfile.read(content_length).decode()

                validation = Validation.validate_json_tracks(tracks)

                if validation == "Invalid data":
                    self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                elif validation == "Invalid JSON":
                    self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                else:
                    database_response = Database.insert_tracks(json.loads(tracks))

                    if database_response is True:
                        self.send_error(204)
                    else:
                        self.send_error(409, Strings.message_409, Strings.message_explanation_409)

            else:
                self.send_error(404, Strings.message_404, Strings.message_explanation_404)
            return
        except:
            self.send_error(500, Strings.message_500, Strings.message_explanation_500)

    def do_PUT(self):
        try:
            if 'Content-Type: application/json' not in str(self.headers):
                self.send_error(415, Strings.message_415, Strings.message_explanation_415)

            if self.path == "/users":
                content_length = int(content_length_regex.search(str(self.headers))[1])
                users = self.rfile.read(content_length).decode()

                validation = Validation.validate_json_users(users)

                if validation == "Invalid data":
                    self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                elif validation == "Invalid JSON":
                    self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                else:
                    database_response = Database.insert_users_overwrite(json.loads(users))

                    if database_response is True:
                        self.send_error(204)
                    else:
                        self.send_error(409, Strings.message_409, Strings.message_explanation_409)

            elif self.path == "/tracks":
                content_length = int(content_length_regex.search(str(self.headers))[1])
                tracks = self.rfile.read(content_length).decode()

                validation = Validation.validate_json_tracks(tracks)

                if validation == "Invalid data":
                    self.send_error(422, Strings.message_422, Strings.message_explanation_422)
                elif validation == "Invalid JSON":
                    self.send_error(400, Strings.message_400, Strings.message_explanation_400)
                else:
                    database_response = Database.insert_tracks_overwrite(json.loads(tracks))

                    if database_response is True:
                        self.send_error(204)
                    else:
                        self.send_error(409, Strings.message_409, Strings.message_explanation_409)
            else:
                self.send_error(404, Strings.message_404, Strings.message_explanation_404)

            return
        except:
            self.send_error(500, Strings.message_500, Strings.message_explanation_500)

    def do_DELETE(self):
        try:
            if self.path == "/users":
                database_response = Database.delete_users()

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            elif delete_user_regex.match(str(self.path)):
                user_id = delete_user_regex.match(str(self.path))[1]

                database_response = Database.delete_user(user_id)

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            elif self.path == "/artists":
                database_response = Database.delete_artists()

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            elif delete_artist_regex.match(str(self.path)):
                artist_id = delete_artist_regex.match(str(self.path))[1]

                database_response = Database.delete_artist(artist_id)

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            elif self.path == "/tracks":
                database_response = Database.delete_tracks()

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            elif delete_track_regex.match(str(self.path)):
                track_id = delete_track_regex.match(str(self.path))[1]

                database_response = Database.delete_track(track_id)

                if database_response is False:
                    self.send_error(204)
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"")

            else:
                self.send_error(404, Strings.message_404, Strings.message_explanation_404)
            return
        except:
            self.send_error(500, Strings.message_500, Strings.message_explanation_500)


if __name__ == '__main__':
    server = HTTPServer(('', SERVER_PORT), ServerRequestHandler)

    print('Started http server on port ' + str(SERVER_PORT) + '...')

    server.serve_forever()
