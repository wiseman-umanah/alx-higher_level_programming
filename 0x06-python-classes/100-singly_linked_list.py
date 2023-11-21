#!/usr/bin/python3
class SinglyLinkedList:
    def __init__(self, data, next_node=None):
        self.next_node = next_node
        self.__data = data
