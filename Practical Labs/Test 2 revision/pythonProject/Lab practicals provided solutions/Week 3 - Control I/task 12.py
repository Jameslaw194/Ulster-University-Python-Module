# com101 lab week3 q 12
#the chinese animals
#the trick here is to note this is a 12 yr cycle and that
#2000%12 = 8, 2001%12=9, 2004%12=0 etc
#ie we can assign each of the animals the appropriate remainder

year=int(input('What year is it?'))

if year%12 == 8:
    print('It is the year of the Dragon.')
elif year%12==9:
    print('It is the year of the Snake.')
elif year%12==10:
    print('It is the year of the Horse.')
elif year%12==11:
    print('It is the year of the Sheep.')
elif year%12==0:
    print('It is the year of the Monkey.')
elif year%12==1:
    print('It is the year of the Rooster.')
elif year%12==2:
    print('It is the year of the Dog.')
elif year%12==3:
    print('It is the year of the Pig.')
elif year%12==4:
    print('It is the year of the Rat.')
elif year%12==5:
    print('It is the year of the Ox.')
elif year%12==6:
    print('It is the year of the Tiger.')
else:
    print('It is the year of the Hare.')
