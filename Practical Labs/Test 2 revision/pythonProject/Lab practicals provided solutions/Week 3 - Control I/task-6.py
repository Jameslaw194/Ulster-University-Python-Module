# task6 week4/5

# note bool_quest and bool_colour are Boolean variables 
#set passwords
QUEST = 'thegrail'
COLOUR= 'blue'


#request user to input answers

input('What is your name: ')
user_quest = input('What is your quest: ')
user_colour = input('What is your favourite colour: ')

# set Boolean values for the ans to the last two questions
bool_quest = user_quest==QUEST
bool_colour = user_colour==COLOUR

# Determine whether the correct passwords were entered

if (bool_quest and bool_colour) :
    print('OK, on you go then.')
else:
    print('Sorry, you must be cast into the gorge of eternal peril.')





