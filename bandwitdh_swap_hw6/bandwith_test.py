from bandwidth import max_bandwidth
import unittest

class Bandwith_test(unittest.TestCase):
    
    def test_max_bandwith(self):
        intervals = [(3, 6, 13), (4, 8, 5), (5, 9, 6), (7, 11, 12), 
                     (12, 15, 10), (14, 20, 19), (16, 19, 3)]
        
        output = max_bandwidth(intervals)
        expected = (14.5, 29)
        self.assertEqual(output, expected)
        
        
if __name__ == '__main__':
    unittest.main()