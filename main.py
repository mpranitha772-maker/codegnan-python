#creating tables
#account_table = {username:password}
#users_table = account:[amount, name, email]

account_table = {1234:456,
                 1235:457}

users_table = {1234:[1000, 'pranitha', 'mpranitha772@gmail.com'],
               1235:[500, 'mani', 'mani8108@gmail.com']}

#functions

#login functions
def login(username:int, password:int):
    if username in account_table:
        if password == account_table[username]:
            print("login successfull")
            return True
        else:
            print("Check with your credintials")
            return False
    else:
        print("user not found")
        return False

#withdraw function defination
def withdraw(account:int, withdraw_amount:int):
    if account in users_table:
        # checking for sufficient balance
        if withdraw_amount <= users_table[account][0]:
            users_table[account][0] -= withdraw_amount  # deducting amount from balance
            print(f'{withdraw_amount} Withdraw Successful and current balance is :{users_table[account][0]}')

        else:
            print('Insuffcient Balance')
            
    else:
        print('User not found')

#deposit
def deposit(account:int, deposit_amount:int):
    if account in account_table:
        users_table[account][0] += deposit_amount  # adding amount to balance
        print(f'{deposit_amount} Deposit Successful and current balance is :{users_table[account][0]}')
    
    else:
        print('User not found')
    

#tranfer function defination
def transfer(sender:int, receiver:int, transfer_amount:int):
    if sender in users_table:
        receiver_ac = int(input('Enter receiver account number: '))
        if receiver_ac in users_table:
            if users_table[sender][0] >= transfer_amount: 
                users_table[sender][0] -= transfer_amount
                users_table[receiver][0] += transfer_amount
                print(f'{transfer_amount} transferred successfull and current_balance is :{users_table[sender][0]}')
            else:
                print('Insufficient Balance')
        else:
            print('Reciever account not found')
    else:
        print('User account not found')
    

#ministatement function defination
def ministatement(account:int):
    print("ministatement page development under proccessing")

#balance enquiry function
def balanceEnquiry(account:int):
    if account in users_table:
        print(f"current balance is: {users_table[account][0]}")
    else:
        print("user not found")

#logout
def logout():
    print("logout successfully")
    exit()

#main()
if __name__ == "__main__":
    print("Welcome to codegnan bank application")
    username = int(input("Enter your account number"))
    password = int(input("Enter your password"))
    login_val = login(username = username, password=password)
    while login_val:
        operations = ("1. withdraw \n",
        "2. deposit \n",
        "3. transfer \n",
        "4. ministatement \n",
        "5. balanceEnquiry \n",
        "6. logout \n"
        )
        print(*operations)
        choice = int(input("Select your operation:"))
        if choice == 1:
           withdraw(account = username, withdraw_amount = int(input('Enter amount to withdraw: '))) #taking default-without amount as 0
        elif choice == 2:
           deposit(account = username , deposit_amount = int(input('Enter amount to deposit: '))) 
        elif choice == 3 :
           transfer(sender = username, receiver = username, transfer_amount = int(input('Enter the amount to transfer: ')))
        elif choice == 4:
           ministatement(account = username)
        elif choice == 5:
           balanceEnquiry(account = username)
        elif choice == 6:
           logout()
        else:
           print('Please select the operations in between 1 to 6')

