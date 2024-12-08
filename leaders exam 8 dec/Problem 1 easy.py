def sum_of_positive(numbers):
    total = 0
    # გადდავუვლით ყველა რიცხვს numbers ში 
    for i in numbers:
        #თუ რიცხვი დადებითია დავუმატებთ ჯამს
        if i > 0:
            total += i

    return total

print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([-1, -2, -3, -4]))
print(sum_of_positive([]))