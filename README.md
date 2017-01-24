# dynobject
Dynamic object class which allows dynamic adding of attributes on the run
and dict-like access to the attributes.

```python
>>> d = DynObject()
>>> d.x = 10  # dynamic adding of attributes
>>> d.x  # access to attributes
10
>>> d["x"]  # access to attribute like to a dict
10
```

