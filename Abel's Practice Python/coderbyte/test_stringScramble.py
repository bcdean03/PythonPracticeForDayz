from unittest import TestCase
from StringScramble import StringScramble

__author__ = 'abelamadou'


class TestStringScramble(TestCase):
  def test_StringScramble(self):#have to start with 'test_..'
    self.assertEqual(StringScramble("cdore","coder"),True,"StringScramble method failed")
    self.assertEqual(StringScramble("rkqodlw","world"),True)