#Next class
from Functions.TheFuncts import Functs as f
students={}
file=input('Which file do you keep your students in? ')
lines=f.fileopener(file)
for x in lines:
    if x[:5]=='name:' or x[:5]=='Name:':
        name=x[6:-1]
    elif x[:4]=='age:' or x[:4]=='Age:':
        age=float(x[5:-1])
    elif x[:6]=='grade:' or x[:6]=='Grade:':
        grade=float(x[7:-1])
    elif x[:8]=='teacher:' or x[:8]=='Teacher:':
        teacher=x[9:-1]
    elif x[0]=='-':
        students[name]={'Age':age,'Grade':grade,'Teacher':teacher,'Everything':{'Age':age,'Grade':grade,'Teacher':teacher}}
students[name]={'Age':age,'Grade':grade,'Teacher':teacher,'Everything':{'Age':age,'Grade':grade,'Teacher':teacher}}
student=input('Which student do you wish to look up? ').lower().capitalize()
studentinfo=input('What info do you wish to look up about '+student+'? ').lower().capitalize()
print(students[student][studentinfo])
