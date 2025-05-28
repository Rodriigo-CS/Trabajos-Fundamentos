def hanoi (n, inicial = '1', auxiliar = '2', final= '3'):
    if n > 0:
        hanoi(n-1, inicial, final, auxiliar)
        print('El disco', n,'se movera de la torre', inicial, 'a la torre', final)
        hanoi(n-1, auxiliar, inicial, final)
discos = int(input("ingresa el numero de discos que desees: "))
hanoi(discos)
print("los movimientos minimos que se realizan son: ", pow(2, discos)-1)