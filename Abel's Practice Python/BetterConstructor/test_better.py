from unittest import TestCase
from BetterConstructor.BetterClassConstructor import Better

__author__ = 'abelamadou'

b = Better(Mike=10, __Joe="14", __Abel=(1,"2",3,"4"))

class TestBetter(TestCase):
  def test_set_attributes(self):
      setVall = b
      setVall.set_attributes("Mike",1000)
      self.assertEqual(setVall.get_attributes("Mike"),1000)
      self.assertEqual(setVall.get_attributes("__Abel",(1,"2",3,"4")))
      setVall.set_attributes("__Joe",[10,200,"400", 6+10])
      self.assertEqual(setVall.get_attributes("__Joe",[10,200,"400", 16]))
    # pass
  def test_get_attributes(self):
    self.assertEqual(b.get_attributes("__Joe"),"14")
    self.assertEqual(b.get_attributes("__Abel"),(1,"2",3,"4"))
    self.assertEqual(b.get_attributes("Mike"),10)

  def test_get_couple_attributes(self):

    self.assertEqual(b.get_couple_attributes(),None)
    self.assertEqual(b.get_couple_attributes("__Abel"),[(1,"2",3,"4")])
    self.assertEqual(b.get_couple_attributes('Mike',"__Abel"),[10,(1,"2",3,"4")])
    self.assertEqual(b.get_couple_attributes('Mike',"__Joe","__Abel"),[10,"14",(1,"2",3,"4")])
    pass

  def test_toString(self):
    e = Better()
    self.assertEqual(e.toString(),"")
    self.assertEqual(b.toString(),"|<Key:__Joe; Value:14>||<Key:__Abel; Value:(1, '2', 3, '4')>||<Key:Mike; Value:10>|")
    a = Better(__Howdy="20")
    self.assertEqual(a.toString(),"|<Key:__Howdy; Value:20>|")
    pass
