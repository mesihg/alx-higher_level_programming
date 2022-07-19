#!/usr/bin/python3

"""Singly-linked list Entity"""


class Node:
    """A class to represent a node in a single linked list"""

    def __init__(self, data, next_node=None):
        """Initialize node instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return the node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the node data with a new value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next_node with a new value the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class to represent a single linked list"""

    def __init__(self):
        """Initialize a single linked list instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new value to the singly-linked list"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """str representation of singly-linked list"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
