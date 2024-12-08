def common_elements(list1 , list2):
    
    common = []
    for i in list1:
        #თუ ელემენტი არის list2 - ში ის დაემატება common სიას 
        if i in list2:
            common.append(i)
    return common

print(common_elements([1, 2, 3], [2, 3, 4]))
print(common_elements([1, 1, 2], [1, 3]))
print(common_elements([], [1, 2]))