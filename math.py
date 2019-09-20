print("\n")
print("="*4,"Program for Circle,Triangle and Square Formulas","="*4,"\n")

print("1. Circle\t:\n")
print("2. Triangle \t:\n")
print("3. Square \t:\n")

while True:

    choice = int(input("Enter option no\t :"))
    print("\n")

    if choice < 1 or choice >3 :
        print("\n,""-"*4,"Enter a valid option","-"*4)

    elif choice >=1 and choice <=3 :
        break

# Circle
if choice == 1:
    print("\n")
    print("\t","*"*4,"Circle","*"*4,"\n")
    print("1. Find Area of circle\t:\n")
    print("2. Diameter of circle \t:\n")
    print("3. Circumference of circle \t:\n")

    while True:
        a = int(input("Enter your option no \t:"))
        print("\n")

        if a>3 or a<1 :
            print("\n","-"*4,"Please enter a right option","-"*4,"\n")
        elif a>=1 and a<=3 :
            break
    r = float(input("Enter Radius \n:"))

    if a == 1:
       x = 3.14*(r**2)
       print("Area of circle with radius {} is {}".format(r,x))
    
    elif a == 2:
        x = 2*r
        print(" Diameter of a circle with radius {} is {}".format(r,x))
    elif a==3 :
        x=2*3.14*r
        print("Circumferences of Circle with radius {} is {}".format(r,x))

# Triangle
if choice == 2 :
    print("\n")
    print("\t","*" * 4, "Triangle", "*" * 4,"\n")
    print("1. Find Area of a Triangle\t:\n")
    print("2. Perimeter \t:\n")

    while True:
        a = int(input("Enter your option no \t:"))
        print("\n")

        if a > 2 or a < 1:
            print("\n", "-" * 4, "Please enter a right option", "-" * 4, "\n")
        elif a >= 1 and a <= 2:
            break

    if a == 1:
        h = float(input("Enter height \t:"))
        b = float(input("Enter Base \t:"))
        area = (h*b)/2
        print("\n Area of Triangle with height {} and base {} is {}".format(h,b,area))
    elif a == 2:
        s1 = float(input("Enter first side \t:"))
        s2 = float(input("Enter second side \t:"))
        b = float(input("Enter Base \t:"))
        P = s1+s2+b
        print("\n Perimeter of Triangle with First side {}, Second side {} and base {} is {}".format(s1,s2, b, p))

# Square
if choice == 3:
    print("\n")
    print("\t","*" * 4, "Square", "*" * 4,"\n")
    print("1. Find Area of Square\t:\n")
    print("2. Perimeter of Square \t:\n")

    while True:
        i = int(input("Enter your option no \t:"))
        print("\n")

        if i > 2 or i < 1:
            print("\n", "-" * 4, "Please enter a right option", "-" * 4, "\n")
        elif i >= 1 and i <= 2:
            break

    a = float(input("Enter side length of square \n:"))

    if i == 1:
        x = (a**2)
        print("Area of square with side length {} is {}".format(a, x))

    elif i == 2:
        x = 4*a
        print(" Diameter of a Square with side length {} is {}".format(a, x))
