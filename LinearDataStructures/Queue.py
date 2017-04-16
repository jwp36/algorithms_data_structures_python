class Queue:
    def __init__(self):
       self.items = []

    """Queue new item into Queue"""
    def queue(self, new_item):
        self.items.insert(0, new_item)

    """Dequeue item from Queue"""
    def dequeue(self):
        return self.items.pop()

    "Return True if Queue is Empty"""
    def isEmpty(self):
        return self.size() == 0

    """Return the size of the Queue"""
    def size(self):
        return len(self.items)
