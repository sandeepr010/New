import pandas as pd
from pandas_ods_reader import read_ods
df = read_ods("/home/sandeep/Sandeep/Jupyter/Panda/Country_Area.ods",1)
cl = list(df['Country'])
ccl = list(df.columns)
cn = input("Enter the country Name:")
if(cl.count(cn)>0):
    print('1. Area and 2. population')
    opt = input("Enter an option : ")
    if(opt=='1'):
        pos = ccl.index('Area')
        print(cn,'Area = ',df.loc[cl.index(cn)][pos])
    else:
        pos = ccl.index('Population')
        print(cn,'Area = ',df.loc[cl.index(cn)][pos])
else:
    print("Wrong Inp")
