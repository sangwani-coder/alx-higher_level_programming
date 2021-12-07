#!/usr/bin/python
""" Module that defines a node of a singly linked list
"""


class Node:
    """Class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Method to initialise data and Node objects
            Args:
                data (int): integer type
                next_node (Node): A node object
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter to retrive the date """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter to set the data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter to return the next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter to set the next_node in the list """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list """
    def __str__(self):
        res = ""
        ptr = self.__head

        while ptr is not None:
            res += str(ptr.data)
            if ptr.next_node is not None:
                res += "\n"
            ptr = ptr.next_node
        return res

    def __init__(self):
        """initialise objects"""
        self.__head = None

    def sorted_insert(self, value):
        """method to insert new Node into correct sorted
            position in the list (increasing order)
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            prev.next_node = newNode
