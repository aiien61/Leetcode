from abc import ABC, abstractmethod

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(ABC):
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    @abstractmethod
    def partition_list(self, x):
        raise NotImplementedError
