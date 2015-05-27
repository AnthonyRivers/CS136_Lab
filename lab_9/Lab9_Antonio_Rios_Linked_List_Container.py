# Antonio Rios
# April 10, 2015
# Lab 9 - Linked List Containers
# ==============================

from linkedlists import *

class LinkedListContainer(LinkedList, NodeSingle):
    """
    The LinkedListContainer class subclasses the LinkedList class and the NodeSingle
    class. This class implements the custom functionality for the default
    operations of gettig an item on a list by index,
    assigning a value by index on a list, and deleting an item of the list.

    -> lst[2]
    -> lst[0] = 'x'
    -> del lst[1]
    """

    def __init__(self):
        """
        Constructor of the LinkedListContainer calls the Super class
        to initialize it.
        """
        super().__init__()

    def __getitem__(self, key):
        """
        This method implements the custom functionality of returning
        an item from the linked list by using the key pass in the call.

        Ex: lst[2]

        parameters: This method takes key value as a parameter. It should be
        an integer which represents the index of the item in the linked list.

        returns: This method returns the contents of the location in the linked list
        which was determine by using the key.
        """
        if key + 1 > len(self):    # check if key is out beyond the length of the linked list
            raise IndexError       # if it is beyond the length then raise an IndexError exception

        node = self._first         # otherwise assign the value of self._first to the local variable node
                                   # self._first is inherited from LinkedList

        for i in range(0, key):    # loop through the linked list from 0 to the key passed in
            node = node._next      # assign the next node to node

        return node._contents      # return the node's contents

    def __setitem__(self, key, value):
        """
            The setitem method implements the functionality to assign a value
            in the linked list.

            This method is executed when an item is added to the linked list.
            Ex: lst[0] = 'x'

            parameters: A key and a value is passed to this method.
            The value is stored in the position that the key represents in the
            linked list as an index.

            return: This method returns nothing
        """
        if key + 1 > len(self):     # check if the key is out of range in the linked list
            raise IndexError        # if it is raise an IndexError exception

        node = self._first          # else store the value in self._first in node

        for i in range(0, key):     # loop through the linked list and find the position
                                    # where the value will be stored
            node = node._next

        node._contents = value      # assigned the value passs in to the method to
                                    # override the value in the node

    def __delitem__(self, key):
        """
            The delitem method implements the functionality to delete an item
            from the linked list.

            This method is called when the keyword del is used to delete an item.
            Ex: del lst[2]

            parameters: A key is passed in to this method which represents the index
            of the item in the linked list.

            returns: This method returns nothing.
        """
        if key + 1 > len(self):     # Check if the key is out of range
            raise IndexError        # if it is the Index Error exception is raised
        node = self._first          # else the value in self._first is assign to node

        # check if the key passed in is 0
        # if it is store the reference of the next node
        # which will become the first node in the linked list
        if key == 0:
            temp = node
            self._first = node._next    # assigns the next node to be the first item in the linked list
            temp._next = None           # deletes the first item in the linked list by pointing to None

        # if the key is not zero then the following
        # code is executed
        else:
            # loop through the linked list and find the position of the item that
            # will get deleted
            for i in range(0, key - 1):
                node = node._next       # get the reference of the next node to the node that we want to delete

            temp = node._next       # store the reference of the next node

            # check if the item to be deleted is the last item in the linked list
            if key == len(self) - 1:
                node._next = None       # deletes the last item in the liked list

            else:
                # store the reference of the node next to the one that will get deleted
                node._next = node._next._next

            temp._next = None       # sets the reference None to delete the item from the linked list




# TEST CODE
# create a linked list and add two elements
ll = LinkedListContainer()
print("Testing add_first")
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)
ll.add_first(4)
ll.add_first(5)
print(ll)

print("Testing the __getitem__ method")
print("ll[1]:", ll[1])
print("ll[2]:", ll[2])
print()
print("Testing the __setitem__ method")
print("ll[1] = 10 "); ll[1] = 10
print("ll[2] = 23 "); ll[2] = 23
print(ll)

print()

print("Testing the __delitem__ method")
print("del ll[1]"); del ll[1]
print("del ll[2]"); del ll[2]
print(ll)
#del ll[4]


