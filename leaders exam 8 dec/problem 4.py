def longest_substring_lenght(s):
    max_lenght = 0 #მაქსიმალური სიგრძე
    left = 0
    # გადავუვლი ყველა სიმბოლოს სტრინგში 
    for i in range(len(s)):
        #ამოწმებს თუ არსებულ სტრინგში არისრამე სიმბოლო გამეორებული
        while s[i] in s[left:i]:
            left += 1
        # მაქსიმალური სიგრძის განახლება
        max_lenght = max(max_lenght, i - left + 1)
    return max_lenght

print(longest_substring_lenght("abcabcbb"))
print(longest_substring_lenght("bbbb"))
print(longest_substring_lenght(""))
print(longest_substring_lenght("pwwkew"))