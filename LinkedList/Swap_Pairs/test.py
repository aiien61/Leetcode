from __future__ import annotations
import unittest
from typing import List
from exercise1 import SolutionList

def linkedlist_to_list(head) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

class TestSwapPairs(unittest.TestCase):

    def test_swap_pairs_when_list_is_empty(self):
        ll = SolutionList(None)
        ll.head = None
        ll.length = 0

        ll.swap_pairs()

        expected: List[int] = []
        actual: List[int] = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_pairs_when_list_has_only_one_node(self):
        ll = SolutionList(1)

        ll.swap_pairs()

        expected: List[int] = [1]
        actual: List[int] = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_pairs_when_list_has_only_two_nodes(self):
        ll = SolutionList(1)
        ll.append(2)

        ll.swap_pairs()

        expected: List[int] = [2, 1]
        actual: List[int] = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_swap_pairs_when_list_odd_nodes(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.swap_pairs()

        expected: List[int] = [2, 1, 4, 3, 5]
        actual: List[int] = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)


    def test_swap_pairs_when_list_even_nodes(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)

        ll.swap_pairs()

        expected: List[int] = [2, 1, 4, 3]
        actual: List[int] = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
