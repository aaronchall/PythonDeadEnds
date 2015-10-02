# PythonDeadEnds
Dead ends in Python!

# setcomplement.py
## SetComplement

Since all (builtin) sets in Python are finite, all complements of the builtin sets would be infinite. 

Practically, one cannot iterate over an infinite set... so no __iter__ method. 
Unless maybe we have the complement of the complement of a finite set, but then we'd just have the set.

Also, since len() must return an integer, and a len(SetComplement([])) would be infinity, 
and you cannot represent infinity as an integer type (well, maybe you can by subclassing ints...) 
but it's not very practical. Anyways, no __len__ method.

This object is interesting theoretically, but has little practical use.

