#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import Database
import Strings
import re

SERVER_PORT = 8080
get_user_regex = re.compile(r"/users/(\d+)$")
get_user_playlists_regex = re.compile(r"/users/(\d+)/playlists$")
get_user_playlist_regex = re.compile(r"/users/(\d+)/playlists/(\d+)$")
get_track_regex = re.compile(r"/tracks/(\d+)$")
get_artist_regex = re.compile(r"/artists/(\d+)$")
delete_user_regex = re.compile(r"delete/users/(\d+)$")


class ServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if 'application/json' not in str(self.headers):
            self.send_error(415, Strings.message_415, Strings.message_explanation_415)

        if self.path == "/users":
            database_response = Database.get_users()

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif get_user_regex.match(str(self.path)):
            user_id = get_user_regex.match(str(self.path))[1]

            database_response = Database.get_user(user_id)

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif get_user_playlists_regex.match(str(self.path)):
            user_id = get_user_playlists_regex.match(str(self.path))[1]

            database_response = Database.get_user_playlists(user_id)

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
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
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif self.path == "/tracks":
            database_response = Database.get_tracks()

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif get_track_regex.match(str(self.path)):
            track_id = get_track_regex.match(str(self.path))[1]

            database_response = Database.get_track(track_id)

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif self.path == "/artists":
            database_response = Database.get_artists()

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        elif get_artist_regex.match(str(self.path)):
            artist_id = get_artist_regex.match(str(self.path))[1]

            database_response = Database.get_artist(artist_id)

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())

        else:
            self.send_error(404, Strings.message_404, Strings.message_explanation_404)
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b"POST")
        return

    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b"PUT")
        return

    def do_DELETE(self):

        if self.path == "/delete/users/":
            database_response = Database.get_users()

            if database_response is None:
                self.send_error(204, Strings.message_204, Strings.message_explanation_204)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(database_response.encode())
        return


if __name__ == '__main__':
    server = HTTPServer(('', SERVER_PORT), ServerRequestHandler)

    print('Started http server on port ' + str(SERVER_PORT) + '...')

    server.serve_forever()
