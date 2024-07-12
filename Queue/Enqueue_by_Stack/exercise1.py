from base import Queue

class MyQueue(Queue):
    def enqueue(self, value: int):
        if not self.stack1:
            self.stack1.append(value)
            return True
        
        while self.stack1:
            self.stack2.append(self.stack1.pop(-1))
        
        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop(-1))

        return True
