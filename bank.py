print("Welcome to BANK")

user_name = input("Please enter your name: ")

current_balance = 1000
op=True

while op:

    print("Choose 1 for deposit")
    print("Choose 2 to withdraw")
    print("Choose 3 to check balance")
    print("Choose 0 to exit")
    choice=input("Please choose transactions:")

    if choice == "1":
        DeP= int(input("Please enter the amount you would like to deposit: "))
        if type(DeP)is int:
            current_balance += DeP
            print(f"Your current balance is: {current_balance}")
    
    elif choice== "2":
        withdraw= int(input("Please enter the amount you would like to withdraw: "))
        if withdraw>current_balance:
            print("It is not possible to withdraw an amount that exceeds the current balance")
        
        else:
            print("You have sufficient amount")
            current_balance -= withdraw
            print(f"Your current balance is: {current_balance}")

    elif choice== "3":
        print(f"Your current balance is: {current_balance}")
    
    elif choice== "0":
        print(f"Thanks for using our service {user_name}")
        op = False
    
    else:
        print("Wrong transaction please try again")

    con = input('would you like to complete another action y/n: ')
    while True:

        if con.lower()== 'n':
            print(f"Thanks for using our service {user_name}")
            op = False
            break

        elif con.lower() == 'y':
            break

        else:
            print('enter y or n')

        con = input('would you like to complete another action y/n: ')
        
        



