import csv

class Pracownik:
    def __init__(self, imie, nazwisko, pensja_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja_brutto = pensja_brutto

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}"

    def oblicz_netto(self):
        skladka_emerytalna = self.pensja_brutto * 0.0976
        skladka_rentowa = self.pensja_brutto * 0.065
        skladka_chorobowa = self.pensja_brutto * 0.0245
        skladka_zdrowotna = self.pensja_brutto * 0.09
        podstawa_opodatkowania = self.pensja_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa
        podatek = podstawa_opodatkowania * 0.12
        netto = self.pensja_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa - podatek
        return round(netto, 2)




import unittest
class TestPracownik(unittest.TestCase):
     def test_oblicz_koszty_pracodawcy(self):
         pracownik = Pracownik("Jan", "Kowalski", 5000)
         expected_result = 6791.30
         assert pracownik.oblicz_koszty_pracodawcy() == expected_result

     if __name__ == "__main__":
        unittest.main()



with open("/Users/ania/Desktop/studia magisterskie/io/pracownicy.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        imie = row[0]
        nazwisko = row[1]
        pensja = float(row[2])

        pracownik = Pracownik(imie, nazwisko, pensja)

        print(pracownik)
        netto = pracownik.oblicz_netto()
        print(f"Netto dla {imie} {nazwisko}: {netto}")
        koszty = pracownik.oblicz_koszty_pracodawcy()
        print(f"Koszt pracodawcy dla {imie} {nazwisko}: {koszty}")
        pracownik.wygeneruj_raport()
        print()