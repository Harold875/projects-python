# Instrucciones

Proyecto para construir una calculadora de área de polígono

En este proyecto, utilizarás programación orientada a objetos para crear las clases Rectángulo (`Rectangle`) y Cuadrado (`Square`). La clase Cuadrado debe ser una subclase de Rectángulo y heredar sus métodos y atributos.

## Clase Rectangle

Al crear un objeto `Rectangle`, debe inicializarse con los atributos de ancho (`width`) y alto (`height`). La clase también debe contener los siguientes métodos:

- `set_width`

- `set_height`

- `get_area`: Retorna area (`width * height`)

- `get_perimeter`: Retorna el perímetro (`2 * width + 2 * height`)

- `get_diagonal`: Retorna diagonal (`(width ** 2 + height ** 2) ** .5`)

- `get_picture`: Devuelve una cadena que representa la forma usando líneas de `'*'`. El número de líneas debe ser igual a la altura y el número de `'*'` en cada línea debe ser igual al ancho. Debería haber una nueva línea (`\n`) al final de cada línea. Si el ancho o la altura son mayores de 50, esto debe devolver la cadena: 'Demasiado grande para la imagen'(`'Too big for picture.'`).

- `get_amount_inside`: Toma otra forma (cuadrado o rectángulo) como un argumento. Devuelve el número de veces que la figura pasada podría caber dentro de la figura (sin rotaciones). Por ejemplo, un rectángulo con un ancho de 4 y un alto de 8 podría caber en dos cuadrados con lados de 4.

Además, si una instancia de un `Rectangle` se representa como una cadena, debería verse así: `'Rectangle(width=5, height=10)'`.

## Clase Square

La clase `Square` debe ser una subclase de `Rectangle`. Al crear un objeto `Square`, se pasa la longitud de un solo lado. El método `__init__` debe almacenar la longitud del lado en los atributos `width` y `height` de la clase `Rectangle`.

La clase `Square` debe poder acceder a los métodos de la clase `Rectangle`, pero también debe contener el método `set_side`. Si una instancia de un `Square` se representa como una cadena, debería verse así: `'Square(side=9)'`.

Además, los métodos `set_width` y `set_height` de la clase `Square` deben establecer tanto el ancho como el alto.

## Ejemplo de uso

```py
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

Ese código debería devolver:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```