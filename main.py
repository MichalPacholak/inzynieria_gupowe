#zadanieA
import math

#objetosc szescianu
def objetosc_szescianu(a):
    return a**3
    

#pole powierzchni szescianu

def powierzchnia_szescianu(a):
    return 6*a**2

#test dla objętości stozka

spodziewany_wynik = 1/3 * math.pi * h_stozka * (promien_stozka ** 2)

assert oblicz_objetosc_stozka(promien_kuli, h_stozka) == spodziewany_wynik

#objetosc ostroslupa
a = 4

h = 6

objetosc_ostroslupa = (1/3) * a**2 * h




# pole powierzchni ostrosłupa

a = 4

h = 6

pole_powierzchni_ostroslupa = a**2 + (a * math.sqrt((a**2)/4 + h**2)) + (a * math.sqrt((a**2)/4 + h**2))

