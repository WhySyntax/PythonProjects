def fileopener(a):
    b=[]
    try:
        with open(a,'r') as words:
            b = words.readlines()
    except FileNotFoundError as i:
        print(i)
        quit()
    else:
        return b,len(b)
def wordcounter(a):
    b=[]
    ctr=1
    d=0
    for x in range(len(a)):
        if a[x]==' ':
            ctr+=1
            b.append(a[d:x])
            d=x+1
    b.append(a[d:])
    return b,ctr
def vowelcounter(a):
    b=0
    for x in range(len(a)):
        if a[x]=='a' or a[x]=='e' or a[x]=='i' or a[x]=='o' or a[x]=='u':
            b+=1
    return b
file=input('Which file do you wish to open? ')
linewordctr=[]
wordvowelctr=[]
numofwords=0
filelist,linesinfile=fileopener(file)
for x in range(linesinfile):
    words,a=wordcounter(filelist[x])
    numofwords+=a
    linewordctr.append(filelist[x])
    linewordctr.append(a)
    for y in range(a):
        numofvowels=vowelcounter(words[y])
        wordvowelctr.append(words[y])
        wordvowelctr.append(numofvowels)
maxfinder=wordvowelctr[1]
for x in range(len(wordvowelctr)):
   if type(wordvowelctr[x])==int:
       if wordvowelctr[x]>maxfinder:
           maxfinder=wordvowelctr[x]
print('There are ',linesinfile,' lines in the file ',file)
print('There are ',numofwords,' words in the file ',file)
print('The word in the file ',file,' with the most vowels is ',wordvowelctr[wordvowelctr.index(maxfinder)-1],' and it has ',maxfinder,' vowels')
