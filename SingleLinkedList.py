__author__ = 'apassi'

# This class represents a node in a singly linked list.
# It contains two fields data and next
class Node:

    # Initialization function for the Node
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    # Returns a string representation 
    def __str__(self):
        return str(self.data)


# This class represents Single Linked List data structure.
# It uses the Node class and provides basic functionality
# to add, remove, and find elements in a single linked list
class SingleLinkedList:

    # Initialization function for the single linked list
    def __init__(self):
        self.head = None
        self.size = 0

    # Returns string representation of the linked list
    def __str__(self):
        cur = self.head
        list_str = ""
        while cur:
            list_str = list_str + cur.str()
            cur = cur.next
        return list_str

    # Method to insert data item in the front of the list
    # Arg0 : data to be inserted in the list
    def insert_first(self, data):
        cur = self.head
        self.head = Node(data)
        self.head.next = cur
        self.size += 1
        return

    # Method to insert data item at the index provided
    # Arg0 : index location to insert the data
    # Arg1 : data to be inserted in the list
    # Raises IndexError when invalid index is provided
    def insert(self, index, data):

        if index < 0 or index > self.size:
            raise IndexError('Index out of bound')

        count = 0
        cur = self.head

        if index == 0:
            self.insert_first(data)
            return

        while count < index - 1:
            count += 1
            cur = cur.next

        newNode = Node(data)
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1
        return

    # Method to retrieve data at the provided index
    # Arg0 : index location in the list
    # Return : data element at the provided index
    # Raises IndexError when invalid index is provided
    def get(self, index):

        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')

        count = 0
        cur = self.head

        while count < index:
            count += 1
            cur = cur.next

        return cur.data

    # Method to replace the provided item at the desired index location
    # Arg0 : index location in the list
    # Arg1 : data element to be replaced
    # Raises IndexError when invalid index is provided
    def replace(self, index, data):

        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')

        count = 0
        cur = self.head

        while count < index:
            count += 1
            cur = cur.next

        cur.data = data
        return

    # Method to remove the data element at the provided location
    # Arg0 : index location in the list
    # Return : data element that was removed from the list
    # Raises IndexError when invalid index is provided
    def remove(self, index):

        if index < 0 or index >= self.size:
            raise IndexError('Index out of bound')

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

        count = 0
        cur = self.head

        while count < index - 1:
            count += 1
            cur = cur.next

        data = cur.next.data
        cur.next = cur.next.next
        self.size -= 1
        return data

    # Method to retrieve the size of the list
    # Return : size of the list
    def size(self):
        return self.size

