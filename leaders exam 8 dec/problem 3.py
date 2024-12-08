def find_missing_number(numbers):
    n = len(numbers) + 1 # რიცხვების total count missing რიცხვის ჩათვლით 
    _sum = n * (n + 1 )//2 # რიცხვების ჯამი 1 დან n-მდე 
    sum_ = sum(numbers) 
    return _sum - sum_

print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([3, 5, 6, 1, 2]))
print(find_missing_number([2]))