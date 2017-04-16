import unittest
import BracketChecker

class TestBracketChecker(unittest.TestCase):
    def testUnbalancedLeftParenthesisOnly(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check('('))

    def testUnbalancedRightParenthesisOnly(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check(')'))

    def testUnbalancedMissingRightParenthesis(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check('(()'))

    def testUnbalancedMissingLeftParenthesis(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check('())'))

    def testBalancedSimple(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertTrue(parityChecker.check('()'))

    def testBalancedNestedParenthesis(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertTrue(parityChecker.check('(())'))
        self.assertTrue(parityChecker.check('(()())'))
        self.assertTrue(parityChecker.check('()((()))'))
        self.assertTrue(parityChecker.check('(()()()())'))
        self.assertTrue(parityChecker.check('(((())))'))
        self.assertTrue(parityChecker.check('(()((())()))'))

    def testUnbalancedNestedParenthesis(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check('((((((())'))
        self.assertFalse(parityChecker.check('()))'))
        self.assertFalse(parityChecker.check('(()()(()'))

    def testBalancedNestedMixed(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertTrue(parityChecker.check('{{([][])}()}'))
        self.assertTrue(parityChecker.check('[[{{(())}}]]'))
        self.assertTrue(parityChecker.check('[][][](){}'))

    def testUnbalancedNestedMixed(self):
        parityChecker = BracketChecker.BracketChecker()
        self.assertFalse(parityChecker.check('([)]'))
        self.assertFalse(parityChecker.check('((()]))'))
        self.assertFalse(parityChecker.check('[{()]'))

if __name__ == "__main__":
    unittest.main()

