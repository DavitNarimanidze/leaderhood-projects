def reverse(sentence):
    words = sentence.split() # თითოეული სიტყვა ცალკე ელემენტი გახდება 

    reversed_ = words[::-1] # აქ ჩანაცვლდება სიტყვების თანმიმდევრობა ესეიგი გადავაბრუნეთ რა :დ 

    revered__ = " ".join(reversed_) # join სიტყვებს სტრინგებად აერთიანებს, ესეიგი უკუქცეულ სიტყვებს ვაერთიანებთ ისევ წინადადებაში 

    return revered__ # რავი return :დ დავაბრუნოთ ჩვენი მიღებული შედეგი 

print(reverse("Hello World"))
print(reverse("Python is great"))
print(reverse("a b c"))
print(reverse(""))
print(reverse(" Spaces "))