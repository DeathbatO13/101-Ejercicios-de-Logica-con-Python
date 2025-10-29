# 🧮 Ejercicio 12 — Maquina Expendedora

## 📌 Descripción


  Simula el funcionamiento de una máquina expendedora creando una operación
 que reciba dinero (array de monedas) y un número que indique la selección
 del producto.
 - El programa retornará el nombre del producto y un array con el dinero
    de vuelta (con el menor número de monedas).
  - Si el dinero es insuficiente o el número de producto no existe,
    deberá indicarse con un mensaje y retornar todas las monedas.
  - Si no hay dinero de vuelta, el array se retornará vacío.
  - Para que resulte más simple, trabajaremos en céntimos con monedas
    de 5, 10, 50, 100 y 200.
  - Debemos controlar que las monedas enviadas estén dentro de las soportadas.



## 💡 Ejemplo

    
    $ python Maquina_Expendedora.py

    Ingrese las monedas separadas por comas (ejemplo: 100,50,10): 100, 50
    Seleccione el número del producto (1-3): 3
    {'producto': 'Café', 'monedas': [10, 10, 10]}

   
