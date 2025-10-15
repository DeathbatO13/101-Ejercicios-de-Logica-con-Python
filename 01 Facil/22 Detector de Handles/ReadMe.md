# 🧮 Ejercicio 22 — Detector de Handles



## 📌 Descripción

Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares. 

Debes crear una expresión regular para cada caso:
- Handle usuario: Los que comienzan por "@"
- Handle hashtag: Los que comienzan por "#"
- Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)


## 💡 Ejemplo

    
    $ python DetectorHandles.py

    Texto de ejemplo:
    Sígueme en @Daniel y usa #Python. Visita https://github.com/DeathbatO13 o www.ejemplo.es para más info.

    Resultados del detector de handles:
    {'usuarios': ['@Daniel'], 'hashtags': ['#Python'], 'webs': ['https://github.com', 'www.ejemplo.es']}  
    