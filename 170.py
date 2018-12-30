#Fails 170.py
#Autors: Artūrs Asars-Asarovskis
#Apliecības nummurs: 181REB263
# Dtums: 2018.12.3
# Sagatave funkcijas saknes meklēšanai ar dihatomijas metodi 

# -*- coding: utf-8 -*-

from math import exp, fabs
from time import sleep

def f(x):
    return (1-x)*exp(-x)

# Definejam argumenta x robežas 
a = 1.1
b = 3.2 
#Aprēķinam funkcijas vērtības dotajos punktos
funa = f(a)
funb = f(b)
 
#Pārbaudam, vai dotajā intervālā ir saknes :
if ( funa * funb > 0.0):
    print ("Dotajā intervālā [%s, %s] sakņu nav"%(a,b))
    sleep(1); exit()  #ziņo uz ekrāna, gaida 1 sec. un darbu beidz
else: 
    print ("Dotajā intervālā sakne(s) ir!")

#Definējam precizitāti, ar kādu meklēsim sakni :
deltax = 0.01

#Sašaurinam saknes meklēšanas robežas:
while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0. ):
       b = x
    else:
        a = x
print ("Sakne ir: ", x)

