from datetime import datetime,timedelta
import pandas as pd
from pandas_ods_reader import read_ods
df = read_ods('/home/bus.ods',1)
source = list(df['Source'])
s = set(source)
s = list(s)
dest = list(df['Destination'])
col = list(df.columns)
l = len(col)
ln = len(source)
print(s)
inp = input("Enter source station : ")
inp1 = input("Enter Destination station : ")
now = datetime.now()
cu= now.strftime("%H:%M")
cu1=datetime.now() + timedelta(hours=1)
cu1=cu1.strftime("%H:%M")

for i in range(ln):
    for j in range(ln):
        if i == j:
            if source[i]==inp and dest[j]==inp1:
                val=list(df.loc[i])
for i in range(l):
        if col[i]>cu and col[i]<cu1:
            print("Time {} to {} bus are : {}".format(cu,cu1,val[i]))
