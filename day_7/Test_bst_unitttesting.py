import unittest
from . BinarySearchTree import BinarySearchTree

class Test_bst(unittest.TestCase):

    def setUp(self):
        bst = BinarySearchTree()
        bst.put(21, "a")
        bst.put(18, "b")
        bst.put(10, "c")
        bst.put(40, "d")
        bst.put(8, "e")
        bst.put(11, "f")

    def test_get(self):
        self.assertEqual("f", bst.get(11))

if __name__ == '__main__':
    unittest.main()

main()
