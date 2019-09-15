a=' Hello, world!'
print(a+"\n")

print(a[2:5]+"\n") #this will print the string star from positon 2 to position 4 : ell

print(a[-5:-2]+"\n") # this start count from back : orl

print(len(a))# used to know the length of string
print("\n")

print(a.strip()+"\n") # used to remove any white space from beginning or end

print(a.lower()+"\n") # used to print string in lower case 

print(a.upper()+"\n") # used to print string in upper case

print(a.replace("H","J")+"\n") # replace the string with another string

print(a.split(",")) #split the string into substring if it is finds instances of
print("\n")

d="ell" in a # check the given string present in string return true or fals
print(d)
print("\n")

b="ell" not in a # check the given string not present in string return true or fals
print(b)
print("\n")
