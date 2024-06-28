
accounts = {}
def create_account():
    #აქ ვიღებთ ინფორმაციას მომხმარებლისგან 
    account_number , name , balance = input("შეიყვანეთ აქაუნთის ნომერი , სახელი ,ბალანსი ").split()
    # აქ ვამოწმებთ თუ უკვე არის შექმნილი აქაუნთი 
    if account_number in accounts:
        print("ეს აქაუნთი უკვე არსებობს! ")
    else:
        #აქ იქმნება უკვე account
        accounts[account_number] = {"name" : name ,  "balance" : float(balance)}
        print("აქაუნთი წარმატებით შეიქმნა  ")
create_account()
def perform_transaction():
    #ეხლა ავიღებთ ტრანზაქციის დეტალებს მომხმარებლისგან მაგალითად თანხის რაოდენობას 
    account_number , transaction_type , amount = input("შეიყვანეთ აქაუნთის ნომერი   , ტრანზაქციის ტიპი თანხის შეტანა ან გამოტანა , თანხის რაოდენობა ").split()
    amount = float(amount)
    #ეხლა შევამოწმოთ ის აქაუნთი არსებობს თუ არა რომელიც 20 ხაზზე შეიყვანეს 
    if account_number in accounts:
        if transaction_type == "deposit":
            accounts[account_number] ["balance"] += amount 
        elif transaction_type == "withdraw":
            if accounts[account_number] ["balance"] >= amount:
                accounts[account_number] ["balance"] -= amount
            else:
                print("არასაკმარისი თანხა ბალანსზე ")
                return
        else:
            print("არასწორი ტრანზაქციის ტიპი! ")
            return
        print(f"ტრანზაქცია წარმატებით შესრულდა. ახალი ბალანსი : {accounts[account_number] ["balance"]}")
    else:
        print("აქაუნთი ვერ მოიძებნა")

perform_transaction()

def update_account_info():
    question = input("გინდათ რომ აღადგინოთ აქაუნთის ინფორმაცია?: ")
    if question == "კი":
    #ავიღოთ ახალი ინფორმაცია მომხმარებლისგან აქაუნთის მონაცემების განახლებისთვის
        account_number , new_name = input("შეიყვანეთ აქაუნთის ნომერი , ახალი სახელი: ").split()
        if account_number in accounts:
            accounts[account_number] ["name"] = new_name
            print("აქაუნთის მონაცემები წარმატებით განახლდა ")
        else:
            print("აქაუნთი ვერ მოიძებნა! ")
    elif question == "არა":
        print("თქვენი პასუხი მიღებულია: ")

update_account_info()

def delete_account():
    a = input("გინდათ რომ წაშალოთ აქაუნთი?: ").lower()
    if a == "კი:":
        account_number = input("შეიყვანეთ აქაუნთის ნომერი")

        if account_number in accounts:
            del accounts[account_number]
            print("აქაუნთი წაიშალა წარმატებით!")
        else:
            print("აქაუნთი ვერ მოიძებნა!")
    elif a == "არა":
        print("მადლობთ რომ დარჩით ჩვენთან <3 ")
    else:
        print("Error")
delete_account()

def search_account_info():
    account_number = input("შეიყვანეთ აქაუნთის ნომერი")
    if account_number in accounts: # ანუ აქ მოვძებნით აქაუნთი არსებობს თუ არა და თუ არსებობს გამოვიტანთ ინფორმაციას ამ აქაუნთის შესახებ 
        account = accounts[account_number]
        print(f"account number: {account_number} , name: {account["name"]}, balance: {account["balance"]}")
