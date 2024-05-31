# import random

# random_words = ["python", "css" , "html" , "swift" , "java" , "javascript"]

# #ავირჩიოთ random-ად სიტყვა ლისტიდან random_words

# chosen_word = random.choice(random_words)
# displayed_word = ["_" for _ in chosen_word] #ლისტი ქვედატიირების 
# attempts = 8 #ცდების რიცხვი 

# print("Welcome to my game ")

# while attempts > 0 and "_" in displayed_word:
#     print("\n" + ' '.join(displayed_word))
#     guess = input("Guess a letter: ").lower()
#     if guess in chosen_word:
#         for index, letter in enumerate(chosen_word):
#             if letter == guess:
#                 displayed_word[index] = guess
#     else:
#         print("that letter doesn't appear in the word.. idiot !!! try again")
#         attempts -= 1
#         while attempts <= 1:
#             print("ah god okay lats try ")

# if "_" not in displayed_word:
#     print("you won ! ")
#     print(' '.join(displayed_word))
#     print("you survived :D ")
# else:
#     print("you run out of attempts the word was: " + displayed_word)
#     print("you lost loooser")



print(type(10))