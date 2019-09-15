print("\n")
tuple1 = ("Value","Sandeep","Sandhya","Manoj","Adi")
print(tuple1)
print("\n")

print(tuple1[1]) # Print value in 1st position
print("\n")

print(tuple1[-1]) # Print value count from last 
print("\n")  

print(tuple1[1:3]) # Print value from position 1 and end in 3(not include 3)
print("\n")

print(tuple1[-3:-1]) # print value from position start from behaint
print("\n")

x = list(tuple1) # convert a tuple into lsit to change value in  a list
x[0] = "Uma"
tuple1 = tuple(x)
print(tuple1)
print("\n")

print(len(tuple1)) # Print the length of tuple
print("\n")

del tuple1 # Tuple is unchangeble, so you cannot remove item from it but you can delete a tuple
print(tuple1)
