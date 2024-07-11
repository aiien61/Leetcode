import unittest
from base import Stack
from exercise1 import sort_stack
from typing import List

def stack_to_list(stack: Stack) -> List[int]:
    result: List[int] = []
    while not stack.is_empty():
        result.append(stack.pop())
    return result


class TestSortStack(unittest.TestCase):
    def test_sort_stack_when_mix_ordered_stack(self):
        my_stack = Stack()
        my_stack.push(3)
        my_stack.push(10)
        my_stack.push(15)
        my_stack.push(1)
        my_stack.push(20)

        sort_stack(my_stack)

        expected: List[int] = [1, 3, 10, 15, 20]
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_unsorted_stack(self):
        my_stack = Stack()
        my_stack.push(3)
        my_stack.push(1)
        my_stack.push(5)
        my_stack.push(4)
        my_stack.push(2)

        sort_stack(my_stack)

        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_reverse_sorted_stack(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        my_stack.push(5)

        sort_stack(my_stack)

        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_sorted_stack(self):
        my_stack = Stack()
        my_stack.push(5)
        my_stack.push(4)
        my_stack.push(3)
        my_stack.push(2)
        my_stack.push(1)

        sort_stack(my_stack)

        expected: List[int] = [1, 2, 3, 4, 5]
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_empty_stack(self):
        my_stack = Stack()

        sort_stack(my_stack)

        expected: List[int] = []
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_single_element_stack(self):
        my_stack = Stack()
        my_stack.push(1)

        sort_stack(my_stack)

        expected: List[int] = [1]
        actual: List[int] = stack_to_list(my_stack)

        self.assertEqual(expected, actual)

    def test_sort_stack_when_duplicate_element_stack(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(3)
        my_stack.push(1)

        sort_stack(my_stack)

        expected: List[int] = [1, 1, 3]
        actual: List[int] = stack_to_list(my_stack)


if __name__ == '__main__':
    unittest.main()