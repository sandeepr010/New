print("\n")
list1 = ["Sandhya","Sandeep","Vasanth","Manoj","Adi"]
print(list1)
print("\n")

print(list1[1]) # print the value in 1th position
print("\n")

print(list1[-1]) # Negative intex is use to access the value from last
print("\n")

print(list1[1:4]) # Print the list start from 1th position ends in before 4th position
print("\n")

list1[2] = "Rajesh" # change the value of 2nd position and updated with new value
print(list1)
print("\n")

list1.append("Vasanth") # Add value to the list in last
print(list1)
print("\n")

list1.insert(0,"Uma") # insert value in the 0th position
print(list1)
print("\n")

list1.remove("Vasanth") # Remove the specified value
print(list1)
print("\n")

list1.pop() # Remove the last value from the list
print(list1)
print("\n")

del list1[0] # Remove the 0th position value
print(list1) # del list : this will delete the list
print("\n") # list.clear() empti the list

copy = list1.copy() # copy the list 
print(copy)
print("\n")

list2 = list(list1) # Copy list by using list()
print(list2)
print("\n")

list3 = list1+list2 # Join tow list into three
print(list3)
print("\n")

list4 = ["Uma","Adi","Vasanth"]
list1.extend(list4) # Add list4 in the end of list1 by using extend()
print(list1)

