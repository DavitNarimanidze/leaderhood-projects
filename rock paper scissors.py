import random 

options = ("rock" , "paper" , "scissors")

player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter Your Choice: rock , paper or scissors: ")

print(f"player: {player}")
print(f"computer : {computer}")


if player == computer:
    print("it's a tie! ")