# unittest for prime-faster.py

from turtle import end_fill
import unittest
import primefaster

class TestPrimeFaster(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(primefaster.is_prime(2))
        self.assertTrue(primefaster.is_prime(3))
        self.assertTrue(primefaster.is_prime(5))
        self.assertTrue(primefaster.is_prime(7))
        self.assertTrue(primefaster.is_prime(11))
        self.assertTrue(primefaster.is_prime(13))
        self.assertTrue(primefaster.is_prime(17))
        self.assertTrue(primefaster.is_prime(19))
        self.assertTrue(primefaster.is_prime(23))
        self.assertTrue(primefaster.is_prime(29))
        self.assertTrue(primefaster.is_prime(31))
        self.assertTrue(primefaster.is_prime(37))
        self.assertTrue(primefaster.is_prime(41))
        self.assertTrue(primefaster.is_prime(43))
        self.assertTrue(primefaster.is_prime(47))
        self.assertTrue(primefaster.is_prime(53))
        self.assertTrue(primefaster.is_prime(59))
        self.assertTrue(primefaster.is_prime(61))
        self.assertTrue(primefaster.is_prime(67))
        self.assertTrue(primefaster.is_prime(71))
        self.assertTrue(primefaster.is_prime(73))
        self.assertTrue(primefaster.is_prime(79))
        self.assertTrue(primefaster.is_prime(83))
        self.assertTrue(primefaster.is_prime(89))
        self.assertTrue(primefaster.is_prime(97))
        self.assertTrue(primefaster.is_prime(101))
        self.assertTrue(primefaster.is_prime(103))
        self.assertTrue(primefaster.is_prime(107))
        self.assertTrue(primefaster.is_prime(109))
        self.assertTrue(primefaster.is_prime(113))

    def test_get_prime_faster(self):
        self.assertEqual(primefaster.get_prime(1), [])
        self.assertEqual(primefaster.get_prime(2), [2])
        self.assertEqual(primefaster.get_prime(3), [2, 3])
        self.assertEqual(primefaster.get_prime(4), [2, 3])
        self.assertEqual(primefaster.get_prime(5), [2, 3, 5])
        self.assertEqual(primefaster.get_prime(6), [2, 3, 5])
        self.assertEqual(primefaster.get_prime(7), [2, 3, 5, 7])
        self.assertEqual(primefaster.get_prime(8), [2, 3, 5, 7])
        self.assertEqual(primefaster.get_prime(9), [2, 3, 5, 7])
        self.assertEqual(primefaster.get_prime(10), [2, 3, 5, 7])
        self.assertEqual(primefaster.get_prime(11), [2, 3, 5, 7, 11])
        self.assertEqual(primefaster.get_prime(12), [2, 3, 5, 7, 11])
        self.assertEqual(primefaster.get_prime(13), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primefaster.get_prime(14), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primefaster.get_prime(15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primefaster.get_prime(16), [2, 3, 5, 7, 11, 13])
        self.assertEqual(primefaster.get_prime(17), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(primefaster.get_prime(18), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(primefaster.get_prime(19), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
    end_fill()
    exit()

