def password(FirstPas,SecondPas):
    FirstPas = input("Enter your password:")
    SecondPas = input("Re-enter the password:")
    if FirstPas == len(SecondPas):
        return "Password was entered correctly"
    else:
        return "Please enter the correct password"

#Withdraw

def withdraw(balance,amount):
    if amount > 0:
        if amount <= balance:
            balance -=amount
            print(f"withdrew {amount}$,Balance: {balance}$")
        else:
            print("Insuficient funds. Try again.")
    else:
        print("Insufficient funds. Enter positive value.")
    return balance

#Deposit

def deposit(balance,amount):
    if amount > 0:
        balance +=amount
        print(f"Deposited {amount}$,\nBalance: {balance}$")
    else:
        print("Invalid value. Enter positive value.")
    return balance

#Previous and Current Balance
First = input("Enter your Email:")
Second = input("Re-enter the Email:")
if First == Second:
    print("Email was entered correctly")
else:
    print ("Please enter the correct Email")

FirstPas = input("Enter your password:")
SecondPas = input("Re-enter the password:")
if FirstPas == SecondPas:
    print("Password was entered correctly")
else:
    print("Please enter the correct password")

starting_balance = float(input("Enter the balance: "))
current_balance = starting_balance
print(f"The balance is {current_balance}$")
while True:
    print("1. Withdraw")
    print("2. Deposit")
    choice = input("Enter your choice 1 or 2:")
    if choice == "1":
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        current_balance = withdraw(current_balance, withdrawal_amount)
    elif choice == "2":
        deposit_amount = float(input("Enter the deposit amount: "))
        current_balance = deposit(current_balance, deposit_amount)
    else:
        print("Invalid choice. Please enter 1 or 2.") 