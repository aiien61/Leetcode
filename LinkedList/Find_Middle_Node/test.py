import unittest
from exercise1 import SolutionList

class Evaluate(unittest.TestCase):
    def test_find_middle_node_in_odd_list(self):
        my_linked_list = SolutionList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        expected = 3
        actual = my_linked_list.find_middle_node().value
        self.assertEqual(expected, actual)

    def test_find_middle_node_in_even_list(self):
        my_linked_list = SolutionList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        expected = 4
        actual = my_linked_list.find_middle_node().value
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
