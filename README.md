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

primes.is_prime(7)
# True
primes.get_primes(10)
# [2, 3, 5, 7]
primes.get_primes_parallel(10)
# [2, 3, 5, 7]
```

parallel is multi-threaded and uses the multiprocessing module.


## License

MIT License Copyright (c) 2022 Takahashi Akari <akaritakahashioss@gmail.com>

