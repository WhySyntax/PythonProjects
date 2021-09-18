def float2(inp="Pick a number ",inp2="Numbers only please"):
    while True:
        try:
            var=float(input(inp))
            break
        except ValueError:
            print(inp2)
    return var
def int2(inp="Pick a number ",inp2="Numbers only please"):
    while True:
        try:
            var=int(input(inp))
            break
        except ValueError:
            print(inp2)
    return var
print("This function will tell you how much money you can get by sitting on some cash but for it to work properly only write the numbers no symbols or letters.")
endingamount=[]
#this list will contain the amount of cash that you will have after each year
amountgained=[]
#this list will have the amount that you gain after each year
intrest=float2("how much intrest will you get annually? %")
yearswaited=int2("how many years will you wait? ")
moneyputin=float2("how much money will you put in? $")
def intrestfinder(x,y,z):
    """intrestfinder(intrestgiven,cashputin,timewaited) gives the amount of money in a bank account after the given amount of years with the given amount of intrest"""
    a=y*(x/100+1)**z
    b=y*(1+z*(x/100))
    c=(a,b)
    return c
myfunction=intrestfinder(intrest,moneyputin,yearswaited)
print("this is how much money you will have at the end of the last year if you are using compound intrest")
print(myfunction[0])
print("this is how much you will have gained at the end of the last year if you are using compound intrest")
print(myfunction[0]-moneyputin)
print("this is how much money you will have at the end of the last year if you are using simple intrest")
print(myfunction[1])
print("this is how much you will have gained at the end of the last year if you are using simple intrest")
print(myfunction[1]-moneyputin)
