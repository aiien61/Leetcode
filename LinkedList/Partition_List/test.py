import random
import unittest
from exercise1 import SolutionList

# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

class TestPartitionList(unittest.TestCase):
    def test_partition_normal_random_unsorted_values(self):
        x = 3
        ll = SolutionList(3)
        ll.append(1)
        ll.append(4)
        ll.append(2)
        ll.append(5)
        ll.partition_list(x)

        expected = [1, 2, 3, 4, 5]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_all_equal_values(self):
        x = 3
        ll = SolutionList(3)
        ll.append(3)
        ll.append(3)
        ll.partition_list(x)

        expected = [3, 3, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_single_element(self):
        x = 3
        ll = SolutionList(1)
        ll.partition_list(x)

        expected = [1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_already_sorted_values(self):
        x = 2
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.partition_list(x)

        expected = [1, 2, 3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_reversed_values(self):
        x = 2
        ll = SolutionList(3)
        ll.append(2)
        ll.append(1)
        ll.partition_list(x)

        expected = [1, 3, 2]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_all_smaller_values(self):
        x = 2
        ll = SolutionList(1)
        ll.append(1)
        ll.append(1)
        ll.partition_list(x)

        expected = [1, 1, 1]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_single_element_equal_to_x(self):
        x = 3
        ll = SolutionList(3)
        ll.partition_list(x)

        expected = [3]
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)

    def test_partition_empty_list(self):
        random.seed(0)
        x = 3
        ll = SolutionList(random.randint(1, 100))
        ll.make_empty()
        ll.partition_list(x)

        expected = []
        actual = linkedlist_to_list(ll.head)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
