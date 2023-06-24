
## objetosc kuli  


import math

def oblicz_objetosc_kuli(promien):
    if promien <= 0:
        return "Promień musi być większy od zera."
    else:
        objetosc = (4/3) * math.pi * (promien ** 3)
        return objetosc


#objetosc szescianu
def objetosc_szescianu(a):
    return a**3
    

#pole powierzchni szescianu

def powierzchnia_szescianu(a):
    return 6*a**2


#Test sprawdzający wynik dla objętości sześcianu
a = 4
spodziewana_objetosc_szescianu = a_szescianu ** 3
assert objetosc_szescianu(a_szescianu) == spodziewana_objetosc_szescianu


# Test sprawdzający wynik dla pola powierzchni sześcianu
a = 5
spodziewane_pole_szescianu = 6 * a_szescianu_2 ** 2
assert powierzchnia_szescianu(a_szescianu_2) == spodziewane_pole_szescianu

#test dla objętości kuli

spodziewany_wynik = 4/3 * math.pi * (promien_kuli ** 3)

assert oblicz_objetosc_kuli(promien_kuli) == spodziewany_wynik