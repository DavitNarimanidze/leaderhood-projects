def arr_anagrams(s1 , s2):
    # ანაგრამებს უნდა ჰქონდეთ ერთნაირი სიგრძე
    if len(s1) != len(s2):
        return False
    
    # დავასორტირე ორივე სტრინგი და შევადარე
    return sorted(s1) == sorted(s2)

print(arr_anagrams("listen", "silent"))
print(arr_anagrams("hello", "world"))
print(arr_anagrams("triangle", "integral"))