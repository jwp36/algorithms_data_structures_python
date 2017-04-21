import sys
sys.path.insert(0, '..')

from LinearDataStructures import Deque

class PalindromeChecker:
    def check(self, string):
        d = Deque.Deque()

        for char in string:
            d.addRear(char)

        for _ in range(0, len(string) // 2):
            if d.removeFront() == d.removeRear():
                pass
            else:
                return False

        return True


