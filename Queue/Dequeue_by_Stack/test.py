import unittest
from exercise1 import MyQueue
from typing import Any, List

class Test(unittest.TestCase):
    def test_dequeue_from_empty_queue(self):
        q = MyQueue()
        expected: Any = None
        actual: Any = q.dequeue()
        self.assertEqual(expected, actual)

    def test_dequeue_multiple_values(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        
        for _ in range(2):
            q.dequeue()

        actual: int = q.dequeue()
        expected: int = 3
        self.assertEqual(expected, actual)

    def test_dequeue_order(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        expected: List[int] = [1, 2, 3]
        actual: List[int] = [q.dequeue() for _ in range(3)]
        self.assertEqual(expected, actual)

    def test_dequeue_single_value(self):
        q = MyQueue()
        q.enqueue(1)

        expected: int = 1
        actual: int = q.dequeue()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()