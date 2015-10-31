__author__ = 'abelamadou'
# https://confluence.jetbrains.com/display/PYH/Creating+and+running+a+Python+unit+test
# https://www.youtube.com/watch?v=F7a0iUH6kVA
# https://www.youtube.com/watch?v=fU7RHewj6dg
import unittest
from coderbyte.StringScramble import StringScramble
# from StringScramble import StringScramble

class MyTestCase(unittest.TestCase):
  def test_StringScramble(self):#have to start with 'test_..'
    self.assertEqual(StringScramble("cdore","coder"),True,"StringScramble method failed")
    self.assertEqual(StringScramble("rkqodlw","world"),True,"StringScramble method failed")
    # print(__name__)

if __name__ == '__main__':
    unittest.main()
