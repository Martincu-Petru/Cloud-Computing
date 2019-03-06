import socket
import threading
import re

from sys import argv

content_length_regex = re.compile("content-length: (\\d+)")
method_type_regex = re.compile("(\\w)+")
content_type_regex = re.compile("Content-Type: ((\\w|/)+)")
request_uri_regex = re.compile("\\w+ (.+?) HTTP")


def get():
    return None


def delete():
    return None


def post():
    return None


def put():
    return None


def get_content(response):
    content_length = int(content_length_regex.search(response)[1])

    return response[-content_length:]


def get_method_type(response):
    return method_type_regex.search(response)[0]


def get_content_type(response):
    return content_type_regex.search(response)[1]


def get_request_uri(response):
    return request_uri_regex.search(response)[1]


def serve_request(connection):
    response = ""
    data = ""

    data += connection.recv(1024).decode()
    while len(data) == 1024:
        response += data
        data = connection.recv(1024).decode()
    response += data

    # print(response)
    # print(get_content(response))
    # print(get_method_type(response))
    # print(get_content_type(response))
    # print(get_request_uri(response))

    method_type = get_method_type(response)

    if method_type == "GET":
        get()
    elif method_type == "POST":
        post()
    elif method_type == "PUT":
        put()
    else:
        delete()

    connection.close()


def run(port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(50)

    while True:
        (connection, address) = server.accept()

        threading.Thread(target=serve_request, args=(connection,)).start()


if __name__ == "__main__":

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
