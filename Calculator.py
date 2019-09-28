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

while True:

         choice = input("Enter Your Option:  ")
         print("\n")

         if choice > "4" or choice <"1":
                  print("Enter option between 1 to 4 \n")
                                  
         elif choice <="4" and choice >="1" :
             break

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n")

if choice == "1":
    print("Addition of {} and {} = {} ".format(num1,num2,add(num1,num2)))

elif choice == "2":
    print("Subtarction of {} and {} = {} ".format(num1,num2,sub(num1,num2)))

elif choice == "3":
    print("Multiplication of {} and {} = {}".format(num1,num2,mul(num1,num2)))

elif choice == "4":
    print("Divition of {} and {} = {}".format(num1,num2,div(num1,num2)))
print("\n")
