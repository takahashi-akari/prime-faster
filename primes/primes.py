# primes - Faster Prime Number Generator
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License Copyright (c) 2022 Takahashi Akari <akaritakahashioss@gmail.com>
# Version: 0.0.1
# Date: 2022-08-08
# Python: 3.10.6
# Description: primes - Faster Prime Number Generator

import math
import numpy

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3 :: 2 * k] = False
            sieve[k * ( k - 2 * (i & 1 ) + 4) // 3 :: 2 * k] = False
    np = numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1)|1)]
    # return array
    return np.tolist()
