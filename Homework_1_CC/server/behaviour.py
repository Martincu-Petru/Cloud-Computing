import urllib.request
import time
import threading
import math


min_request_wait_time = math.inf
max_request_wait_time = 0


def do_get(number_of_requests):

    global min_request_wait_time
    global max_request_wait_time

    average_latency = 0

    for i in range(0, number_of_requests):

        request_start_time = time.time()
        contents = urllib.request.urlopen("http://127.0.0.1:8080").read()
        request_end_time = time.time() - request_start_time

        print("Request wait time: " + str(request_end_time))

        if min_request_wait_time > request_end_time:
            min_request_wait_time = request_end_time
        if request_end_time > max_request_wait_time:
            max_request_wait_time = request_end_time

        average_latency += request_end_time

    print("Average request time: " + str(average_latency/number_of_requests))


def run():

    global max_request_wait_time
    global min_request_wait_time

    threads = []

    for _ in range(0, 3):
        threads.append(threading.Thread(target=do_get, args=(2, )))

    for i in range(0, 3):
        threads[i].start()

    for i in range(0, 3):
        threads[i].join()

    print("Max response time: " + str(max_request_wait_time))
    print("Min response time: " + str(min_request_wait_time))


if __name__ == "__main__":
    run()
