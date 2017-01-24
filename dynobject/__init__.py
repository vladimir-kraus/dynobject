class DynObject(object):

    def __init__(self, source=None):
        if source is not None:
            self.__dict__.update(source)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __bool__(self):
        return bool(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __dir__(self):
            return self.__dict__.keys()

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            # this makes hasattr(...) work correctly
            raise AttributeError(item)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, item):
        try:
            del self.__dict__[item]
        except KeyError:
            raise AttributeError(item)

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        for item in self.__dict__:
            yield item
