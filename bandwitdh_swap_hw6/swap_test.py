from BinaryTree import BinaryTree, TreeNode
from swap import swap, tree_to_tuple
import unittest

class testSwap(unittest.TestCase):
    
    def test_swap(self):
        initial_tree = BinaryTree()
        for val in [60, 55, 100, 57, 45, 67, 107]:
            initial_tree.insert(val)
            
        output_tree = swap(initial_tree.getRoot())

        expected = (
            60,
            (100, (107, None, None), (67, None, None)),
            (55, (57, None, None), (45, None, None))
        )
        
        self.assertEqual(tree_to_tuple(output_tree), expected)
        
            
if __name__ == '__main__':
    unittest.main()