# Task 4
# Write a program that opens a specified text file and then displays a list of all the unique words
# found in the file. Hint: store each word as an element of a set.

def task4():
    dup_words = open('sample_words.txt','r')
    set_List = set()
    for each_word in dup_words:
        set_List.add(each_word.rstrip('\n'))
    print(set_List)

def task4b():
    dup_words = open('sample_words.txt','r')
    set_List = set()

    #split out the words from each line
    temp_line_list = []
    for each_line in dup_words:
        temp_line_list = each_line.split()
        for each_word in temp_line_list:
            set_List.add(each_word.rstrip('\n'))

    print(set_List)

    outfile = open('new_file.txt','w')
    while len(set_List) > 0:
        outfile.writelines(set_List.pop())

# MAIN PROGRAM
selection = ''

while(selection != '0'):
    print()
    print('task 1 - approach1 (1a)')
    print('task 1 - approach2 (1b)')
    print('task 2 - (2)')
    print('task 3 - (3)')
    print('task 4 - (4)')
    print('task 4b - (4b - processing paragraphs)')

    selection = input('\nWhich task do you want to execute? ')
    if(selection == '1a'):
        task1a()
    elif(selection == '1b'):
        task1b()
    elif(selection == '2'):
        task2()
    elif(selection == '3'):
        task3()
    elif(selection == '4'):
        task4()
    elif(selection == '4b'):
        task4b()
    else:
        print('error - retry')