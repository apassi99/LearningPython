__author__ = 'apassi'
import unittest
from AVLTree import AVLTree, InvalidArgumentException


class AVLTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    # Method to test insert function of AVLTree
    def test_insert(self):

        self.assertEqual(self.tree.size, 0, "Incorrect tree size")

        self.tree.insert(100)
        self.assertEqual(self.tree.size, 1, "Incorrect tree size")

        self.assertRaises(InvalidArgumentException, self.tree.insert, 100)

        self.tree.insert(150)
        self.assertEqual(self.tree.size, 2, "Incorrect tree size")

        self.tree.insert(50)
        self.assertEqual(self.tree.size, 3, "Incorrect tree size")

        self.tree.insert(200)
        self.tree.insert(125)

        self.tree.remove(100)
        self.assertEqual(self.tree.size, 4, "Incorrect tree size " + str(self.tree.size))

        self.tree.remove(200)
        self.assertEqual(self.tree.size, 3, "Incorrect tree size " + str(self.tree.size))

        self.tree.remove(125)
        self.assertEqual(self.tree.size, 2, "Incorrect tree size " + str(self.tree.size))

        self.tree.remove(50)
        self.assertEqual(self.tree.size, 1, "Incorrect tree size " + str(self.tree.size))

        self.tree.remove(150)
        self.assertEqual(self.tree.size, 0, "Incorrect tree size " + str(self.tree.size))

    # Method to test contains function of AVLTree
    def test_contains(self):
        self.assertFalse(self.tree.contains(100))
        self.assertFalse(self.tree.contains(50))
        self.assertFalse(self.tree.contains(-50))

        self.tree.insert(100)
        self.assertTrue(self.tree.contains(100))

        self.tree.insert(150)
        self.assertTrue(self.tree.contains(100))
        self.assertTrue(self.tree.contains(150))

        self.tree.insert(50)
        self.assertTrue(self.tree.contains(100))
        self.assertTrue(self.tree.contains(150))
        self.assertTrue(self.tree.contains(50))

        self.tree.remove(100)
        self.assertFalse(self.tree.contains(100))
        self.assertTrue(self.tree.contains(150))
        self.assertTrue(self.tree.contains(50))

        self.tree.remove(150)
        self.tree.remove(50)
        self.assertFalse(self.tree.contains(150))
        self.assertFalse(self.tree.contains(50))

        for i in range(1, 100):
            self.tree.insert(i)
            self.assertTrue(self.tree.contains(i))

        for i in range(1, 100):
            self.tree.remove(i)
            self.assertFalse(self.tree.contains(i))

if __name__ == '__main__':
    unittest.main()