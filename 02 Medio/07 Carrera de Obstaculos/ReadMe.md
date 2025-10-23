# 🧮 Ejercicio 07 — La Carrera de Obstaculos

## 📌 Descripción

  Crea una función que evalúe si un/a atleta ha superado correctamente una
  carrera de obstáculos.
  - La función recibirá dos parámetros:
       - Un array que sólo puede contener String con las palabras
         "run" o "jump"
       - Un String que represente la pista y sólo puede contener "_" (suelo)
         o "|" (valla)
  - La función imprimirá cómo ha finalizado la carrera:
       - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
         será correcto y no variará el símbolo de esa parte de la pista.
       - Si hace "jump" en "_" (suelo), se variará la pista por "x".
       - Si hace "run" en "|" (valla), se variará la pista por "/".
  - La función retornará un Boolean que indique si ha superado la carrera.
  Para ello tiene que realizar la opción correcta en cada tramo de la pista.



## 💡 Ejemplo

    
    $ python Obstaculos.py

    Primera pista y recorrido: 
    ['_', '_', '|', '_', '_', '_', '|', '_']
    ['run', 'run', 'jump', 'run', 'run', 'run', 'jump', 'run']

    Completo la carrera correctamente:
    ['_', '_', '|', '_', '_', '_', '|', '_']


    Segunda pista y recorrido:
    ['_', '|', '_', '|', '_', '_', '|', '_']
    ['run', 'jump', 'run', 'jump', 'jump', 'run', 'run', 'jump']

    No completo la carrera correctamente:
    ['_', '|', '_', '|', 'x', '_', '/', 'x']
