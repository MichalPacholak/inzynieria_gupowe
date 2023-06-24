####################
## objetosc kuli  ##
####################

import math

def oblicz_objetosc_stozka(promien, wysokosc):
    objetosc = (1/3) * math.pi * promien**2 * wysokosc
    return objetosc




# Test sprawdzający wynik dla objętości ostrosłupa
a = 4
h = 6
spodziewana_objetosc_ostroslupa = (1/3) * a**2 * h
assert oblicz_objetosc_ostroslupa(a, h) == spodziewana_objetosc_ostroslupa

# Test sprawdzający wynik dla pola powierzchni ostrosłupa
a = 4
h = 6
spodziewane_pole_ostroslupa = a**2 + (a * math.sqrt((a**2)/4 + h**2)) + (a * math.sqrt((a**2)/4 + h**2))
assert oblicz_pole_ostroslupa(a, h) == spodziewane_pole_ostroslupa

# Test dla objętości kuli
promien_kuli = 5
spodziewany_wynik = (4/3) * math.pi * (promien_kuli ** 3)
assert oblicz_objetosc_kuli(promien_kuli) == spodziewany_wynik
