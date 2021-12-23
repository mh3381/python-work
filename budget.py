class Budget():
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.total = food + clothing + entertainment

    def deposit(self, category, amount):
        setattr(self, category, getattr(self, category) + amount)
        self.total += amount   
        print(f"Deposited {amount} to {category}")

    def sufficient_funds(self, category, amount):
        return getattr(self, category) >= amount    

    def withdraw(self, category, amount):
        if self.sufficient_funds(category, amount):
            setattr(self, category, getattr(self, category) - amount)
            self.total -= amount 
            print(f"Withdraw {amount} from {category}")   
        else:
            print("Insuficient balance!")    

    def transfer(self, cat_from, cat_to, amount): 
        if self.sufficient_funds(cat_from, amount):
            self.withdraw(cat_from, amount)
            self.deposit(cat_to, amount)       

    def __str__(self):
        return f"Food: {self.food}\nClothing: {self.clothing}\nEntertainment: {self.entertainment}\nTotal: {self.total}" 


    # Examples:
budget = Budget(200, 80, 1000)
print(budget)
budget.deposit('clothing', 20)
budget.withdraw('entertainment', 500)
budget.transfer('entertainment', 'food', 100)
print(budget)           