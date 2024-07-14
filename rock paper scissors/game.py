import random



choices = ["rock" , "paper" , "scissors"]


#თამაშის წესები შენახული dict-ში 
rules = {
    "rock" : "scissors",
    "paper" :  "rock",
    "scissors" : "paper"
}

#ფუნქცია რო ავიღოთ კომპიუტერისგან რანდომულად არჩევანი choices ლისტიდან
def get_computer_choice():
    return random.choice(choices)

#ფუნქცია გამარჯვებულის გამოსავლენად 
def get_winner(player , computer):
    if player == computer:
        #როცა ორივე არჩევანი ერთნაირია ფრეა
        return "it's a Tie! "
    elif computer in rules[player]:
        return "You Win! " #მოთამაშე იგებს თუ კკომპიუტერის არჩევანი არის მოთამაშის მოგების ლისტში 
    else: #სხვა შემთხვევაში კომპიუტერი იგებს
        return "computer wins! "
    
#მთავარი ფუნქცია რო ვითასმაშოთ თამაში 
def play_game():
    player_score = 0
    computer_score = 0

    while True:
        #მივიღოთ მოთამაშის არჩევანი
        player_choice = input("Enter Your Choice(rock paper scissors) or 'quit' to stop " ).lower()
        if player_choice == 'quit':
            print("exiting the game! ")
            break
        #შევამოწმოთ არასწორი ინფუთის შემთხვევაში
        if player_choice not in choices:
            print("invalid choice Try Again! ")
            continue
        #მივიღოთ კომპიუტერის არჩევანი
        computer_choice = get_computer_choice()
        print(f"computer chose: {computer_choice}")

        result = get_winner(player_choice , computer_choice)
        print(result)


            #შედეგების მიხედვით update-ბა  ქულები 
        if result == "You Win! ":
            player_score += 1
        elif result == "computer wins! ":
            computer_score += 1

        print(f"score -> you: {player_score} , computer: {computer_score}")

play_game()