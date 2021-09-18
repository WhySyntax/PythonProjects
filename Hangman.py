users=[]
wordsused=[]
wordbank=[]
with open('users.txt','r') as u:
      data=u.readlines()
      for line in data:
            users+=line.split()
with open('HangManWordlist.txt', 'r') as words:
      data = words.readlines()
      for line in data:
                  wordbank+=line.split()
playagain=True
def hangman(a):
      """This function plays hangman"""
      victory=False
      wordbank=[]
      with open('HangManWordlist.txt', 'r') as words:
            data = words.readlines()
            for line in data:
                  wordbank+=line.split()
      import random as rand
      HardMode=rand.randint(0,100)
      word=wordbank[rand.randint(0,len(wordbank)-1)]
      newword=False
      while a.count(word)>0:
            word=wordbank[rand.randint(0,len(wordbank)-1)]
      hiddenword=''
      if HardMode==88:
            attempts=1
      else:
            attempts=len(word)+2
      print("The length of the word you must guess is "+str(len(word))+" letters and you have "+str(attempts)+" lives")
      lettersguessed=[]
      hiddenwordlist=['*']*len(word)
      wordlist=list(word)
      hintletter=rand.randint(0,len(word)-1)
      clue=wordlist[hintletter]
      for x in range(len(wordlist)):
            if clue==wordlist[x]:
                  hiddenwordlist[x]=clue
      lettersguessed.append(clue)
      for x in range(len(hiddenwordlist)):
            hiddenword+=str(hiddenwordlist[x])
      print('The word is',hiddenword)
      print("If you want to quit type 'Quit'")
      while attempts>0:
            guess=input("Guess a letter or whole word ").lower()
            try:
                  float(guess)
                  numguess=True
            except ValueError:
                  numguess=False
            if guess=='quit':
                  victory=False
                  attempts=0
            elif guess=="kabir's admin access":
                  attempts=3333
            elif guess==word:
                  victory=True
                  attempts=0
            elif len(guess)>1:
                  print('only one letter at a time please')
            elif lettersguessed.count(guess)>0:
                  print("You already guessed that try again")
            elif numguess==True:
                  print('letters only please')
            else:
                  lettersguessed.append(guess)
                  if wordlist.count(guess)==0:
                        print("That is not in the word")
                        attempts-=1
                        print(hiddenword)
                  else:
                        for x in range(len(wordlist)):
                              if guess==wordlist[x]:
                                    hiddenwordlist[x]=guess
                        if hiddenwordlist.count('*')==0:
                              victory=True
                              attempts=0
                        else:
                              hiddenword=''
                              for x in range(len(hiddenwordlist)):
                                    hiddenword+=str(hiddenwordlist[x])
                              print(hiddenword)
            if victory==False:
                  if attempts==1:
                        print("You have 1 life remaining use it wisely")
                  else:
                        print("You have "+str(attempts)+" lives left")
      if victory==True:
            print("YOU WON!!! Good for you the word was '",word,"'")
      else:
            print('Guess you failed sorry but the word was "',word,'"')
      a.append(word)
admin=input('who are you? ')
if admin=='I am Kabir the admin of this program':
      addedword=input('what word should be added? ').lower()
      if wordbank.count(addedword)==0:
            with open('HangManWordlist.txt','a')as words:
                  words.writelines('\n'+addedword)
      else:
            print('that word is already in the wordbank')
elif users.count(admin.capitalize())==0:
      print('Welcome ',admin.capitalize())
      with open('users.txt','a+') as u:
            u.writelines('\n'+admin.capitalize())
      users.append(admin.capitalize())
else:
      print('Welcome back ',admin)
while playagain==True:
      hangman(wordsused)
      while True:
            Continue=input('Would you like to play again? ').lower()
            if Continue=="yes":
                  playagain=True
                  break
            elif Continue=='no':
                  playagain=False
                  break
            else:
                  print("write yes or no")
