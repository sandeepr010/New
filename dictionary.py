print("\n")
dict1 = { "Brand" : " Ford",
          "Model" : "Mustang",
          "Year"  : 1964
        }
print(dict1)
print("\n")

x = dict1["Model"] # Print the model 
print(x)
print("\n")

y = dict1.get("Model") # Print the value of model using get()
print(y)
print("\n")

dict1["Year"] = 2019 # Change value
print(dict1)
print("\n")

print(len(dict1)) # Print the length of dictionary
print("\n")

dict1["Color"] = "Black" # Adding a value
print(dict1)
print("\n")

dict1.pop("Year") # Remove the value of given by using pop()
print(dict1)
print("\n")

dict1.popitem() # Remove the last incerted item (befor python 3.7 a random value removed)
print(dict1)
print("\n")


