a = []
b = int(input("Enter how many numbers in array : "))

for i in range(0,b):
    d = 1+i
    c = float(input("Enter {} no : ".format(d)))
    a.append(c)
print("Given list : ",a)

minu = a[0]
for x in a:
    if minu>x:
        minu=x
print("\nMinum no in the list = ",minu)

maxm = a[0]
for x in a:
    if maxm<x:
        maxm=x
print("\nMaximum no in the list = ",maxm)
