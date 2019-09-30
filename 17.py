# To find diff between a given no and 17, if it is > 17 print double the diff
a = float(input("Enter no : "))

if a <= 17 :
    b = 17-a
    print("\nDifference between {} and 17 = {} \n".format(a,b))

else :
    b = a - 17
    c = 2*b
    print("\nEntered value is {} > 17 hence double diff = {}\n".format(a,c))

