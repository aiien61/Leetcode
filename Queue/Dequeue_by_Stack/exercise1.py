from base import Queue

class MyQueue(Queue):
    def dequeue(self):
        if self.stack1:
            return self.stack1.pop(-1)
        return None
