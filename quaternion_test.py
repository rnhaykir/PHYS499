import unittest
from quaternion import Quaternions
from math import sqrt

class TestQuaternion(unittest.TestCase):
    
    def test_quaternion_abs(self):
        # Setup
        q1 = Quaternions([1, 1, 2, 1])
        # Method
        abs = q1.__abs__()
        # Expectation
        expected_abs = sqrt(7)
        # Verification
        self.assertEqual(abs, expected_abs)
    
    def test_quaternion_add(self):
        q1 = Quaternions([1, 3, -2, 1])
        q2 = Quaternions([-1, 0, 1, 1])

        sum = q1.__add__(q2)
        expected_sum = Quaternions([0, 3, -1, 2])
        
        sum.__equal__(expected_sum)
        
    def test_quaternion_mul(self):
        q1 = Quaternions([1, -2, -2, 1])
        q2 = Quaternions([-1, 0, 2, 2])

        product = q1.__mul__(q2)
        expected_product = Quaternions([1, -4, 8, -3])
        
        product.__equal__(expected_product)
    
    def test_quaternion_conjugate(self):
        q1 = Quaternions([2, 1, 0.5, -1])
        
        conj = q1.conjugate()
        expected_conj = Quaternions([2, -1, -0.5, 1])
        
        conj.__equal__(expected_conj)
        
    def test_quaternion_inverse(self):
        q1 = Quaternions([-1, 2, 2, -1])
        
        inverse = q1.inverse()
        expected_inverse = Quaternions([-1 / 10, -2 / 10, -2 / 10, 1 / 10])
        
        inverse.__equal__(expected_inverse)
        
    def test_quaternion_quotient(self):
        q1 = Quaternions([1, -1, -2, 1])
        q2 = Quaternions([-1, 0, 4, 2])

        quotient = q1.quotient(q2)
        expected_quotient = Quaternions([-7 / 21, 5 / 21, -4 / 21, 1 / 21])
        
        quotient.__equal__(expected_quotient)

if __name__ == "__main__":
    unittest.main()