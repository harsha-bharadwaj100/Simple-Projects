class BankAccount:
    def __init__(self, balance, pin) -> None:
        self.bal = balance
        self.pin = pin

    def deposit(self, amt):
        if amt > 0:
            self.bal += amt
            print(f"Amount {amt} deposited!")
        else:
            print("Invalid amount!")

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal -= amt
            print(f"Amount {amt} withdrawn!")
        else:
            print("Invalid amount!")

    def change_pin(self, npin):
        if self.pin != npin:
            print(f"Pin changed from {self.pin} to {npin}!")
            self.pin = npin
        else:
            print("Thw pin is same, please try another pin!")

    def display(self):
        print(f"Your Balance: {self.bal}")


acc = BankAccount(8000, 2535)
acc.display()
acc.deposit(2300)
acc.display()
acc.withdraw(4500)
acc.display()
acc.change_pin(2435)
