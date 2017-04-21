import unittest
import Deque

class TestDeque(unittest.TestCase):
    def testFunctional(self):
        d = Deque.Deque();

        self.assertTrue(d.isEmpty())

        d.addRear(4)
        d.addRear("dog")
        d.addFront("cat")
        d.addFront(True)

        self.assertEqual(d.size(), 4)
        self.assertFalse(d.isEmpty())

        d.addRear(8.4)
        self.assertEqual(8.4, d.removeRear())
        self.assertEqual(True, d.removeFront())

if __name__ == "__main__":
    unittest.main()
