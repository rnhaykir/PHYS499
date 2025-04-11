from stackAndQueues import Stack, Queue
import unittest

class TestStackandQueue(unittest.TestCase):
    def test_isBalanced(self):
        stack = Stack()
        string1 = "[()]{}{[()()]()}"
        string2 = "[(])"
        expected1 = True
        expected2 = False
        self.assertEqual(stack.__isBalanced__(string1), expected1)
        self.assertEqual(stack.__isBalanced__(string2), expected2)
        
    def test_findMax(self):
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(3)
        queue.enqueue(8)
        queue.enqueue(-1)
        return queue.findMax() == 8
        
    def test_rotate(self):
        initial = Queue()
        expected_queue = Queue()
        for i in [1, 2, 3, 4, 5]:
            initial.enqueue(i)
        for i in [4, 5, 1, 2, 3]:
            expected_queue.enqueue(i)
        return initial.rotate(2) == expected_queue

if __name__ == "__main__":
    unittest.main()