from abc import ABC, abstractmethod

class Queue(ABC):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    @abstractmethod
    def enqueue(self, value):
        raise NotImplementedError
    
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
