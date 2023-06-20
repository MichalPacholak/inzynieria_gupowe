import math

#objetosc szescianu
def objetosc_szescianu(a):
    return a**3
    

#pole powierzchni szescianu

def powierzchnia_szescianu(a):
    return 6*a**2

#test dla objętości kuli

spodziewany_wynik = 4/3 * math.pi * (promien_kuli ** 3)

assert oblicz_objetosc_kuli(promien_kuli) == spodziewany_wynik