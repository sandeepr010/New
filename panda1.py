import pandas as pd
from pandas_ods_reader import read_ods
df = read_ods("/home/sandeep/Sandeep/Python/panda project.ods",1) #importing excel file
print(df)
v = list(df['Vechileno'])
n = list(df['Name'])
mn = list(df['Mobile'])
st = list(df['State'])
r = len(v)
mnm = [int(i) for i in mn] #Coverting mn float values into intiger

while True:
    z = 0
    inp = input("Enter Vechile no or Name or State for Exit press e or E :")
    print("\n")
    if inp == 'E' or inp =='e':
        print("Have a nice day\n")
        break
    for i in range(r):
        if inp == v[i] or inp == n[i] or inp == st[i]:
            z += 1
            print("*"*20,"Record Found","*"*20)
            print("Name : {} \nVechile No : {} \nMobile No : {} \nState : {}".format(v[i],n[i],mnm[i],st[i]),"\n")
    if z == 0:
        print("="*10,"Record for '{}' not found".format(inp),"="*10,"\n")
