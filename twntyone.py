import random

def dealcards_player1(fullpack, pack, tot):
 global grand

 #random.shuffle(pack)

 print("Your cards are \n")
 for m in range (0,2):
  print(pack[m] )
  tot=tot+(fullpack[pack[m]])#pack is calling the card from the dictionary. Pack is a string like '2 of spades'
 grand=tot


 print (grand)

#(fullpack[pack[i]]))
#print(fullpack)
#print (pack[0])
#print(fullpack['10 of clubs']+fullpack[pack[0]])#pack[0] is first value of 'pack' so here 2 of spades. This is placed into 'fullpack' which calls corresponding value 2



def twist_player1(fullpack, pack, grand):


    #random.shuffle(pack)
    print("Your cards are \n")
    i=random.randint(1,51)
    print(pack[i])
    new = (fullpack[pack[i]])


    if 'Ace'in pack[i] and grand>11:    #if pack i contains A and grand>11 new=1
          # pack is calling the card from the dictionary. Pack is a string like '2 of spades'
     new=1
    grand = new + grand
    print(grand)
    return new

    # (fullpack[pack[i]]))
    # print(fullpack)
    # print (pack[0])
    # print(fullpack['10 of clubs']+fullpack[pack[0]])#pack[0] is first value of 'pack' so here 2 of spades. This is placed into 'fullpack' which calls corresponding value 2




tot=0



suite=[' of diamonds', ' of spades', ' of hearts', ' of clubs'] #a list of strings

value=['2','3','4','5','6','7','8','9','10','J','Q','K','Ace'] #list of values
pack=[] #blank list
num=[] #create numerical list

#random.shuffle(suite)
#random.shuffle(value)

#produces cards in pack and each corresponding val in num
for sucount in range(0,4): #4suits
    cv = 2 #starting value given
    for s in range (len(value)):#each suit is combined with a value the number of variables in list value

     pack.append(value[s]+suite[sucount])#each suit is combined with a value
     num.append(cv)#corresponding value is added to another list
     if s<8: #value increases only if its less than 10
        cv+=1
     elif s==11: #the value can increase only if its a king
        cv+=1
     elif s == 0:
         cv=2
sucount+=1 #increases loop by 1


compack=zip(pack,num) #combines pack and num with the zip function
#for i in range (0,2):
 #print(str(shuffled[i]))

#for i in range (len(pack)):
   # print(str(pack[i]))
   # i=+i

#random.shuffle(pack)
#pick=random.randrange(0,51)
#for p in range(0,2):
#    print(pack[p])
 #   p=+1
fullpack=dict(compack) # turns this into dictionary so card corresponds to numerical value

random.shuffle(pack)
dealcards_player1(fullpack, pack, tot)
# print(grand)

while grand<21:
 if grand==21:
  print("winner")
  print("final total " + str(grand))
  break

 elif grand<21:
  choice=input("another card? ")
 if choice=="n":
  print("final total " + str(grand))
  break
 elif choice=="y":
  grand=grand+twist_player1(fullpack, pack, grand)#runs the code and adds the return value "new". Pretty neat

 if grand==21:
  print("winner")
  print("final total " + str(grand))
 elif grand > 21:
  print("bust")
  print("final total " + str(grand))

















