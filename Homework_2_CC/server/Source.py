#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import Database
import Strings
import json

SERVER_PORT = 8080


class ServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if 'application/json' not in str(self.headers):
            self.send_error(415, Strings.message_415, Strings.message_explanation_415)
        if self.path == "/users":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(Database.get_users().encode())
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
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b"DELETE")
        return


if __name__ == '__main__':
    server = HTTPServer(('', SERVER_PORT), ServerRequestHandler)

    print('Started http server on port ' + str(SERVER_PORT) + '...')

    server.serve_forever()
