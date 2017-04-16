import unittest
import Stack

class TestStack(unittest.TestCase):
    def testFunctional(self):
        s = Stack.Stack();

        self.assertTrue(s.isEmpty())

        s.push(4)
        s.push("dog")
        self.assertEqual("dog", s.peek())

        s.push(True)
        self.assertEqual(s.size(), 3)
        self.assertFalse(s.isEmpty())

        s.push(8.4)
        self.assertEqual(8.4, s.pop())
        self.assertEqual(True, s.pop())
        self.assertEqual(2, s.size())

if __name__ == "__main__":
    unittest.main()
