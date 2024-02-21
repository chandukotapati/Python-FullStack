# conact / add the list
l1 = [10,20,30,40,50]
l2 = [10,20,30,40,50]
print(l1 + l2)   #[10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# Repetation/ Multiplication
print(l1 * 2)     #[10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
print(l1 * 3)     #[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

#Unpacking
a, *b, c, d = [10, 20, 30, 40, 50, 60]
print(a)    #10
print(b)     #[20,30,40]
print(c)     #50
print(d)      #60

