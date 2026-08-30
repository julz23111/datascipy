class chckingsAuthID:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.balance = 0.00

    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = float(input("Enter new id: "))
        if newId <1000 or newId > 9999:
            print("ERROR - id must be between 1000 and 9999, and must be a 4 digit number")
        else:
         self.id = newId

    def getBalance(self):
        return self.balance


    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("ERROR - deposit must be a positve amount")
        else:
            self.balance += amount

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount < 0:
            print("ERROR - withdraw must be a positve amount")
        elif amount > self.balance:
            print("ERROR - withdraw cannot exceed balance")
        else:
            self.balance -= amount
        

def main():
    user_id = float(input("Enter your 4 digit id: "))

    if user_id < 1000 or user_id > 9999:
     print("ERROR - id must be between 1000 and 9999, and must be a 4 digit number")
     return

    c = chckingsAuthID(user_id, 0.00)

    print(f'Your id is {c.getId()} and your balance is ${c.getBalance():.2f}')

    if choice := input("Would you like to make a deposit or withdrawal? Enter 'd' for deposit or 'w' for withdraw':").lower() == 'd':
        c.deposit()
        print(f'Your new balance is ${c.getBalance():.2f}')
    elif choice == 'w':
        c.withdraw()
        print(f'Your new balance is ${c.getBalance():.2f}')
    else:
        print("Invalid choice. Please enter 'd' for deposit or 'w' for withdraw.")

        return
        

main()


#   c= chckingsAuthID(user_id,0.00)
#   user_id = float(input("Enter your 4 digit id: "))

#   if user_id < 1000 or user_id > 9999:
#     print("ERROR - id must be between 1000 and 9999, and must be a 4 digit number")
#     return
#   elif user_id >= 1000 and user_id <= 9999:
#     choice=  print(f'Your id is {c.getId()} and your balance is ${c.getBalance():.2f} would you like to make a deposit or withdrawal?')/
#           input("Enter 'd' for deposit or 'w' for withdraw: "))
    

