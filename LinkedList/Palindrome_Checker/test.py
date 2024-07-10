import unittest
from base import Node, DoublyLinkedList
from exercise1 import SolutionList
from typing import List

def linkedlist_to_list(head: Node) -> List[int]:
    result: List[int] = []
    current: Node | None = head
    while current:
        result.append(current.value)
        current = current.next
    return result

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome_checker_when_empty_list(self) -> None:
        ll: DoublyLinkedList = SolutionList(None)
        ll.head = None
        ll.tail = None
        ll.length = 0

        actual: bool = ll.is_palindrome()
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_longer_palindrome(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(4)
        ll.append(3)
        ll.append(2)
        ll.append(1)

        actual: bool = ll.is_palindrome()
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_longer_not_palindrome(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(0)
        ll.append(1)
        ll.append(3)
        ll.append(2)
        ll.append(1)

        actual: bool = ll.is_palindrome()
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_odd_length_not_palindrome(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(2)
        ll.append(3)

        actual: bool = ll.is_palindrome()
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_odd_length_palindrome(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(2)
        ll.append(1)

        actual: bool = ll.is_palindrome()
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_single_node(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)

        actual: bool = ll.is_palindrome()
        expected: bool = True
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_two_different_node(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(2)

        actual: bool = ll.is_palindrome()
        expected: bool = False
        self.assertEqual(actual, expected)

    def test_palindrome_checker_when_two_same_node(self) -> None:
        ll: DoublyLinkedList = SolutionList(1)
        ll.append(1)

        actual: bool = ll.is_palindrome()
        expected: bool = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()