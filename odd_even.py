# To find enter given no is odd or even

print("\n","="*8,"Program to find enterd no is even or odd","="*8)
a = int(input("\nEnter a no :"))

c = a % 2    # Finding mod 

if c > 0:
    print("\n","="*16,"No {}  is odd no".format(a),"="*16,"\n\n")

else :
    print("\n","="*16,"No {}  is even no".format(a),"="*16,"\n\n")
