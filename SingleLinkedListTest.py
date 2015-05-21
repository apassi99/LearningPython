__author__ = 'apassi'
import unittest
from SingleLinkedList import SingleLinkedList

# This class implements test functions for all the
# methods provided by SingleLinkedList class
class SingleLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.list = SingleLinkedList()

    # Method to test the size method
    def test_size(self):
        self.assertEqual(self.list.size, 0, "Incorrect list size")
        self.list.insert_first(1)
        self.list.insert_first(2)
        self.assertEqual(self.list.size, 2, "Incorrect list size")

        self.list.insert_first(3)

        self.list.remove(2)
        self.assertEqual(self.list.size, 2, "Incorrect list size")

        self.list.remove(1)
        self.assertEqual(self.list.size, 1, "Incorrect list size")

        self.list.remove(0)
        self.assertEqual(self.list.size, 0, "Incorrect list size")

    # Method to test insert_first method
    def test_insert_first(self):
        self.assertRaises(IndexError, self.list.get, 0)
        self.assertRaises(IndexError, self.list.get, 1)
        self.assertRaises(IndexError, self.list.get, -1)

        self.list.insert_first(1)
        self.assertEqual(self.list.get(0), 1)

        self.list.insert_first(2)
        self.assertEqual(self.list.get(0), 2)
        self.assertEqual(self.list.get(1), 1)

        self.list.insert_first(3)
        self.assertEqual(self.list.get(0), 3)
        self.assertEqual(self.list.get(1), 2)
        self.assertEqual(self.list.get(2), 1)

    # Method ot test insert method
    def test_insert(self):
        self.assertRaises(IndexError, self.list.insert, 1, 1)
        self.assertRaises(IndexError, self.list.insert, 12, 1)
        self.assertRaises(IndexError, self.list.insert, -10, 1)

        self.list.insert(0, 1)
        self.assertEqual(self.list.get(0), 1)

        self.assertRaises(IndexError, self.list.insert, 12, 1)
        self.assertRaises(IndexError, self.list.insert, -10, 1)

        self.list.insert(1, 3)
        self.assertEqual(self.list.get(0), 1)
        self.assertEqual(self.list.get(1), 3)

        self.assertRaises(IndexError, self.list.insert, 12, 1)
        self.assertRaises(IndexError, self.list.insert, -10, 1)

        self.list.insert(2, 4)
        self.assertEqual(self.list.get(0), 1)
        self.assertEqual(self.list.get(1), 3)
        self.assertEqual(self.list.get(2), 4)

        self.assertRaises(IndexError, self.list.insert, 12, 1)
        self.assertRaises(IndexError, self.list.insert, -10, 1)

        self.list.insert(1, -1)
        self.assertEqual(self.list.get(0), 1)
        self.assertEqual(self.list.get(1), -1)
        self.assertEqual(self.list.get(2), 3)
        self.assertEqual(self.list.get(3), 4)

        self.assertRaises(IndexError, self.list.insert, 12, 1)
        self.assertRaises(IndexError, self.list.insert, -10, 1)

    # Method to test replace method
    def test_replace(self):
        self.assertRaises(IndexError, self.list.replace, 1, 1)
        self.assertRaises(IndexError, self.list.replace, 0, 1)
        self.assertRaises(IndexError, self.list.replace, -4, 1)

        self.list.insert(0, 1)
        self.list.replace(0, 5)
        self.assertEqual(self.list.get(0), 5)

        self.list.insert(1, 10)
        self.list.replace(0, -5)
        self.assertEqual(self.list.get(0), -5)

        self.list.replace(0, 4)
        self.assertEqual(self.list.get(0), 4)

    # Method to test remove method
    def test_remove(self):
        self.assertRaises(IndexError, self.list.remove, 1)
        self.assertRaises(IndexError, self.list.remove, 0)
        self.assertRaises(IndexError, self.list.remove, -4)

        self.list.insert(0, 1)
        self.assertEqual(self.list.remove(0), 1)
        self.assertEqual(self.list.size, 0, "Incorrect list size")

        self.list.insert(0, 1)
        self.list.insert(1, 5)
        self.list.insert(2, 10)

        self.assertEqual(self.list.remove(2), 10)
        self.assertEqual(self.list.size, 2, "Incorrect list size")

        self.assertEqual(self.list.remove(1), 5)
        self.assertEqual(self.list.size, 1, "Incorrect list size")

        self.assertEqual(self.list.remove(0), 1)
        self.assertEqual(self.list.size, 0, "Incorrect list size")

if __name__ == '__main__':
    unittest.main()
