class ATM:
    def __init__(self,account_id,pin,balance=0):
        self.account_id = account_id
        self.pin = pin
        self.balance = balance
           
    def check_pin(self):
        entered_pin = (int(input("Enter your pin: ")))
        if entered_pin == self.pin:
            return True
        else:
            return False
        
    def check_balance(self):
        if self.check_pin():
            print(f"available Balance: {self.balance}")

    def deposit(self):
        if self.check_pin():
            amount = float(input("Enter amount to deposit"))
            self.amount > 0
            self.balance += amount
            print("{amount} deposit successfully.")
            print("current Balance += {self.balance}")
        else:
            print("Invailid PIN.")

    def withdraw(self):
        if self.check_pin():
            amount = float(input("Enter amount to withdraw."))
            if amount <= self.balance:
                self.balance -= amount
                print("{amount} withdraw successfully.") 
                print("current Balance += {self.balance}")
            else:
                print("Insufficient Balance!")

    def change_pin(self):
        if self.check_pin():
            new_pin = int(input("Enter new pin."))
            self.pin = new_pin
            print("pin changed successfully.")
    
user1 = ATM("dipti",1324, 1300)
 
while True:
    print("welcome to ATM machine.")
    print("1. check_pin")
    print("2. check_balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Change_pin")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user1.check_pin()
    
    elif choice == "2":
        user1.check_balance()

    elif choice == "3":
        user1.deposit()

    elif choice == "4":
        user1.withdraw()

    elif choice == '5':
        user1.change_pin()

    elif choice == "6":
        print("Thant you for using ATM.")
        break

    else:
        print("Invalid pin.")
