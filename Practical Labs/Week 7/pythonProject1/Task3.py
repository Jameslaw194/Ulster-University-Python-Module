import random

def sorting(values):
    n = 2
    values_copy = values.copy() #copy list

    values_copy.sort() #sort the list
    del values_copy[:n] #remove smallest
    del values_copy[-n:] #remove largest

    print(values_copy)


original_list = random.sample(range(1, 101), 20)
