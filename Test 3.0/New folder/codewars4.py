
# How many are smaller than me? 7kyu

def smaller(arr):
    if len(arr) == 1: 
        return [0]
    count = 0 
    
    
    for i in arr[1:]:
        if arr[0] > i:
            count = count + 1
    return [count] + smaller(arr[1:])