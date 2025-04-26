from pathlib import Path

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    
    def __str__(self):
        message = ''
        distance = (30 - len(self.name[0:30])) // 2
        message += ('*'*distance) + f'{self.name}' + ('*'*distance) + '\n'
        for registro in self.ledger:
            num_str = f'{registro['amount']:.2f}'
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
    data_categories.sort(key=lambda el:el[1],reverse=True)
    data_categories_final = []
    for category in data_categories:
        porcentaje_category = (100 * category[1]) / porcentaje_total
        data_categories_final.append((category[0], porcentaje_category // 10))
    
    # print(data_categories_final)
    message = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        if i == 0:
            message += f'  {i}|\n' + ' '*4
        elif i == 100:
            message += f'{i}|\n'
        else:
            message += f' {i}|\n'

    text_list = message.split('\n')
    print(text_list)
    z = 0
    string_amount = ''
    for category in data_categories_final:
        for i in range(1, 12):
            if i == (11 - category[1]): break
            text_list[i] += '   '
        for x in range(int(category[1]) + 1):
            index = 11 - x
            text_list[index] += ' o '
        text_list[12] += '---'
        string_amount = category[0] if len(category[0]) > len(string_amount) else string_amount
        for index, char in enumerate(category[0]):
            try:
                text_list[13 + index] += f' {char} '
            except IndexError:
                text_list.append((' ' * (4 + z)) + f' {char} ')
            # text_list[13 + i] += ''
        z += 3
    text_list[12] += '-'
    message_final = '\n'.join(text_list)
    return message_final

    

# [food., clothing]

# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o  o     
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g     

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
food.transfer(200, clothing)
clothing.withdraw(130, 'loquesea')
auto = Category("Auto")
food.transfer(50, auto)
auto.withdraw(30,'loquesea2')
print(food)
grafico = create_spend_chart([food,clothing, auto])
print(grafico)
path = Path('03-budget-app/grafico.txt')
path.write_text(grafico)


# lista_text = ['titulo','100|\n','90|\n','80|\n','70|\n','60|\n']
# lista_text[5] += ' o '
# print(lista_text)

# lista = ['Percentage spent by category', '100|']
# try:
#     lista[3] += 'Hola2'
# except IndexError:
#     lista.insert(3, 'hola')

# print(lista)