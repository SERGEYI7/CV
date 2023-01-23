from multiprocessing import context
import time

class Indenter:

    def print(self, word):
        print(word)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class Timer:
    def __init__(self):
        self.start_time = float()
        self.end_time = float()

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(self.end_time - self.start_time)

from math import sqrt

with Timer() as timer:
    for i in range(1000):
        for j in range(i):
            aa = sqrt(j)


from contextlib import contextmanager

@contextmanager
def timer_func():
    try:
        start_time = time.time()
        yield
    finally:
        end_time = time.time()
        print(end_time - start_time)

with timer_func() as timer:
        for i in range(1000):
            for j in range(i):
                aa = sqrt(j)