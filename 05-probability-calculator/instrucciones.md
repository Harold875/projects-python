# Instrucciones

Proyecto para crear una calculadora de probabilidades

Supongamos que hay un sombrero con 5 bolas azules, 4 bolas rojas y 2 bolas verdes. ¿Cuál es la probabilidad de que al extraer 4 bolas al azar, haya al menos una bola roja y 2 bolas verdes? Si bien es posible calcular la probabilidad mediante matemáticas avanzadas, una forma más sencilla es escribir un programa que realice una gran cantidad de experimentos para estimar una probabilidad aproximada.

Para este proyecto, escribirás un programa para determinar la probabilidad aproximada de extraer ciertas bolas al azar de un sombrero.

Primero, crea una clase `Hat` en `main.py`. La clase debe tomar un número variable de argumentos que especifiquen la cantidad de bolas de cada color que hay en el sombrero. Por ejemplo, un objeto de clase podría crearse de cualquiera de estas maneras:

```py
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

Un sombrero (`hat`) siempre se creará con al menos una bola. Los argumentos pasados ​​al objeto sombrero al crearlo deben convertirse en una variable de instancia de contenido (`contents`). El contenido (`contents`) debe ser una lista de cadenas que contenga un elemento por cada bola del sombrero. Cada elemento de la lista debe ser el nombre de un color que represente una bola de ese color. Por ejemplo, si el sombrero es `{'red': 2, 'blue': 1}`, el contenido (`contents`) debe ser `['red', 'red', 'blue']`.

La clase Sombrero (`Hat`) debe tener un método de extracción (`draw`) que acepte un argumento que indique el número de bolas que se extraerán del sombrero. Este método debe extraer bolas aleatoriamente del contenido (`contents`) y devolverlas como una lista de cadenas. Las bolas no deben volver al sombrero durante la extracción, de forma similar a un experimento de urna sin reemplazo. Si el número de bolas a extraer excede la cantidad disponible, se devuelven todas las bolas.

A continuación, crea una función de experimento (`experiment`) en `main.py` (fuera de la clase Sombrero (`Hat`)). Esta función debe aceptar los siguientes argumentos:

- `hat`: Un objeto de sombrero que contiene pelotas que deben copiarse dentro de la función.

- `expected_balls`: Un objeto que indica el grupo exacto de bolas para intentar sacar del sombrero para el experimento. Por ejemplo, para determinar la probabilidad de sacar 2 bolas azules y 1 bola roja del sombrero, configure `expected_balls` en `{'blue':2, 'red':1}`.

- `num_balls_drawn`: El número de bolas a dibujar del sombrero en cada experimento.

- `num_experiments`: El número de experimentos a realizar. (Cuantos más experimentos se realicen, más precisa será la probabilidad aproximada)

La función de experimento (`experiment`) debe devolver una probabilidad.

Por ejemplo, si quieres determinar la probabilidad de obtener al menos dos bolas rojas y una verde al extraer cinco bolas de un sombrero con seis negras, cuatro rojas y tres verdes, realizarás `N` experimentos, contarás cuántas veces `M` obtienes al menos dos bolas rojas y una verde y estimarás la probabilidad como `M/N`. Cada experimento consiste en comenzar con un sombrero con las bolas especificadas, extraer varias bolas y comprobar si has obtenido las bolas que intentabas extraer.

Así es como llamarías a la función de experimento (`experiment`), basándote en el ejemplo anterior con 2000 experimentos:

```py
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

La salida sería algo como esto:

```py
0.356
```

Dado que esto se basa en tablas aleatorias, la probabilidad será ligeramente diferente cada vez que se ejecuta el código.

Sugerencia: Considera usar los módulos que ya se importaron en la parte de arriba (`copy`, `random`). No inicializar la semilla aleatoria dentro del archivo.