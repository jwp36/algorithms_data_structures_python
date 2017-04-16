import sys
sys.path.insert(0, '..')

from LinearDataStructures import Stack

class BracketChecker:
    OPENERS = "([{"
    CLOSERS = ")]}"

    def check(self, string):
        stack = Stack.Stack()

        for char in string:
            if char in BracketChecker.OPENERS:
                #Handle Opener
                stack.push(char)
            elif char in BracketChecker.CLOSERS:
                #Handle Closer
                if stack.isEmpty():
                    return False
                elif self.matches(stack.peek(), char):
                        stack.pop()
                else:
                    return False
            else:
                raise Exception()

        return stack.isEmpty()

    def matches(self, opener, closer):
        return BracketChecker.OPENERS.index(opener) == BracketChecker.CLOSERS.index(closer)
