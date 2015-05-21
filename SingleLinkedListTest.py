__author__ = 'apassi'
import unittest
from SingleLinkedList import SingleLinkedList

class SingleLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.list = SingleLinkedList()

    def test_size(self):
        self.assertEqual(self.list.size, 0, "Incorrect list size")
        self.list.insert_first(1)
        self.list.insert_first(2)
        self.assertEqual(self.list.size, 2, "Incorrect list size")

if __name__ == '__main__':
    unittest.main()
