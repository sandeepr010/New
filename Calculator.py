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

choice = input("Enter Your Choice:  ")
print("\n")
if choice > "4":
   print("Enter any option between 1 to 4 \n")
   exit()

if choice < "1":
   print("Enter any option between 1 to 4 \n")
   exit()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n")

if choice == "1":
    print("Addition of:",num1,"+",num2,"=", add(num1,num2))

elif choice == "2":
    print("Subtarction of:",num1,"-",num2,"=", sub(num1,num2))

elif choice == "3":
    print("Multiplication of:",num1,"*",num2,"=", mul(num1,num2))

elif choice == "4":
    print("Divition of:",num1,"/",num2,"=", div(num1,num2))
print("\n")