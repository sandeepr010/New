def lowercaseAlphabets():

    for c in range(97,123):
        print(chr(c), end = ",");

    print(" ");

def uppercasealphabets():

    for c in range(65,91):
        print(chr(c), end = ",");

    print(" ");

print("\n");
print("*"*20,"Uppercase Alphabets","*"*20,"\n");
uppercasealphabets();

print("\n");
print("*"*20,"Lowercase Alphabets","*"*20,"\n");
lowercaseAlphabets();

print("\n\n")

