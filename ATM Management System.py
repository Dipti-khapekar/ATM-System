class ATM:
    def __init__(self,account_holder,pin,balance=0):
        self.account_holder = account_holder
        self.__pin = pin
        self.__balance = balance

    def check_pin(self):
        entered_pin = int(input("Enter PIN:"))
        if entered_pin == self.__pin:
            return True
        else:
            print("Invalid PIN!")
            return False

    def check_balance(self): 
        if self.check_pin():
            print(f"Available Balance:  {self.__balance}")

    def deposit(self):
            if self.check_pin():
                amount = float(input("Enter amount to deposit:₹"))
                if amount > 0:
                    self.__balance += amount
                    print(f"₹{amount} deposited successfully:")
                    print(f"Current Balance: ₹{self.__balance}")
                else: 
                    print("Invalid amount!")


    def withdraw(self):
        if self.check_pin():
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= self.__balance: 
                self.__balance -= amount
                print(f"₹{amount} withdraw successfully.")
                print(f"Remaining Balance: ₹{self.__balance}")
            else:
                print("Insufficient Balance!")

    def change_pin(self):
        if self.check_pin():
            new_pin = int(input("Enter new PIN"))
            self.__pin = new_pin
            print("PIN chenged successfully!")

#Creating an object
user1 = ATM("Daksh",1234,10000)

while True:  #looping system
    print("\n===== ATM MANAGEMENT SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Mony")
    print("3. Withdraw Mony")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        user1.check_balance()

    elif choice == "2":
        user1.deposit()

    elif choice == "3":
        user1.withdraw()

    elif choice == "4":
        user1.change_pin()

    elif choice == "5":
        print("Thank you for using ATM!") 
        break
        
    else:
        print("Invalid choice Please try again.")