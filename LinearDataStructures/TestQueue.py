import unittest
import Queue

class TestQueue(unittest.TestCase):
    def testFunctional(self):
        q = Queue.Queue();

        self.assertTrue(q.isEmpty())

        q.queue(4)
        q.queue("dog")
        q.queue(True)

        self.assertEqual(q.size(), 3)
        self.assertFalse(q.isEmpty())

        q.queue(8.4)
        self.assertEqual(4, q.dequeue())
        self.assertEqual("dog", q.dequeue())
        self.assertEqual(2, q.size())

if __name__ == "__main__":
    unittest.main()
