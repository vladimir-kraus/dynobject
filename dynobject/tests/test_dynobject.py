import unittest

from dynobject import DynObject


class DynObjectTests(unittest.TestCase):

    def test_empty(self):
        dobj = DynObject()
        self.assertFalse(dobj)
        self.assertEqual(len(dobj), 0)
        self.assertTrue(isinstance(self.__dict__, dict))
        self.assertEqual(dobj.__dict__, dict())
        self.assertFalse(dobj.__dict__)
        self.assertEqual(len(dobj), 0)

    def test_init_with_dict(self):
        source = dict(x=1, y=2)
        dobj = DynObject(source)
        self.assertEqual(dobj.__dict__, source)
        self.assertEqual(dobj.x, 1)
        self.assertEqual(dobj.y, 2)
        self.assertEqual(dobj["x"], 1)
        self.assertEqual(dobj["y"], 2)

    def test_init_with_kwargs(self):
        source = dict(x=1, y=2)
        dobj = DynObject(x=1, y=2)
        self.assertEqual(dobj.__dict__, source)
        self.assertEqual(dobj.x, 1)
        self.assertEqual(dobj.y, 2)
        self.assertEqual(dobj["x"], 1)
        self.assertEqual(dobj["y"], 2)

    def test_properties(self):
        dobj = DynObject(x=1, y=2)
        self.assertTrue(dobj)
        self.assertEqual(len(dobj), 2)
        self.assertEqual(dobj.x, 1)
        self.assertEqual(dobj.y, 2)
        self.assertEqual(dobj["x"], 1)
        self.assertEqual(dobj["y"], 2)
        self.assertListEqual(dir(dobj), ["x", "y"])
        self.assertEqual(str(dobj), str(dobj.__dict__))
        self.assertEqual(repr(dobj), repr(dobj.__dict__))
