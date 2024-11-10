import random
from words import word_list

def get_word():
    word = random.choice(word_list) #რანდომად ვირჩევთ სიტყვას
    return word.upper()

def play(word):
    word_completion = "_" * len(word) #დაიბეჭდება იმდენი _ რამდენი ასოცაა სიტყვაში გამოსაცნობი
    guessed = False
    guessed_letters = [] #ამ list ში ინახავს გამოცნობილ ასოებს 
    guessed_words = []
    tries = 6 #ცდების რიცხვი 
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0: 
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #მეთოდი isalphaამოწმებს არის თუ არა შეტანილი ასო "ანბანური"
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1 #როცა არასწორ ასოს მივუთითებთ tries გამოაკლდება ერთი 
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!") 
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
# 21-იდან 54-მდე შემოდის გამოსაცნობი სიტყვა და განხილულია ყველა ვარიანტი როცა ასო სწორია და როცა არ არის სწორი თუ გამოცნობილი ასო სწორია 32 ხაზის გამოყენებით
#დაემატება list-ს რომელიც ტერმინალში გამოსახული იქნება _ _ _ _ _ სახით და ჩაჯდება გამოცნობილი ასოს ადგილას 
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): 
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # საბოლოო მდგომარეობა თავი ტანი ორივე ხელი და ორივე ფეხიც
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # თავი ტანი ორივე ხელი და ერთი ფეხი
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # თავი ტანი და ორივე ხელი
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # თავი ტანი და ერთი ხელი
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # ტანი
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # თავი
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # საწყისი ცარიელი მდგომარეობა
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y": # ეს კოდის ნაკუწი სთავაზობს მომხმარებელს თავიდან დაწყება უნდა თუ არა
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()