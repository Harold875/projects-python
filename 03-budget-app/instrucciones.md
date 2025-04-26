# Instrucciones:

Proyecto de creación de una aplicación de presupuesto

Completa la clase `Category`. Debe ser capaz de instanciar objetos basados ​​en diferentes categorías de presupuesto, como comida, ropa y entretenimiento. Cuando se crean objetos, se pasan en el nombre de la categoría. La clase debe tener una variable de instancia llamada `ledger` que sea una lista. 

La clase también debe contener los siguientes métodos:

- Un método de `deposit` que acepte una cantidad y una descripción. Si no se proporciona una descripción, debe ser una cadena vacía por defecto. El método debe añadir un objeto a la lista del libro mayor en forma de `{'amount': amount, 'description': description}`.

- Un método de `withdraw` similar al método de depósito, pero la cantidad pasada debe almacenarse en el libro mayor como un número negativo. Si no hay suficientes fondos, no se debe añadir nada al libro mayor. Este método debe devolver `True` si se realizó el retiro y `False` en caso contrario.

- Un método `get_balance` que devuelve el saldo actual de la categoría de presupuesto en función de los depósitos y retiros que se han producido.

- Un método de `transfer` que acepta un importe y otra categoría de presupuesto como argumentos. El método debe añadir un retiro con el importe y la descripción 'Transferir a [Categoría de presupuesto de destino]'. A continuación, el método debe añadir un depósito a la otra categoría de presupuesto con el importe y la descripción 'Transferir desde [Categoría de presupuesto de origen]'. Si no hay fondos suficientes, no se debe añadir nada a ninguno de los libros contables. Este método debe devolver `True` si se realizó la transferencia y `False` en caso contrario.

- Un método `check_funds` que acepta un importe como argumento. Devuelve `False` si el importe es mayor que el saldo de la categoría de presupuesto y devuelve `True` en caso contrario. Este método debe ser utilizado tanto por el método de `withdraw` como por el método de `transfer`.

Cuando se imprime el objeto de presupuesto, debe mostrar:

- Una línea de título de 30 caracteres donde el nombre de la categoría está centrado en una línea de `*` caracteres.

- Una lista de los elementos en el contador. Cada línea debe mostrar la descripción y la cantidad. Los primeros 23 caracteres de la descripción deben mostrarse, luego la cantidad. La cantidad debe estar alineada correctamente, contener dos decimales y mostrar un máximo de 7 caracteres.

- Una línea que muestra el total de las categorías.

Aquí hay un ejemplo de uso:
```py
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

Y aquí hay un ejemplo del resultado:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Además de la clase `Category`, crear una función (fuera de la clase) llamada `create_spend_chart` que toma una lista de categorías como argumento. Debe devolver una cadena que es un gráfico de barras.

El gráfico debe mostrar el porcentaje gastado en cada categoría pasado a la función. El porcentaje de gasto debe calcularse solo con retiros, no con depósitos, y debe ser el porcentaje del monto gastado en cada categoría respecto al total gastado en todas las categorías. En la parte inferior izquierda del gráfico debe estar la etiqueta 0-100. Las barras del gráfico deben estar formadas por el carácter "o".  La altura de cada barra debe ser redondeada hacia abajo al 10 más cercano. La línea horizontal debajo de las barras debe ir dos espacios más allá de la barra final. Cada nombre de categoría debe ser escrito verticalmente debajo de la barra. Debería haber un título en la parte superior que diga 'Porcentaje gastado por categoría'.

Esta función se probará con hasta cuatro categorías.

Mire el output del ejemplo a continuación muy de cerca y asegúrese de que el espaciado coincida exactamente con el ejemplo.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A    
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g 
```