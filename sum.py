# Program to fins sum of 3 no if no are equal then print 3 times of the sum

a = float(input("Enter first no  : "))
b = float(input("Enter second no : "))
c = float(input("Enter third no  : "))

if a == b == c:
    d = a+b+c
    e = d*3
    print("\n The entered no are eual hence 3 times of sum = {}".format(e))

else:
    d = a+b+c
    print("\n Sum of given no = {}".format(d))
