import calendar
y = int(input("Enter Year : "))
m = int(input("Enter Month : "))

print("\n\n","="*15,"Calender of {}/{}".format(m,y),"="*15)
print(calendar.month(y,m))
