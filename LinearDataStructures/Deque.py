class Deque:
    def __init__(self):
        self.items = []

    """Add new item to the front of the Deque"""
    def addFront(self, new_item):
        self.items.insert(0, new_item)

    """Add new item to the rear of the Deque"""
    def addRear(self, new_item):
        self.items.append(new_item)

    """Remove item from the front of the Deque"""
    def removeFront(self):
        return self.items.pop(0)

    """Remove item from the rear of the Deque"""
    def removeRear(self):
        return self.items.pop()

    "Return True if Deque is Empty"""
    def isEmpty(self):
        return self.size() == 0

    """Return the size of the Deque"""
    def size(self):
        return len(self.items)
