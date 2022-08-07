# primes - Faster Prime Number Generator
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License Copyright (c) 2022 Takahashi Akari <akaritakahashioss@gmail.com>
# Version: 0.0.1
# Date: 2022-08-08
# Python: 3.10.6
# Description: primes - Faster Prime Number Generator


import math
import multiprocessing


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def get_primes_mp(n):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    primes = pool.map(is_prime, range(2, n + 1))
    pool.close()
    pool.join()
    return primes
    
def benchmark(n):
    import time
    start = time.time()
    get_primes(n)
    end = time.time()
    print(end - start)
    start = time.time()
    get_primes_mp(n)
    end = time.time()
    print(end - start)

def benchmark_mp(n):
    import time
    start = time.time()
    get_primes_mp(n)
    end = time.time()
    print(end - start)

