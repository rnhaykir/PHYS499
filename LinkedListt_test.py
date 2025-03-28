import unittest
from LinkedListt import LinkedList

class testLinkedList(unittest.TestCase):
    
    def test_intersection(self):
        L1 = LinkedList()
        L2 = LinkedList()
        expected_intersection = LinkedList()
        for i in [2, 4, 8, 12, 20, 46]:
            L1.addLast(i)
        for i in [1, 4, 12, 35, 72]:
            L2.addLast(i)
        for i in [4, 12]:
            expected_intersection.addLast(i)
        L3 = L1.intersection(L2)
        L3.__isequal__(expected_intersection)
    
    def test_union(self):
        L1 = LinkedList()
        L2 = LinkedList()
        expected_union = LinkedList()
        for i in [2, 4, 8, 12, 20, 46]:
            L1.addLast(i)
        for i in [1, 4, 12, 35, 72]:
            L2.addLast(i)
        for i in [1, 2, 4, 8, 12, 20, 35, 46, 72]:
            expected_union.addLast(i)
        L3 = L1.union(L2)
        L3.__isequal__(expected_union)
    
if __name__ == "__main__":
    unittest.main()