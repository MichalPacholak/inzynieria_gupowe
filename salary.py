def oblicz_koszty_pracodawcy(self):
        skladka_emerytalna = self.pensja_brutto * 0.0976
        skladka_rentowa = self.pensja_brutto * 0.065
        skladka_wypadkowa = self.pensja_brutto * 0.0167
        skladka_fundusz_pracy = self.pensja_brutto * 0.0245
        skladka_fgsp = self.pensja_brutto * 0.01
        koszty_pracodawcy = self.pensja_brutto + skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_fundusz_pracy + skladka_fgsp
        return round(koszty_pracodawcy, 2)

    def wygeneruj_raport(self):
        koszty_pracodawcy = self.oblicz_koszty_pracodawcy()
        skladka_emerytalna = self.pensja_brutto * 0.0976
        skladka_rentowa = self.pensja_brutto * 0.065
        skladka_wypadkowa = self.pensja_brutto * 0.0167
        skladka_fgsp = self.pensja_brutto * 0.01
        print("Raport kosztów/przychodów:")
        print(f"-------------------------------------------")
        print(f"Składka emerytalna: {skladka_emerytalna:.2f}")
        print(f"Składka rentowa: {skladka_rentowa:.2f}")
        print(f"Składka wypadkowa: {skladka_wypadkowa:.2f}")
        print(f"Składka FGŚ: {skladka_fgsp:.2f}")



import unittest
class TestPracownik(unittest.TestCase):
    def test_str(self):
        pracownik = Pracownik("Jan", "Kowalski", 5000)
        expected_result = "Pracownik: Jan Kowalski"
        assert str(pracownik) == expected_result

    def test_oblicz_netto(self):
        pracownik = Pracownik("Jan", "Kowalski", 5000)
        expected_result = 3754.68
        assert pracownik.oblicz_netto() == expected_result