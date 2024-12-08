#  check if two strings are anagrams 
from collections import Counter

def anagrams(s , s1):
    # ვალაგებთ სტრინგებს ვწერთ ყველას lower ში და ვუშლი გამოტოვებებს ხარვეზების გარეშე შესამოწმებლად მაინცცც რაიცი რახდება 
    s = s.replace(" " , "").lower()
    s1 = s1.replace(" " , "").lower()   
    # counter ფუნქცია შექმნის რაიმე სტრინგიდან ცალკეული ყველა სიმბოლოების დიქტს მაგალითად: counter(silent) = {"s" : 1 , "i" : 1, "l" : 1 , და ა.შ}
    return Counter(s) == Counter(s1)

print(anagrams("listen" , "silent"))
print(anagrams("triangle" , "integral"))
print(anagrams("apple" , "pale"))
print(anagrams("a" , "a"))
print(anagrams("rat" , "car"))