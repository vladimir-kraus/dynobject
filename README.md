# dynobject
Dynamic object class which allows dynamic adding of attributes on the run
and dict-like access to the attributes.

```python
>>> a = DynObject()
>>> a.x = 10  # dynamic adding of attributes
>>> a.x  # access to attributes
10
>>> a["x"]  # access to attributes like to a dict
10
```

DynObject can be initialized from dict or using keyword arguments.

```python
>>> d = dict(x=10, y=20)  # or d = {"x": 10, "y": 20}
>>> a = DynObject(d)
>>> b = DynObject(x=10, y=20)  # equivalent to the above
```

Convert to or use as dict:

```python
>>> a = DynObject(x=10, y=20)
>>> d1 = a.__dict__  # not a copy!
>>> d2 = dict(a.__dict__)  # a copy
>>> d3 = {k: a[k] for k in dir(a)}  # a copy
```
