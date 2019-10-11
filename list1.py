l=[]
e=[]
o=[]
a = int(input('Enter the lenth of list : '))
for i in range(a):
    b = int(input('Enter values for list : '))
    l.append(b)
print(l)
k=0
for i in range(a):
    print(l[k])
    if l[k]%2 == 0:
        e.append(l[k])
    else:
        o.append(l[k])
    l.remove(l[k])
print("Even list = ",e)
print("Odd list = ",o)
print("After removing list element: ",l)
