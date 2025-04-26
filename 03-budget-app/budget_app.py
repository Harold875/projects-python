class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    
    def __str__(self):
        message = ''
        distance = (30 - len(self.name[0:30])) // 2
        message += ('*'*distance) + f'{self.name}' + ('*'*distance) + '\n'
        for registro in self.ledger:
            num_str = "%.2f" % registro['amount']
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
    data_categories = []
    for category in categories:
        total_retirado = sum([
            abs(registro['amount']) for registro in category.ledger 
            if registro['amount'] < 0
        ])
        data_categories.append((category.name, total_retirado))
        
    porcentaje_total = sum([i[1] for i in data_categories])
    # data_categories.sort(key=lambda el:el[1],reverse=True)    # <- Uncomment to sort
    data_categories_final = []
    string_amount = ''
    for category in data_categories:
        porcentaje_category = (100 * category[1]) / porcentaje_total
        string_amount = category[0] if len(category[0]) > len(string_amount) else string_amount
        data_categories_final.append((category[0], porcentaje_category // 10))
    
    
    message = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        if i == 0:
            message += f'  {i}|\n' + ' '*4
        elif i == 100:
            message += f'{i}|\n'
        else:
            message += f' {i}|\n'

    text_list = message.split('\n')
    # print(text_list)
    
    string_amount = int(len(string_amount))
    for _ in range(string_amount):
        text_list.append(' ' * 4)
    

    for category in data_categories_final:
        for i in range(1, 12):
            if i == (11 - category[1]): break
            text_list[i] += ' ' * 3 
        for x in range(int(category[1]) + 1):
            index = 11 - x
            text_list[index] += ' o '
        text_list[12] += '---'
        
        
        for index, char in enumerate(category[0]):
            text_list[13 + index] += f' {char} '
            
        if len(category[0]) != string_amount:
            diferencia = string_amount - len(category[0]) 
            for i in range(1, diferencia + 1):
                text_list[-i] += ' '* 3

    for i in range(1, len(text_list)):
        if i == 12:
            text_list[12] += '-'
            continue
        text_list[i] += ' '


    message_final = '\n'.join(text_list)
    return message_final



food = Category('Food')
clothing = Category('Clothing')
auto = Category("Auto")

food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.transfer(200, clothing)
food.transfer(50, auto)
clothing.withdraw(130, 'loquesea')
auto.withdraw(30,'loquesea2')
print(food)

grafico = create_spend_chart([food,clothing, auto])
print(grafico)
