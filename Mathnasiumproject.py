def int2(a='pick a number ',b='numbers only please'):
    while True:
        try:
            c=int(input(a))
            break
        except ValueError:
            print(b)
    return c
def float2(a='pick a number ',b='numbers only please'):
    while True:
        try:
            c=float(input(a))
            break
        except ValueError:
            print(b)
    return c
import random as r
while True:
    operation=input('What operation do you want +, -, x, or / ')
    if operation=='+':
        break
    elif operation=='-':
        break
    elif operation=='x':
        break
    elif operation=='/':
        break
    else:
        print('+, -, x, or / only nothing else')
hpn=float2('What is your highest possible number ')
lpn=float2('What is your lowest possible number ')
questions=int2('How many questions do you want ')
sheet=[]
for x in range(questions):
    sheet.append(str(r.randint(lpn,hpn))+operation+str(r.randint(lpn,hpn))+'=')
for x in sheet:
    print(x)
