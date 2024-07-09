from base import Node, LinkedList

class SolutionList(LinkedList):
    def binary_to_decimal(self) -> int:
        decimal: int = 0
        power: int = self.length - 1
        digit: Node = self.head
        while digit is not None:
            decimal += digit.value * 2 ** power
            power -= 1
            digit = digit.next
        return decimal
