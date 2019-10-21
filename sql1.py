import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='7830507740',database='student')
cu = mydb.cursor()
cu.execute('create table student(Name varchar(25),Class varchar(10),Math int(5),computer int(5),physics int(5),grade varchar(5))')
sql = 'insert into student(Name,Class,Math,computer,physics,grade) values(%s,%s,%s,%s,%s,%s)'
s = int(input("Enter how many data : "))
data = []
for i in range(s):
    data.clear()
    Name = input("Enter name:")
    Class = input("Enter class name:")
    Math = input("Enter math marks:")
    computer = input("Enter computer marks:")
    physics = input("Enter physics marks:")
    grade = input("Enter grade:")
    data.extend([Name,Class,Math,computer,physics,grade])
    cu.execute(sql,data)
    mydb.commit()
cu.execute('select * from student')
table = cu.fetchall()
#print(table)
df = pd.DataFrame(table,columns=('Name','Class','Math','Computer','Physics','Grade'))
#print(df)
Name = list(df['Name'])
columns = list(df.columns)
print(Name)

while True:
    l=0
    input1 = input("Enter Name of Student (Enter e for exit) : ")
    #input2 = input("Enter Subject(Math,Computer,Physics) or Grade :")
    for i in Name:
        if i == input1:
            l = Name.count(input1)
            val = Name.index(input1)
            va = list(df.loc[val])
            #print(va)
    if l>0:
        input2 = input("Enter Subject(Math,Computer,Physics) or Grade:")
        for i in columns:
            if i == input2:
                index = columns.index(input2)
        if input2 == 'Grade':
            print("\nName : {} \nClass : {} \nGrade :{}\n".format(input1,va[1],va[index]))
        else:
            print("\nName : {} \nClass : {} \n{} Score : {}\n".format(input1,va[1],columns[index],va[index]))
    if input1 == 'e':
        print('Bye')
        break
