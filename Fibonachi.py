def Fibo(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return Fibo(a-1)+Fibo(a-2)
def int2(inp="Pick a number ",inp2="Numbers only please"):
    while True:
        try:
            var=int(input(inp))
            break
        except ValueError:
            print(inp2)
    return var
fib=int2('What value of the fibonachi sequence do you wish to find? ')
print(Fibo(fib-1))
def LineEquation(a,b):
    c=(b[1]-a[1])/(b[0]-a[0])
    d=a[1]-c*a[0]
    return 'y='+str(c)+'x+'+str(d)
p1=[int2('What is your 1st x value? '),int2('What is your 1st y value? ')]
p2=[int2('What is your 2nd x value? '),int2('What is your 2nd y value? ')]
print(LineEquation(p1,p2))
