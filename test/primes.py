# test ../primes/primes.py

# import ../primes/primes.py

import primes


def test_is_prime():
    assert primes.is_prime(1) is False
    assert primes.is_prime(2) is True
    assert primes.is_prime(3) is True
    assert primes.is_prime(4) is False
    assert primes.is_prime(5) is True
    assert primes.is_prime(6) is False
    assert primes.is_prime(7) is True
    assert primes.is_prime(8) is False
    assert primes.is_prime(9) is False
    assert primes.is_prime(10) is False
    assert primes.is_prime(11) is True
    assert primes.is_prime(12) is False
    assert primes.is_prime(13) is True
    assert primes.is_prime(14) is False
    assert primes.is_prime(15) is False
    assert primes.is_prime(16) is False
    assert primes.is_prime(17) is True
    assert primes.is_prime(18) is False
    assert primes.is_prime(19) is True
    assert primes.is_prime(20) is False
    assert primes.is_prime(21) is False
    assert primes.is_prime(22) is False
    assert primes.is_prime(23) is True
    assert primes.is_prime(24) is False
    assert primes.is_prime(25) is False
    assert primes.is_prime(26) is False
    assert primes.is_prime(27) is False
    assert primes.is_prime(28) is False
    assert primes.is_prime(29) is True
    assert primes.is_prime(30) is False
    assert primes.is_prime(31) is False
    assert primes.is_prime(32) is False
    assert primes.is_prime(33) is False
    assert primes.is_prime(34) is False
    assert primes.is_prime(35) is True

def test_get_primes():
    assert primes.get_primes(1) == []
    assert primes.get_primes(2) == [2]
    assert primes.get_primes(3) == [2, 3]
    assert primes.get_primes(4) == [2, 3]
    assert primes.get_primes(5) == [2, 3, 5]
    assert primes.get_primes(6) == [2, 3, 5]
    assert primes.get_primes(7) == [2, 3, 5, 7]
    assert primes.get_primes(8) == [2, 3, 5, 7]
    assert primes.get_primes(9) == [2, 3, 5, 7]
    assert primes.get_primes(10) == [2, 3, 5, 7]
    assert primes.get_primes(11) == [2, 3, 5, 7, 11]
    assert primes.get_primes(12) == [2, 3, 5, 7, 11]
    assert primes.get_primes(13) == [2, 3, 5, 7, 11, 13]
    assert primes.get_primes(14) == [2, 3, 5, 7, 11, 13]
    assert primes.get_primes(15) == [2, 3, 5, 7, 11, 13, 15]
    assert primes.get_primes(16) == [2, 3, 5, 7, 11, 13, 15]
    assert primes.get_primes(17) == [2, 3, 5, 7, 11, 13, 15, 17]
    assert primes.get_primes(18) == [2, 3, 5, 7, 11, 13, 15, 17]
    assert primes.get_primes(19) == [2, 3, 5, 7, 11, 13, 15, 17, 19]
    assert primes.get_primes(20) == [2, 3, 5, 7, 11, 13, 15, 17, 19]

def test_get_primes_mp():
    assert primes.get_primes_mp(1) == []
    assert primes.get_primes_mp(2) == [2]
    assert primes.get_primes_mp(3) == [2, 3]
    assert primes.get_primes_mp(4) == [2, 3]
    assert primes.get_primes_mp(5) == [2, 3, 5]
    assert primes.get_primes_mp(6) == [2, 3, 5]
    assert primes.get_primes_mp(7) == [2, 3, 5, 7]
    assert primes.get_primes_mp(8) == [2, 3, 5, 7]
    assert primes.get_primes_mp(9) == [2, 3, 5, 7]
    assert primes.get_primes_mp(10) == [2, 3, 5, 7]
    assert primes.get_primes_mp(11) == [2, 3, 5, 7, 11]
    assert primes.get_primes_mp(12) == [2, 3, 5, 7, 11]
    assert primes.get_primes_mp(13) == [2, 3, 5, 7, 11, 13]
    assert primes.get_primes_mp(14) == [2, 3, 5, 7, 11, 13]
    assert primes.get_primes_mp(15) == [2, 3, 5, 7, 11, 13, 15]
    assert primes.get_primes_mp(16) == [2, 3, 5, 7, 11, 13, 15]
    assert primes.get_primes_mp(17) == [2, 3, 5, 7, 11, 13, 15, 17]
    assert primes.get_primes_mp(18) == [2, 3, 5, 7, 11, 13, 15, 17]
    assert primes.get_primes_mp(19) == [2, 3, 5, 7, 11, 13, 15, 17, 19]

if __name__ == "main":
    print("Running tests")
    test_is_prime()
    test_get_primes()
    test_get_primes_mp()
    print("All tests passed")
    print("Running benchmarks")
    primes.benchmark()
    print("Benchmarks complete")
    print("Running benchmarks with multiprocessing")
    primes.benchmark_mp()
    print("Benchmarks complete")