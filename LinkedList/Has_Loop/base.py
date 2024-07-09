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
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    @abstractmethod
    def has_loop(self):
        raise NotImplementedError
