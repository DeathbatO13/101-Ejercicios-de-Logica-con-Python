## DeathbatO

def es_Armstrong(num):
    org = num
    sum = 0
    len_num = len(str(num))

    while num != 0:
        mod = num % 10
        sum += mod**len_num
        num //= 10

    return org == sum

for i in range(5):
    num =  int(input("Por favor ingrese un numero:..."))
    if num > 0:
        if es_Armstrong(num):
            print(f"El numero {num} es Armstrong.")
        else:
            print(f"El numero {num} NO es Armstrong...")
    else:
        print("El numero debe ser mayor a 0")