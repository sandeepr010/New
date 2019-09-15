print("\n")

set1 = {"Ramachandran","Uma","Sandeep","Sandhya"}
print(set1)
print("\n")

set1.add("Adi") # add a value to set by using add()
print(set1)
print("\n")

set1.update(["Manoj","Rajesh","Raji"]) # Add multiple values to set
print(set1)
print("\n")

print(len(set1)) # Get the length of the set
print("\n")

set1.remove("Raji") # Remove a value from set by using remove() this will show eror if value not in the set
print(set1)
print("\n")

set1.discard("Rajesh") # Remove a value from set by using discard() but not show eror if value not in the set
print(set1)
print("\n")

x = set1.pop() # Remove last item from set
print(x)
print(set1)
print("\n")

set1.clear() # Clear the set
print(set1)

del set1   # Delete the complete set

set1 = {"a","b","c"}
set2 = {"1","2","3"}

set3 = set1.union(set2) # union() use to combile both set value in third set
print(set3)
print("\n")

set1.update(set2) # update() method insert set2 into set1
print(set1)
print("\n")
