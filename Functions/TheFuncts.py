class Functs:
    def float2(inp="Pick a number ",inp2="Numbers only please"):
        """Asks the user for a number and forces them to repeat if they put in anything other than valid numbers"""
        while True:
            try:
                var=float(input(inp))
                break
            except ValueError:
                print(inp2)
        return var
    def int2(inp="Pick a number ",inp2="Numbers only please"):
        """Asks the user for an integer and forces them to repeat until they give a valid one"""
        while True:
            try:
                var=int(input(inp))
                break
            except ValueError:
                print(inp2)
        return var
    def intrestfinder(x,y,z):
        """intrestfinder(intrestgiven,cashputin,timewaited) gives the amount of money in a bank account after the given amount of years with the given amount of intrest"""
        a=y*(x/100+1)**z
        b=y*(1+z*(x/100))
        c=(a,b)
        return c
    def Fibo(a):
        """Gets the Xth number in the fibonachi sequence"""
        if a==1:
            return 0
        elif a==2:
            return 1
        else:
            return Functs.Fibo(a-1)+Functs.Fibo(a-2)
    def LineEquation(a,b):
        """Gets the equation of a line using two points found on the line"""
        c=(b[1]-a[1])/(b[0]-a[0])
        d=a[1]-c*a[0]
        return 'y='+str(c)+'x+'+str(d)
    def fileopener(a):
        """Opens a file and puts all of the lines in a list"""
        b=[]
        try:
            with open(a,'r') as words:
                b = words.readlines()
        except FileNotFoundError as i:
            print(i)
        else:
            return b
    def wordcounter(a):
        """Tells you the amount of words in a given sentence and puts them in a list"""
        b=[]
        ctr=1
        d=0
        for x in range(len(a)):
            if a[x]==' ':
                ctr+=1
                b.append(a[d:x])
                d=x+1
        b.append(a[d:])
        return b
    def vowelcounter(a):
        """Returns the amount of vowels in a given word"""
        b=0
        for x in range(len(a)):
            if a[x]=='a' or a[x]=='e' or a[x]=='i' or a[x]=='o' or a[x]=='u':
                b+=1
        return b
    def factors(a):
        """Returns a list containing all of the factors a number has as well as weather the number is prime or composite"""
        b=[]
        for x in range(1,a+1):
            if a%x==0:
                b.append(x)
        if len(b)==2:
            c=str(a)+' is a prime number'
        else:
            c=str(a)+' is a composite number'
        return b,c
    def factorial(a):
        """Returns the factorial of any given number"""
        b=1
        c=1
        while b<=a:
            c*=b
            b+=1
        return c
    def eman(a):
        """Returns a given string typed backwards"""
        b=len(a)-1
        c=''
        while b>=0:
            c+=a[b]
            b-=1
        return c
