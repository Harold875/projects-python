class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    
    def __str__(self):
        message = ''
        distance = (30 - len(self.name)) // 2
        message += ('*'*distance) + f'{self.name}' + ('*'*distance) + '\n'
        for registro in self.ledger:
            num_str = str("%.2f" % registro['amount'])
            description = registro['description'][0:23]
            message += description + ((23 - len(description))+(7-len(num_str)))*' ' + num_str + '\n'
        message += f'Total: {self.get_balance()}'
        return message
    
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True
        
    def get_balance(self):
        cantidad = [registro['amount'] for registro in self.ledger]
        return sum(cantidad)
            

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True
        
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True



def create_spend_chart(categories):
    pass


# pruebas
# food = Category("Food")
# food.deposit(123)
# food.withdraw(50)
# print(food.get_balance())
# print(food)
# a = -10
# print(str(a))

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)