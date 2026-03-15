import requests

gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',            
         'https://gist.github.com/recluze/a98aa1804884ca3b3ad3', 
            'https://gist.github.com/recluze/5051735efe3fc189b90d', 
            'https://gist.github.com/recluze/460157afc6a7492555bb',            
            'https://gist.github.com/recluze/5051735efe3fc189b90d', 
            'https://gist.github.com/recluze/c9bc4130af995c36176d']

from contextlib import contextmanager
import time


@contextmanager
def timeit():
    start = int(round(time.time() * 1000))
    yield
    end = int(round(time.time() * 1000))
    print(f"Elapsed time: {end - start} ms")


def get_gist(g):
    print("Starting request: %s" % g)
    r = requests.get(g)
    g_length = len(r.text)
    print("Got response of length: %d" % g_length)


# with timeit():
#     lengths = []
#     for g in gists:
#         get_gist(g)
#     print("All Done!")


# Let's do all these in parallel!
import threading

with timeit():
    threads = []
    for g in gists:
        # Create workers
        t = threading.Thread(target=get_gist, args=(g,))


        # Go!
        t.start()
        threads.append(t) # Keep a list for record

    for t in threads:
        t.join()  # Wait for all to finish
    
    print("All Done!")





