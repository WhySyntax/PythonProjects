from Functions.TheFuncts import Functs as f
sentence=input('Enter a sentence ')
ctr=sentence.count(' ')+1
if ctr==1:
    print('There is 1 word in the sentence "',sentence,'"')
else:
    print('There are ',ctr,' words in the sentence "',sentence,'"')
ctr=0
for x in sentence:
    if x==' ':
        ctr+=1
ctr+=1
if ctr==1:
    print('There is 1 word in the sentence "',sentence,'"')
else:
    print('There are ',ctr,' words in the sentence "',sentence,'"')
ctr=0
ctr2=len(sentence)
while ctr2>0:
    ctr2-=1
    if sentence[ctr2]==' ':
        ctr+=1
ctr+=1
if ctr==1:
    print('There is 1 word in the sentence "',sentence,'"')
else:
    print('There are ',ctr,' words in the sentence "',sentence,'"')
ecnetnes=f.eman(sentence)
print('sdrawkcab ',sentence,' si ',ecnetnes)
number=f.int2()
if number>100:
    print("it must be smaller than 100")
else:
    print('the factorial of ',number,' is ',f.factorial(number))
factors,isprime=f.factors(number)
print('the factors of ',number,'are',factors)
print(isprime)
