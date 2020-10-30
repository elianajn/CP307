import unittest
from datastructures.BinarySearchTree import BinarySearchTree

class Test_bst(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.put(21, "a")
        self.bst.put(18, "b")
        self.bst.put(10, "c")
        self.bst.put(40, "d")
        self.bst.put(8, "e")
        self.bst.put(11, "f")

    def test_get(self):
        self.assertEqual("b", self.bst.get(18))
        self.assertEqual("c", self.bst.get(10))
        self.assertEqual("a", self.bst.get(21))
        self.assertEqual("d", self.bst.get(40))
        self.assertEqual("e", self.bst.get(8))
        self.assertEqual("f", self.bst.get(11))

    def test_size(self):
        self.assertEqual(6, self.bst.size())
        self.bst.delete(8)
        self.assertEqual(5, self.bst.size())

    def test_hasKey(self):
        self.assertEqual(True, self.bst.hasKey(11))
        self.assertEqual(False, self.bst.hasKey(7))

if __name__ == '__main__':
    unittest.main()

main()
