import os
import sys

import unittest

from dynobject import DynObject


class DynObjectTests(unittest.TestCase):

    def test_empty(self):
        dobj = DynObject()
        self.assertTrue(isinstance(self.__dict__, dict))
        self.assertEqual(dobj.__dict__, dict())
        self.assertFalse(dobj.__dict__)
        self.assertEqual(len(dobj), 0)

    def test_non_empty(self):
        source = dict(x=1, y=2)
        dobj = DynObject(source)
        self.assertTrue(dobj.__dict__)
        self.assertEqual(dobj.__dict__, source)
        self.assertEqual(dobj.x, 1)
        self.assertEqual(dobj.y, 2)
        self.assertEqual(dobj["x"], 1)
        self.assertEqual(dobj["y"], 2)


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    module_path = os.path.join(path, os.pardir, os.pardir)
    sys.path.insert(0, module_path)
    print("Testing in {}".format(path))
    test_suite = unittest.defaultTestLoader.discover(path, pattern="*.py")
    unittest.TextTestRunner(verbosity=2).run(test_suite)
