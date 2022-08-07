# unittest for primes.py

from turtle import end_fill
import unittest
import primes

class TestPrimes(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(primes.is_prime(2))
        self.assertTrue(primes.is_prime(3))
        self.assertTrue(primes.is_prime(5))
        self.assertTrue(primes.is_prime(7))
        self.assertTrue(primes.is_prime(11))
        self.assertTrue(primes.is_prime(13))
        self.assertTrue(primes.is_prime(17))
        self.assertTrue(primes.is_prime(19))
        self.assertTrue(primes.is_prime(23))
        self.assertTrue(primes.is_prime(29))
        self.assertTrue(primes.is_prime(31))
        self.assertTrue(primes.is_prime(37))
        self.assertTrue(primes.is_prime(41))
        self.assertTrue(primes.is_prime(43))
        self.assertTrue(primes.is_prime(47))
        self.assertTrue(primes.is_prime(53))
        self.assertTrue(primes.is_prime(59))
        self.assertTrue(primes.is_prime(61))
        self.assertTrue(primes.is_prime(67))
        self.assertTrue(primes.is_prime(71))
        self.assertTrue(primes.is_prime(73))
        self.assertTrue(primes.is_prime(79))
        self.assertTrue(primes.is_prime(83))
        self.assertTrue(primes.is_prime(89))
        self.assertTrue(primes.is_prime(97))
        self.assertTrue(primes.is_prime(101))
        self.assertTrue(primes.is_prime(103))
        self.assertTrue(primes.is_prime(107))
        self.assertTrue(primes.is_prime(109))
        self.assertTrue(primes.is_prime(113))

    def test_get_primes(self):
        self.assertEqual(primes.get_primes(1), [])
        self.assertEqual(primes.get_primes(2), [2])
        self.assertEqual(primes.get_primes(3), [2, 3])
        self.assertEqual(primes.get_primes(4), [2, 3])
        self.assertEqual(primes.get_primes(5), [2, 3, 5])
        self.assertEqual(primes.get_primes(6), [2, 3, 5])
        self.assertEqual(primes.get_primes(7), [2, 3, 5, 7])
        self.assertEqual(primes.get_primes(8), [2, 3, 5, 7])
        self.assertEqual(primes.get_primes(9), [2, 3, 5, 7])
        self.assertEqual(primes.get_primes(10), [2, 3, 5, 7])
        self.assertEqual(primes.get_primes(11), [2, 3, 5, 7, 11])
        self.assertEqual(primes.get_primes(12), [2, 3, 5, 7, 11])
        self.assertEqual(primes.get_primes(13), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primes.get_primes(14), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primes.get_primes(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primes.get_primes(16), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primes.get_primes(17), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(primes.get_primes(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()
    end_fill()
    exit()

