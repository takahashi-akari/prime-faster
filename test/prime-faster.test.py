# unittest for prime-faster.py

from turtle import end_fill
import unittest
import prime-faster

class Testprime-faster(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(prime-faster.is_prime(2))
        self.assertTrue(prime-faster.is_prime(3))
        self.assertTrue(prime-faster.is_prime(5))
        self.assertTrue(prime-faster.is_prime(7))
        self.assertTrue(prime-faster.is_prime(11))
        self.assertTrue(prime-faster.is_prime(13))
        self.assertTrue(prime-faster.is_prime(17))
        self.assertTrue(prime-faster.is_prime(19))
        self.assertTrue(prime-faster.is_prime(23))
        self.assertTrue(prime-faster.is_prime(29))
        self.assertTrue(prime-faster.is_prime(31))
        self.assertTrue(prime-faster.is_prime(37))
        self.assertTrue(prime-faster.is_prime(41))
        self.assertTrue(prime-faster.is_prime(43))
        self.assertTrue(prime-faster.is_prime(47))
        self.assertTrue(prime-faster.is_prime(53))
        self.assertTrue(prime-faster.is_prime(59))
        self.assertTrue(prime-faster.is_prime(61))
        self.assertTrue(prime-faster.is_prime(67))
        self.assertTrue(prime-faster.is_prime(71))
        self.assertTrue(prime-faster.is_prime(73))
        self.assertTrue(prime-faster.is_prime(79))
        self.assertTrue(prime-faster.is_prime(83))
        self.assertTrue(prime-faster.is_prime(89))
        self.assertTrue(prime-faster.is_prime(97))
        self.assertTrue(prime-faster.is_prime(101))
        self.assertTrue(prime-faster.is_prime(103))
        self.assertTrue(prime-faster.is_prime(107))
        self.assertTrue(prime-faster.is_prime(109))
        self.assertTrue(prime-faster.is_prime(113))

    def test_get_prime-faster(self):
        self.assertEqual(prime-faster.get_prime-faster(1), [])
        self.assertEqual(prime-faster.get_prime-faster(2), [2])
        self.assertEqual(prime-faster.get_prime-faster(3), [2, 3])
        self.assertEqual(prime-faster.get_prime-faster(4), [2, 3])
        self.assertEqual(prime-faster.get_prime-faster(5), [2, 3, 5])
        self.assertEqual(prime-faster.get_prime-faster(6), [2, 3, 5])
        self.assertEqual(prime-faster.get_prime-faster(7), [2, 3, 5, 7])
        self.assertEqual(prime-faster.get_prime-faster(8), [2, 3, 5, 7])
        self.assertEqual(prime-faster.get_prime-faster(9), [2, 3, 5, 7])
        self.assertEqual(prime-faster.get_prime-faster(10), [2, 3, 5, 7])
        self.assertEqual(prime-faster.get_prime-faster(11), [2, 3, 5, 7, 11])
        self.assertEqual(prime-faster.get_prime-faster(12), [2, 3, 5, 7, 11])
        self.assertEqual(prime-faster.get_prime-faster(13), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime-faster.get_prime-faster(14), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime-faster.get_prime-faster(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime-faster.get_prime-faster(16), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime-faster.get_prime-faster(17), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(prime-faster.get_prime-faster(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()
    end_fill()
    exit()

