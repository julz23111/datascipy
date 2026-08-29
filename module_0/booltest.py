class chckingsAuthID:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance, 0

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

    def setBalance(self, newBalance):
        if newBalance < 0:
            print("ERROR - balance cannot be negative")
        else:
            self.balance = newBalance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
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
    min = 1000
    max = 9999
    c = chckingsAuthID(min,max)
    print(f'Create a new account id: {c.getId()} with a balance of ${c.getBalance()}')





    




main()

    

