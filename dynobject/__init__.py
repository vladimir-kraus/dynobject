from collections.abc import Container, Sized, Iterable

__version__ = "0.3.0"


class DynObject(Container, Iterable, Sized, object):
    # collections.abc.Collection since Python 3.6

    def __init__(self, *args, **kwargs):
        d = None
        if not args and not kwargs:
            d = dict()
        elif len(args) == 1 and not kwargs:
            d = args[0]
        elif kwargs and not args:
            d = dict(kwargs)

        if d is not None:
            super(DynObject, self).__setattr__("__dict__", d)
        else:
            raise TypeError("invalid arguments")

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __bool__(self):
        return bool(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __contains__(self, item):
        return item in self.__dict__

    def __dir__(self):
            return self.__dict__.keys()

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        for item in self.__dict__:
            yield item
