# primes

## Description

This is a small program that finds all the prime numbers up to a given number faster than the naive algorithm.

## Install

```bash
$ pip install primes
```

## Usage

```python
import primes

print(primes.is_prime(7))
# True
print(primes.get_primes(10))
# [2, 3, 5, 7]
print(primes.get_primes_mp(10, 4))
# [2, 3, 5, 7]
```

mp is the multiprocessing version of the algorithm.

## License

MIT License Copyright (c) 2022 Takahashi Akari <akaritakahashioss@gmail.com>

