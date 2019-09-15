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

c="welcome"
print(c.capitalize()) #convert first character to upper case
print("\n")

e="WELCOME TO MY WORLD"
print(e.casefold()) #convert to lowercase letter
print("\n")

print(a.center(50))#add white space befor and after with assigned value heare it is 50
print("\n")

print(e.count('O')) # hear it count how many time 'O' is present in string
print("\n")

print(e.encode())
print("\n")

print(e.endswith('D')) # check if the strig is endss with given value
print("\n")

f="42\t32\tgood\thelp"
print(f.expandtabs(10)) # set the tab size ("\t") 
