#this is a page for day 2 of python
#Areas=['hallway',11.25,'kitchen',18,'living room',20,'bedroom',10.75,'bathroom',9.5]
areas=[]
while True:
   try:
      rooms=int(input("How many rooms are in your house? "))
      break
   except ValueError:
      print("Only put the number not any letters or symbols")
for x in range(rooms):
   room=input("What is your "+str(x+1)+" room? ")
   areas.append(room)
   while True:
      try:
         area=float(input("How big is this room in square meters? "))
         break
      except ValueError:
         print("Only put the number not any letters or symbols")
   areas.append(area)
averagefinder=0
ctr=0
maxfinder=0
for x in areas:
   if type(x)==float:
       averagefinder=averagefinder+x
       ctr=ctr+1
       if x>maxfinder:
           maxfinder=x
print("The average area of the rooms in the house is "+str(averagefinder/ctr)+"sqm.")
print("The biggest room in the house is the "+areas[areas.index(maxfinder)-1]+" and it has "+str(maxfinder)+"sqm of space.")
print(areas)
