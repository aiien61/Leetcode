import unittest
from exercise1 import SolutionList
from typing import List

def linkedlist_to_list(head) -> List[int]:
    result_values = []
    node = head
    while node:
        result_values.append(node.value)
        node = node.next
    return result_values


class TestReverseBetween(unittest.TestCase):
    def test_reverse_between_when_reverse_sublist_within_list(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.reverse_between(2, 4)

        expected = [1, 2, 5, 4, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_between_when_reverse_another_sublist_within_list(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.reverse_between(2, 4)
        ll.reverse_between(0, 4)

        expected = [3, 4, 5, 2, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_between_when_reverse_sublist_of_length_1_within_list(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.reverse_between(3, 3)

        expected = [1, 2, 3, 4, 5]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_between_when_reverse_empty_list(self):
        ll = SolutionList(0)
        ll.make_empty()
        ll.reverse_between(0, 0)

        expected = []
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_reverse_between_when_reverse_entire_list(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        ll.reverse_between(0, 4)

        expected = [5, 4, 3, 2, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
