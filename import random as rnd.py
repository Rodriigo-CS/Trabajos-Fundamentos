import random as rnd
import os

ruletarusa = int(input("ingrese un numero entre 1 y 6: "))
Num = rnd.randint(1,6)

print (ruletarusa)
print (Num)

if ruletarusa == Num:
    print("Muerto")
else:
    print("Mi papa")