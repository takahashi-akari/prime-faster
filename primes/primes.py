# primes - Faster Prime Number Generator
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License (https://opensource.org/licenses/MIT)
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

def get_primes_parallel(n, n_processes):
    pool = multiprocessing.Pool(n_processes)
    primes = pool.map(get_primes, range(1, n + 1))
    pool.close()
    pool.join()
    return primes
