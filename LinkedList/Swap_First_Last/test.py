import unittest
from exercise1 import SolutionList
from typing import List

def linkedlist_to_list(head) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

class TestSwapFirstLast(unittest.TestCase):
    def test_swap_first_last_when_multiple_nodes(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)

        ll.swap_first_last()

        expected = [4, 2, 3, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_first_last_when_single_node(self):
        ll = SolutionList(1)

        ll.swap_first_last()

        expected = [1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_first_last_when_list_is_empty(self):
        ll = SolutionList(None)
        ll.head = None
        ll.length = 0

        ll.swap_first_last()

        expected = []
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_first_last_when_two_node(self):
        ll = SolutionList(1)
        ll.append(2)

        ll.swap_first_last()

        expected = [2, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()