import unittest
import PalindromeChecker

class TestPalindromeChecker(unittest.TestCase):
    def testFunctional(self):
        palindromeChecker = PalindromeChecker.PalindromeChecker()
        self.assertFalse(palindromeChecker.check("lsdkjfskf"))
        self.assertTrue(palindromeChecker.check("radar"))
        self.assertTrue(palindromeChecker.check("aca"))

if __name__ == "__main__":
    unittest.main()
