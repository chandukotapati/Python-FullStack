# data types: 
# numbers: int, float, bool, complex 
# strings: str
# sequences: list, tuple, range 
# mapping : dict
# set : set and frozenset
# binary : bytes and bytearray 

 # Note: 
# In python all the data types are objects 
# If it is object then it must have class 
# class is blue print or a template it contains properties, methods and constructors


# variable: variable holds the value and stores the value 
# numbers:

i = 10
print(i, type(i))  #o/p; 10 <class 'int'>

# Note: Here i is variable and i is object
j = 10.0
print(j, type(j))  #o/p; 10.0 <class 'float'>

b = True
print(b, type(b))   #o/p; True <class 'bool'>

c = 10j
print(c, type(c))   #o/p; 10j <class 'complex'>

s = "hello" 
print(s, type(s))      # o/p; hello <class 'str'>

l1 = []
print(l1,type(l1))     # [] <class 'list'>

t1 = ()
print(t1, type(t1))     # () <class 'tuple'>

r1 = range(0)
print(r1, type(r1))      #  range(0, 0) <class 'range'>

d1 = {}
print(d1, type(d1))     # {} <class 'dict'>

# set {10}
s1 = {10}
print(s1, type(s1))    # {10} <class 'set'>

b1 = bytes()
print(b1,type(b1))     # b'' <class 'bytes'

b2 = bytearray()
print(b2, type(b2))   #bytearray(b'') <class 'bytearray'>

f1 = frozenset()
print(f1, type(f1))    #frozenset() <class 'frozenset'>

# Eg: 
# class pen:  --> pen()
# class car:  --> car()
# class int --> int()

default_values = [int, float, complex, bool, str, list, tuple, set, frozenset, dict, bytes, bytearray, range, None]
print(default_values)

#[<class 'int'>,
# <class 'float'>,
# <class 'complex'>,
# <class 'bool'>,
# <class 'str'>,
# <class 'list'>,
# <class 'tuple'>,
# <class 'set'>,
# <class 'frozenset'>,
# <class 'dict'>,
# <class 'bytes'>,
# <class 'bytearray'>,
# <class 'range'>,
# None]

d_objects = [int(), float(), complex(), bool(), str(), list(), tuple(), set(), frozenset(), dict(), bytes(), bytearray(), range(0)]
print(d_objects)

        #[0, 0.0, 0j, False, '', [], (), set(), frozenset(), {}, b'', bytearray(b''), range(0, 0)]
        
        
# Java is very strict in term of data types, but not python
a = 10 # int and it is object 

# int a = 10 # it is not object it is int datatype