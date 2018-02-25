import unittest
from collections import defaultdict

class unitest(unittest.TestCase):
    def testNone(self):
        s = ""
        t = ""
        Output = True
        self.assertEqual(Solution().isAnagram(s,t),Output)
    def testSample(self):
        s = "anagram"
        t = "nagaram"
        Output = True
        self.assertEqual(Solution().isAnagram(s,t),Output)
    def testFalseSample(self):
        s = "rat"
        t = "car"
        Output = False
        self.assertEqual(Solution().isAnagram(s,t),Output)

class Solution():
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    unittest.main()
