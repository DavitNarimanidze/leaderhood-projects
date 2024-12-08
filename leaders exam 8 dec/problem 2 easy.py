import math # დავამატე math მოდული რომ გამოვიყენო floor 


def sum_of_positive(numbers):
    total = 0
    # გადავუვლი ყველა რიცხვს numbers ში 
    for i in numbers:
        #თუ რიცხვი დადებითია ჯამს დავუმატებთ 
        if i > 0:
            total += math.floor((i)) #floor ხდის მთელ რიცხვად 
    return total 

print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([-1.5, 2.7, -3.3, 4.8]))
print(sum_of_positive([]))
print(sum_of_positive([-1, -2 ,-3]))