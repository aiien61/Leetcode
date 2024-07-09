import unittest
from typing import List
from exercise1 import SolutionList

def linkedlist_to_list(head) -> List[int]:
    result_values = []
    node = head
    while node:
        result_values.append(node.value)
        node = node.next
    return result_values

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_when_no_duplicates(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.remove_duplicates()

        expected =[1, 2, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_some_duplicates(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(1)
        ll.append(3)
        ll.append(2)
        ll.remove_duplicates()

        expected = [1, 2, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_all_duplicates(self):
        ll = SolutionList(1)
        ll.append(1)
        ll.append(1)
        ll.remove_duplicates()

        expected = [1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_consecutive_duplicates(self):
        ll = SolutionList(1)
        ll.append(1)
        ll.append(2)
        ll.append(2)
        ll.append(3)
        ll.remove_duplicates()

        expected = [1, 2, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_non_consecutive_duplicates(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(1)
        ll.append(3)
        ll.append(2)
        ll.append(4)
        ll.remove_duplicates()

        expected = [1, 2, 3, 4]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_duplicates_at_the_end(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(3)
        ll.remove_duplicates()

        expected = [1, 2, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_empty_list(self):
        ll = SolutionList(None)
        ll.head = None
        ll.length = 0
        ll.remove_duplicates()

        expected = []
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
