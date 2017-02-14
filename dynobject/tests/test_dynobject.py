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
        self.assertTrue(dobj)

        # if the argument in init is a dict then we can test identity
        self.assertTrue(dobj.__dict__ is source)

        self.assertEqual(dobj.__dict__, source)

        self.assertEqual(dobj.x, 1)
        self.assertEqual(dobj.y, 2)

        self.assertEqual(dobj["x"], 1)
        self.assertEqual(dobj["y"], 2)

        self.assertTrue(hasattr(dobj, "x"))
        self.assertEqual(getattr(dobj, "x"), 1)
        self.assertTrue("x" in dobj)

        with self.assertRaises(AttributeError):
            getattr(dobj, "z")

        with self.assertRaises(AttributeError):
            dobj.z

        with self.assertRaises(KeyError):
            dobj["z"]

    def test_init_with_kwargs(self):
        dobj = DynObject(x=1, y=2)
        self.assertEqual(dobj.__dict__, dict(x=1, y=2))

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

        self.assertTrue("x" in dobj)
        self.assertFalse("X" in dobj)

        self.assertEqual(dobj, DynObject(x=1, y=2))
        self.assertNotEqual(dobj, DynObject())
        self.assertNotEqual(dobj, DynObject(x=2, y=2))
        self.assertNotEqual(dobj, DynObject(x=1, y=2, z=3))

    def test_string_repr(self):
        dobj = DynObject(x=1)
        self.assertEqual(str(dobj), "{'x': 1}")
        self.assertEqual(repr(dobj), "{'x': 1}")

    def test_del(self):
        dobj = DynObject(x=1, y=2)
        del dobj.x
        self.assertEqual(dobj.__dict__, dict(y=2))

        dobj = DynObject(x=1, y=2)
        del dobj["x"]
        self.assertEqual(dobj.__dict__, dict(y=2))

    def test_setattr(self):
        dobj = DynObject()
        dobj.x = 1
        self.assertEqual(dobj.__dict__, dict(x=1))

        dobj = DynObject()
        dobj["x"] = 1
        self.assertEqual(dobj.__dict__, dict(x=1))
