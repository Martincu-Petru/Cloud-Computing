#!/usr/bin/python
from sys import argv

import json
import requests
import re
import time
import threading
import socket


class RandomManager:

    @staticmethod
    def get_random_number(max_number):
        url = "http://numbersapi.com/random"
        params = {"min": 0, "max": max_number}
        headers = {"Content-Type": "application/json"}

        random_number_response = requests.get(url=url, params=params, headers=headers)

        return json.loads(random_number_response.text)["number"]


class NewYorkTimesManager:

    @staticmethod
    def get_current_articles():
        url = "https://api.nytimes.com/svc/news/v3/content/all/all.json"
        params = {"api-key": json.loads(open("config.txt", "r").read())["new-york-times-apiKEY"]}

        current_articles_response = requests.get(url=url, params=params)

        while "fault" in current_articles_response.text:
            current_articles_response = requests.get(url=url, params=params)

        return json.loads(current_articles_response.text)["results"]


class SpotifyManager:

    @staticmethod
    def get_access_token():
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": json.loads(open("config.txt", "r").read())["spotify-authorization"]}
        body = {"grant_type": "client_credentials"}

        acces_token_response = requests.post(url=url, headers=headers, data=body)

        return json.loads(acces_token_response.text)["access_token"]

    @staticmethod
    def get_artist_image(artist_id):
        url = "https://api.spotify.com/v1/artists/" + artist_id
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Bearer " + SpotifyManager.get_access_token()}

        artist_image = requests.get(url=url, headers=headers)

        return json.loads(artist_image.text)["images"][-1]["url"]

    @staticmethod
    def get_track(track_name):
        url = "https://api.spotify.com/v1/search"
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Bearer " + SpotifyManager.get_access_token()}
        params = {"q": track_name,
                  "type": "track",
                  "limit": 1}

        return json.loads(requests.get(url=url, headers=headers, params=params).text)


class RequestSolver:

    @staticmethod
    def get_response():
        current_articles = NewYorkTimesManager.get_current_articles()  # webAPI call
        random_article_number = RandomManager.get_random_number(len(current_articles) - 1)  # webAPI call
        word_list = re.split(" ", current_articles[random_article_number]["abstract"])
        random_word_number = RandomManager.get_random_number(len(word_list) - 1)  # webAPI call
        track = SpotifyManager.get_track(word_list[random_word_number])  # webAPI call
        artist_id = re.split(":", track["tracks"]["items"][0]["album"]["artists"][0]["uri"])[2]

        track_title = track["tracks"]["items"][0]["name"]
        track_writer = track["tracks"]["items"][0]["album"]["artists"][0]["name"]
        album_name = track["tracks"]["items"][0]["album"]["name"]
        album_cover_link = track["tracks"]["items"][0]["album"]["images"][0]["url"]
        artist_portrait_link = SpotifyManager.get_artist_image(artist_id)  # webAPI call
        spotify_link = track["tracks"]["items"][0]["album"]["artists"][0]["external_urls"]["spotify"]

        result = {
            "track_title": track_title,
            "artist_portrait_link": artist_portrait_link,
            "track_writer": track_writer,
            "album_cover_link": album_cover_link,
            "album_name": album_name,
            "spotify_link": spotify_link
        }

        return json.dumps(result)


def serve_request(connection):
    request_start_time = time.time()
    message = RequestSolver.get_response()
    request_end_time = time.time() - request_start_time

    response = connection.recv(1024).decode()

    if "GET / " in response:
        logfile = open("log.txt", "a")
        logfile.write("Date and time: " + time.asctime() + "\n\n")
        logfile.write("Latency: " + str(request_end_time) + "s" + "\n\n")
        logfile.write("Response: " + str(message) + "\n\n")
        logfile.write(response)
        logfile.write("----------------------------------------------------------------------\n\n")
        logfile.close()

    print(response)

    if "GET /metrics" in response:

        metrics = open("log.txt", "r").read()

        connection.sendall(bytes(("HTTP/1.0 200 OK"
                                  + "\r\nContent-Length: "
                                  + str(len(metrics))
                                  + "\r\nAccess-Control-Allow-Origin: *;"
                                  + "\r\nContent-Type: text/plain;"
                                  + "\r\n\r\n"
                                  + metrics
                                  + "\r\n").encode()))

    elif "GET / " in response:
        connection.sendall(bytes(("HTTP/1.0 200 OK"
                                  + "\r\nContent-Length: "
                                  + str(len(message))
                                  + "\r\nAccess-Control-Allow-Origin: *;"
                                  + "\r\nContent-Type: application/json;"
                                  + "\r\n\r\n"
                                  + message
                                  + "\r\n").encode()))
    else:
        connection.sendall(bytes(("HTTP/1.0 404 Not Found"
                                  + "\r\nContent-Length: "
                                  + str(10)
                                  + "\r\nAccess-Control-Allow-Origin: *;"
                                  + "\r\nContent-Type: text/html;"
                                  + "\r\n\r\n"
                                  + "NOT FOUND!"
                                  + "\r\n").encode()))

    connection.close()


def run(port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(50)

    while True:
        (connection, address) = server.accept()

        threading.Thread(target=serve_request, args=(connection, )).start()


if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
