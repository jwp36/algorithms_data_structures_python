class Stack:
    def __init__(self):
        self.items = []

    """Push new_item onto the stack"""
    def push(self, new_item):
        return self.items.append(new_item)

    """Return and remove the item at the top of the stack"""
    def pop(self):
        return self.items.pop()

    """Return but do not remove the item at the top of the stack"""
    def peek(self):
        return self.items[self.size() - 1]

    def isEmpty(self):
        return self.size() == 0

    """Return the size of the stack"""
    def size(self):
        return len(self.items)
