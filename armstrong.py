a = int(input("Enter a number: "))
b = a
c = len(str(a))
s = 0
while(b!=0):
    s = s+((b%10)**c)
    b = b//10
if a == s:
    print("Number {} is armstrong no".format(a))
else :
    print("Number {} is not armstrong no".format(a))
