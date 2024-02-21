# set 
# set is unordered elements 
# list and tuple are ordered elements
# set will not maintain duplicates, list and tuple will maintain duplicates
# set is mutable, frozen set is immutable
s1 = set()
print(s1) # set()

s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
print(s1)  # {50, 20, 70, 40, 10, 60, 30}

print(dir(s1))
# 'add', 'clear', 'copy', 'discard', 'pop', 'remove', 'update'

s1 = {"NameOne"}
s1.add("NameTwo")
print(s1) # {'NameOne', 'NameTwo'}

# s2 = {10, 20, 30, 40, 50}
# s2.add(s1)
# print(s2) # TypeError: unhashable type: 'set'

s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
s1.remove(20)
print(s1)  # {50, 70, 40, 10, 60, 30}

# remove will throw error if value is not present
# Discord will not throw error if value is not present
 
s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
s1.discard(20)
print(s1)  # {50, 70, 40, 10, 60, 30}

s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
s1.update([100, 200, 300, 400])
print(s1)  # {70, 200, 10, 400, 20, 30, 100, 40, 300, 50, 60}

l1 = list(s1)
print(l1)  # [70, 200, 10, 400, 20, 30, 100, 40, 300, 50, 60]

l1.sort()
print(l1) # [10, 20, 30, 40, 50, 60, 70, 100, 200, 300, 400]

s1 = {10, 20, 30, 40, 50, 60, 70, 10, 20}
s1.pop()
print(s1) # {20, 70, 40, 10, 60, 30}

# pop will remove any one of the element

f1 = frozenset() #[frozenset will not use any where]
print(f1)      #frozenset()

s1 = set()
s1.add(f1)
print(s1) # {frozenset()}

s1 = {10, 20, 30, 40}
print(s1)

f2 = frozenset(["NameOne", "NameTwo"])
s1.add(f2) # 
print(s1)  # {40, 10, frozenset({'NameOne', 'NameTwo'}), 20, 30}

s1.remove(f2)
print(s1)  # {40, 10, 20, 30}