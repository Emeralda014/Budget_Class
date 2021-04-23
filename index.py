class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        
    def deposit(self, money):
        self.amount += money
        print(f"you have deposited {money} into {self.category} budget")
    def check_balance(self):
        return self.amount
    
    def withdraw(self, money):
        self.amount -= money
        print(f"you have withdrawn {money} ")
        
    def transfer(self, money):
        self.amount -= money
        return money
    
food = Budget("food", 1000)    
clothing = Budget("clothing", 1500)    
entertainment = Budget("entertainment", 1400)
    
    
cash = int(input('how much do you want to deposit to your food budget :'))
food.deposit(cash)
print(f"your food balance is {food.check_balance()}")
cash = int(input('how much do you want to withdraw from your food budget :'))
food.withdraw(cash)
print(f"your food balance is {food.check_balance()}")
cash = int(input('how mmuch do you want to transfer from food budget to clothing budget? :'))
transfer_fee = food.transfer(cash)
clothing.deposit(transfer_fee)
print(f"your food balance is {food.check_balance()}")
print(f"your clothing balance is {clothing.check_balance()}")