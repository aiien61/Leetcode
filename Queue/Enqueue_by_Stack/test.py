import unittest
from exercise1 import MyQueue

class Test(unittest.TestCase):
    def test_enqueue(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        expected: int = 1
        actual: int = q.peek()

        self.assertEqual(expected, actual)

    def test_enqueue_when_queue_is_not_empty(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        expected: bool = False
        actual: bool = q.is_empty()

        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main()
