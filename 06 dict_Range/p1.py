# dict
#Usingdict we can store key value pairs
#In dict key can be either string or integer

# print(dir(dict))

# 'clear',
# 'copy',
# 'items',
# 'keys',
# 'pop',
# 'update',
# 'values'
d1 = {}
print(d1, type(d1))   #{} <class 'dict'>

d1 = {1 :10, 2:20, 3 :30, 4 :40}
print(d1)   #{1: 10, 2: 20, 3: 30, 4: 40}
print(d1.keys())     #[1, 2, 3, 4]
print(d1.values())   #[10, 20, 30, 40]
print(d1.items())     #[(1, 10), (2, 20), (3, 30), (4, 40)]

#can we assign a position a position to list
d1 = {1 : 10, 2 : 20}
d1[3] = 30
print(d1)  # {1: 10, 2: 20, 3: 30}

d1 = {}
d1[1] = 10
d1[2] = 20
print(d1)  # {1: 10, 2: 20}

d1 = {"nameone" : "Sai Kiran", "nametwo" : "Sai Ram"}
d1["nametwo"] = "Sai Kumar"
print(d1)  # {'nameone': 'Sai Kiran', 'nametwo': 'Sai Kumar'}

d1 = {1: 10, 2: 20, 3: 30, 4 : 40}
d2 = {"nameone" : "Sai Kiran", "nametwo": "Sai Ram"}
d1.update(d2)
print(d1)  # {1: 10, 2: 20, 3: 30, 4: 40, 'nameone': 'Sai Kiran', 'nametwo': 'Sai Ram'}

d1 = {1: 10, 2: 20, 3: 30, 4 : 40}
d1.update({1: "NameOne"})
print(d1)  # {1: 'NameOne', 2: 20, 3: 30, 4: 40}

d1 = {1: 10, 2:20, 3:30, 4: 40, 5: 50}
d1["NameOne"] = d1.pop(1)
print(d1)  # {2: 20, 3: 30, 4: 40, 5: 50, 'NameOne': 10}


employees = {
    
    "employeeName" : {"NameOne": "Sai Kiran", "NameTwo": "Sai Ram"},
    "employeeSalary" : 25000,
    "employeePostion" : ["Developer", "Designer", "Devops Engineer"]
}

print(employees["employeeName"]) # {'NameOne': 'Sai Kiran', 'NameTwo': 'Sai Ram'}
print(employees["employeeName"]["NameTwo"]) # Sai Ram

print(employees["employeeSalary"]) # 25000

print(employees["employeePostion"][1]) # Designer

# range:
r1 = range(0, 10)
print(r1) # range(0, 10)

r2 = list(range(0, 10))
print(r2) #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# r2 = dict(range(0, 10))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

l1 = []
r1 = range(10, 20)
l1.extend(r1) 
print(l1)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# t1 = [1, 2, 3]
# print(id(t1))
# t1 = t1 + [4,]
# print(id(t1))
# print(t1)

# t1 = 10, 20
# t1 = 30, 40

t1 = (10, 20, 30, 40, 50, 10, 20)
print(id(t1))
t1 = (10, 20, 30, 40, 50, 10, 20)
print(id(t1))

print(id(t1[0]), id(t1[1]))