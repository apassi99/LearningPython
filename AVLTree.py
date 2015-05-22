__author__ = 'apassi'

class InvalidArgumentException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# This class represents a node in an AVL Tree.
# It
class AVLTreeNode:

    # Initialization Function for AVLTreeNode
    # Four member variables
    #   left - left child of the node
    #   right - right child of the node
    #   data - data contained in the node
    #   height - height of the node
    def __init__(self, data = None, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
        self.height = 0

    # Returns the string representation of AVLTreeNode
    def __str__(self):
        return str(self.data)

# This class implements AVL Tree. It is a self balancing search tree
# In this implementation duplicates are not allowed!
class AVLTree:

    # Initialization function for AVL Tree
    # Two member variables
    #   root - root of the AVL search tree
    #   size - size of the AVL search tree
    def __init__(self):
        self.root = None
        self.size = 0

    # Method to retrieve the size of the AVLTree
    # Return : size of the tree
    def size(self):
        return self.size

    # Method to insert data in the AVL TREE
    # Arg0 : data to be inserted
    # Raises InvalidArgumentException when invalid data is provided
    # data is invalid if it's None or already present in the tree
    def insert(self, data):

        if data is None:
            raise InvalidArgumentException("data is null")

        self.root = self.__insert_helper(self.root, data)
        return

    # Method to search provided data in the AVLTree
    # Arg0 : AVLTree node
    # data : data to search in the tree
    # Return : True if data present in the tree otherwise False
    def contains(self, data):

        if data is None:
            raise InvalidArgumentException("data is null")

        return self.__contains_helper(self.root, data)

    # Method to remove the specified data from the tree
    # Arg0 : data item to be removed
    # Raises InvalidArgumentException when invalid data is provided
    def remove(self, data):

        if data is None:
            raise InvalidArgumentException("data is null")

        self.root = self.__remove_helper(self.root, data)

    # Helper method to recursively remove specified data element
    # in the tree
    # Arg0 : AVLTreeNode from where to start finding the data element
    # Arg0 : data element to be removed
    # Return : AVLTreeNode to reorganize the tree
    def __remove_helper(self, node, data):

        if node is None:
            return node

        if data > node.data:
            node.right = self.__remove_helper(node.right, data)
        elif data < node.data:
            node.left = self.__remove_helper(node.left, data)
        else:
            return self.__remove_node_helper(node)

        node.height = max(self.__height(node.left), self.__height(node.right)) + 1
        node = self.__perform_rotation(node)

        return node

    # Helper method to remove the specified AVLTreeNode from the tree
    # Arg0 : node to be removed
    # Return : node to reorganize the tree
    def __remove_node_helper(self, node):

        if node is None:
            return node

        if node.left is None and node.right is None:
            self.size -= 1
            return None
        elif node.left is None and node.right is not None:
            self.size -= 1
            return node.right
        elif node.left is not None and node.right is None:
            self.size -= 1
            return node.left
        else:
            copy_data = self.__find_min(node.right)
            node = self.__remove_helper(node, copy_data)
            node.data = copy_data
            return node


    # Helper method to iteratively find the minimum
    # in the AVLTree
    # Arg0 : AVLTree node
    # Return : minimum data element
    def __find_min(self, node):

        cur_node = node
        while cur_node.left is not None:
            cur_node = cur_node.left

        return cur_node.data

    # Helper method to recursively search the provided data
    # item in the AVLTree
    # Arg0 : AVLTree node
    # data : data to search in the tree
    # Return : True if data present in the tree otherwise False
    def __contains_helper(self, node, data):

        if node is None:
            return False

        if node.data == data:
            return True
        elif data > node.data:
            return self.__contains_helper(node.right, data)
        else:
            return self.__contains_helper(node.left, data)

    # Recursive helper method to insert data in the AVL Tree
    # Arg0 : AVLTree node
    # Arg1 : data to be inserted
    def __insert_helper(self, node, data):

        if node is None:
            new_node = AVLTreeNode(data)
            self.size += 1
            return new_node

        if data > node.data:
            node.right = self.__insert_helper(node.right, data)

        elif data < node.data:
            node.left = self.__insert_helper(node.left, data)
        else:
            raise InvalidArgumentException("data already present")

        node.height = max(self.__height(node.left), self.__height(node.right)) + 1
        node = self.__perform_rotation(node)
        return node

    # Helper method that performs a rotation depending on the
    # height of the sub tree node provided
    # Arg0 : AVLTree node
    # Return : rotated sub tree root
    def __perform_rotation(self, node):

        if node is None:
            return None

        if abs(self.__difference(node)) <= 1:
            return node

        if self.__difference(node) == 2 and self.__difference(node.left) == 1:
            node = self.__right_rotate_left_child(node)

        elif self.__difference(node) == -2 and self.__difference(node.right) == -1:
            node = self.__left_rotate_right_child(node)

        elif self.__difference(node) == -2 and self.__difference(node.right) == 1:
            node.right = self.__right_rotate_left_child(node.right)
            node = self.__left_rotate_right_child(node)
        else:
            node.left = self.__left_rotate_right_child(node.left)
            node = self.__right_rotate_left_child(node)

        return node

    # Helper method to perform right rotation on left child
    # This rotation must be performed whenever left_height - right_height
    # is greater than 1
    # Arg0 : AVLTree node
    # Return : rotated sub tree root
    def __right_rotate_left_child(self, node):

        if node is None or node.left is None:
            return node

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Adjusting heights
        new_root.height = max(self.__height(new_root.left), self.__height(new_root.right)) + 1
        node.height = max(self.__height(node.left), self.__height(node.right)) + 1

        return new_root

    # Helper method to perform left rotation on right child
    # This rotation must be performed whenever right_height - left_height
    # is greater than 1
    # Arg0 : AVLTree node
    # Return : rotated sub tree root
    def __left_rotate_right_child(self, node):

        if node is None or node.right is None:
            return node

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        # Adjusting heights
        new_root.height = max(self.__height(new_root.left), self.__height(new_root.right)) + 1
        node.height = max(self.__height(node.left), self.__height(node.right)) + 1

        return new_root

    # Helper method to return the difference of the left height
    # and right height
    # Arg0 : AVLTree node
    # Return : height difference of left and right tree
    def __difference(self, node):

        if node is None:
            return 0
        else:
            return self.__height(node.left) - self.__height(node.right)

    # Helper method to retrieve the height of the node
    # Arg0 : AVLTree node
    # Return : height of that node
    def __height(self, node):
        if node is None:
            return -1
        else:
            return node.height

