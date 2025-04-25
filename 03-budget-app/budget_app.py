class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    
    def __str__(self):
        message = ''
        distance = (30 - len(self.name)) // 2
        message += ('*'*distance) + f'{self.name}' + ('*'*distance) + '\n'
        for registro in self.ledger:
            num_str = str(registro['amount'])
            message += registro['description'][0:23] + ' '*(7-len(num_str)) + num_str + '\n'
        return message
    
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):
        cantidad = [registro['amount'] for registro in self.ledger]
        return sum(cantidad)
            

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True



def create_spend_chart(categories):
    pass


# pruebas
# food = Category("Foods")
# food.deposit(123)
# food.withdraw(50)
# print(food.get_balance())
# print(food)
# a = -10
# print(str(a))