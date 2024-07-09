import unittest
from exercise1 import SolutionList

class Evaluate(unittest.TestCase):
    def test_has_loop_when_tail_connects_to_head(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.tail.next = ll.head
        
        expected = True
        actual = ll.has_loop()
        self.assertEqual(expected, actual)

    def test_has_loop_when_inner_loop(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.append(6)
        ll.tail.next = ll.head.next.next.next  # 6 -> 4

        expected = True
        actual = ll.has_loop()
        self.assertEqual(expected, actual)

    def test_has_loop_when_no_loop(self):
        ll = SolutionList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)

        expected = False
        actual = ll.has_loop()
        self.assertEqual(expected, actual)

    def test_has_loop_when_no_nodes(self):
        ll = SolutionList(1)
        ll.pop()

        expected = False
        actual = ll.has_loop()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
