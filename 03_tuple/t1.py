# tuple is datatype and it an an object
# tuple is safe (immutable) 
# 'count', 'index

# count(elemnet)
t1 = (10, 20, 30, 40, 50, 60, 70, 80, 10, 20)
#      0   1   2   3   4   5   6   7   8   9 
print(t1.count(10))  # 2

# index(elemnet)
# index(elemnet, start, end)
print(t1.index(10))  # 0 
print(t1.index(10,4,9)) # 8

t1 = 10,
print(t1, type(t1))