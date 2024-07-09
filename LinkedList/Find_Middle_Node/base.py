from __future__ import annotations
from abc import ABC, abstractmethod

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(ABC):
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    @abstractmethod
    def find_middle_node(self):
        raise NotImplementedError
