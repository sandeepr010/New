# Function for add two number

def add(x,y):
    return x+y

# Function for subtracts two number

def sub(x,y):
    return x-y

# Function for multiplies two number

def mul(x,y):
    return x*y

# Function for divides twon number

def div(x,y):
    return x/y

print("Select One of the operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter Your Choice")

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if choice == "1":
    print(num1,"+",num2,"=", add(num1,num2))

else choice == "2":
    print(num1,"-",num2,"=", sub(num1,num2))

else choice == "3":
    print(num1,"*",num2,"=", mul(num1,num2))

else choice == "4":
    print(num1,"/",num2,"=", div(num1,num2))

else: print("Enter a valid input")

