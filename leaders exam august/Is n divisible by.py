def is_divisible(*n):
    first = n[0]
    for i in n[1:]:
        if first % i != 0:
            return False
    
    
    return True

#მეორე 7kyu 