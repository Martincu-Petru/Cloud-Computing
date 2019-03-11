#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import Database

SERVER_PORT = 8080


class ServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b"GET")
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

