# Unique In Order 6kyu

def unique_in_order(sequence):
    new_list = []
    for i in sequence: 
        if len(new_list) < 1 or not i == new_list[len(new_list) -1]:
            new_list.append(i)
    return new_list 