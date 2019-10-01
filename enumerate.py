a = [[1,4,5],[2,3,4],[1,2,0]]
print("lsit = ",a,"\n")

print("="*10,"Dividing sublist method 'Enumerate()'","="*10,"\n")
for i,v in enumerate(a):        # use to unpake a list in a list 
    print(i,v)

print("\n","="*10,"first multiply the list no with the position of no and add total with enumerate()","="*10,"\n")
for sublist in a:
    val = [i*v for i,v in enumerate(sublist)]
    print(sum(val))

print("\n","="*10,"first multiply the list no with the position of no and add total with out enumerate()","="*10,"\n")
for i,v,x in a:
    val = (i*0)+(v*1)+(x*2)
    print(val)
