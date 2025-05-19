# Try it out - Program that reads actor grades from a file and stores these to a 2D list.

# Extend the actor grades file and program as follows:
# Alter the data file, separating name into first name and surname, and adding in ‘year of study’ as an additional element.
# Update the print function to accommodate the changes in step 1.
# Add a method to prompt the user for input of a ‘surname’ prior to searching and returning relevant list items should a match be located within the list.

# read in the data file, ignoring the '# comments' and append to a list
# def read_file():
#     source_file = open("actor_grades.txt")
#
#     # manual method for searching each string for commas
#     for each_row in source_file:
#         start = 0
#         string_builder=[]  # list to hold each each_row
#         if not each_row.startswith("#"):  # ignoring the header comment in the data file
#             for index in range(len(each_row)):
#                  if each_row[index] == ',' or index == len(each_row)-1:
#                     string_builder.append(each_row[start:index])  # list builder
#                     print(string_builder)
#                     start = index + 1
#             actor_grade_list.append(string_builder)  # add list to outer list
#             print(actor_grade_list)
#         else:
#             print('Commented row - ignoring')
#     source_file.close()
# # ********************************************************************
# # ENTRY POINT TO PROGRAM
# # define an empty list with scope across the functions
# actor_grade_list = []

# read in data for processing within the menu


def read_file():
    infile = open("actor_grades.txt")
    # optimised method using .split()
    for row in infile:
        if not row.startswith("#"):  # ignore the header comment in the data file
            row = row.rstrip('\n').split(', ') # strip & split
            #print(row)
            actor_grade_list.append(row)  # each element now contains a 'row’
            #print(actor_grade_list)]
    infile.close()


def print_summary():
    total_score = 0
    for actor_profile in range(len(actor_grade_list)):
        print(actor_grade_list[actor_profile][0],actor_grade_list[actor_profile][1], \
            actor_grade_list[actor_profile][2], actor_grade_list[actor_profile][3], actor_grade_list[actor_profile][4], sep=' -> ')
        total_score += float(actor_grade_list[actor_profile][4])

    print('\nCombined Scores:',format(total_score,'.2f'))
    print('Average Score:',format(total_score/len(actor_grade_list),'.2f'))


def my_minimum(act_g_lst):
    minimum = act_g_lst[0] #[B009, Ethan Hunt, 20]

    for item in act_g_lst:
        if item[4] < minimum[4]: # Is 20 < 30
            minimum = item
    return minimum

def actor_search ():
    again = 'y'
    while again == 'y':
        name = input("Which Actor do you wish to search for? ")

        for each_actor in actor_grade_list:
            # [B001, James, Bond, 1, 45]
            if name in each_actor:
                print("Sucess - found")
                print(each_actor[0],each_actor[1],each_actor[2], sep=' -> ')
        else:
            print("Search unsucessful")

        again = input ('Search again?').lower()


#example to show how you might extract elements from a list into a dictionary
# e.g {'James': 'UG', 'Daniel': 'PG', 'Dr': 'PG', 'Jonny': 'UG', 'Ethan': 'UG'}
def element_extractor(act_g_lst):
    actor_summary = {}
    for each_actor in act_g_lst:
        actor_summary[each_actor[1]] = each_actor[5]
    print(actor_summary)



#example to count occurrences of strings in a list
# e.g output
# UG:  3
# PG:  2
def tally_studType(aL):
    stud_type_dict = {}
    for each_actor in aL:
        #[B001, James, Bond, 1, 45, UG]
        if each_actor[5] in stud_type_dict:
            # if dictionary already contains a key for UG or PG, then add 1 to that key value.
            stud_type_dict[each_actor[5]] = int(stud_type_dict[each_actor[5]]) + 1
        else:
            #creeate a new dictionary for either UG or PG and assign a value of 1
            stud_type_dict[each_actor[5]] = 1

    for key, value in stud_type_dict.items():
        print(key + ': ', value)




# ********************************************************************
# ENTRY POINT TO PROGRAM
# define an empty list with scope across the functions
actor_grade_list = []


# read in data for processing within the menu
read_file()
print_summary()
print(my_minimum(actor_grade_list))

element_extractor(actor_grade_list)

tally_studType(actor_grade_list)

actor_search()

print("finished")
