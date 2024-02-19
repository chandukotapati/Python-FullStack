# list 
# List is a datatype and it is an object 
# List is unsafe (muttable)
# In list we can store different types of datatypes 
# List will maintain the insertion order 
# List will allow duplicates values

l1 = []
print(l1, type(l1))   #[] <class 'list'>

l2 = list
print(l2, type(l2))   #<class 'list'> <class 'type'>

l3 = list()
print(l3, type(l3))    #[] <class 'list'>

# in list we can store different data types and duplicates allowed
l4 = [ 10, 20, 30, 40, 50, 60, "name one", "nametwo", "namethree" "namefour"]
print(l4, type(l4))

# [10, 20, 30, 40, 50, 60, 'name one', 'nametwo', 'namethreenamefour'] <class 'list'>

l5 = [10, 20, 30, 40, 10, 20, 30]
print(l5)  # [10, 20, 30, 40, 10, 20, 30]

# list is a class, list is an object, list is datatype 
l6 = []
l6.append(10)
print(l6)    #[10]

l6.append(20)
l6.append(30)
print(l6)        #[10, 20, 30]

#l6.append(10, 20)
# print(l6)     ## print(l6)  # TypeError: list.append() takes exactly one argument (2 given)

# Two behavioiurs:
# extend(string element)
# extend([elements])

l7 = [10, 20, 30, 40,]
l7.extend("nameone")
print(l7)           #[10, 20, 30, 40, 'n', 'a', 'm', 'e', 'o', 'n', 'e']
l7.extend(["nameone"])
print(l7)   #[10, 20, 30, 40, 'n', 'a', 'm', 'e', 'o', 'n', 'e', 'nameone']

l7.extend(["chandu", "jayanth"])
print(l7)     #[10, 20, 30, 40, 'n', 'a', 'm', 'e', 'o', 'n', 'e', 'nameone', 'chandu', 'jayanth']

l7.extend([100])
print(l7)   # [10, 20, 30, 40, 50, 'N', 'a', 'm', 'e', 'O', 'n', 'e', 'NameOne', 'Sai Kiran', 'Sai Ram', 'Sai Krishna', 100]

# Two behavioiurs:
# pop() : delete the last element 
# pop(index) : delete the index element

l1 = [10, 20, 30, 40, 50, 60, 70, 80]
#      0   1   2   3   4   5   6   7 
print(l1)  # [10, 20, 30, 40, 50, 60, 70, 80]
print(l1[2]) # 30
print(l1[4]) # 50

l1.pop() 
print(l1) # [10, 20, 30, 40, 50, 60, 70]

print(l1.pop())  # 70
print(l1)  # [10, 20, 30, 40, 50, 60]

l1.pop(3)
print(l1) # [10, 20, 30, 50, 60]

# index(element)
l1 = [10, 20, 30, 40, 50, 60, 70, 80]  # elements
#      0   1   2   3   4   5   6   7   # index positions 
print(l1.index(40))  # 3
# print(l1.index(100))   # ValueError: 100 is not in list

# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort

# insert(index, element)
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
#      0   1   2   3   4   5   6   7 
l1.insert(4, "Sai Kiran")
print(l1)  # [10, 20, 30, 40, 'Sai Kiran', 50, 60, 70, 80]

# remove(element)
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
#      0   1   2   3   4   5   6   7 
l1.remove(30)
print(l1) # [10, 20, 40, 50, 60, 70, 80]

# clear()
l1 = [10, 20, 30, 40, 50]
l1.clear()
print(l1) # []

# copy()
l1 = [10, 20, 30, 40]
print(l1)  # [10, 20, 30, 40]
print(l1.copy())   # [10, 20, 30, 40]

# count()
l1 = [10, 20, 30, 40, 10, 20, 30, 10, 20]
print(l1.count(10))  # 3
print(l1.count(40))  # 1
print(l1.count(100)) # 0

# reverse()
l1 = [10, 20, 30, 40]
l1.reverse()
print(l1)  # [40, 30, 20, 10]

# sort()
l1 = [50, 30, 10, 20, 10]
l1.sort(reverse=False)
print(l1)  # [10, 10, 20, 30, 50]

l1.sort(reverse=True)
print(l1)  # [50, 30, 20, 10, 10]

