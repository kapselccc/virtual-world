from Organizm import Organizm
from random import randint
from enum import Enum
from abc import ABC, abstractmethod


class Zwierze(Organizm, ABC):
    class WynikWalki(Enum):
        WYGRAL, PRZEGRAL, NIE_ODBYLO_SIE = 1, 2, 3

    class RodzajAtaku(Enum):
        ATAKUJACY, ATAKOWANY = 1, 2

    @abstractmethod
    def __init__(self, swiat, x, y):
        super(Zwierze, self).__init__(swiat, x, y)
        self.czas_zycia = 0

    def zmien_wiek(self):
        self.czas_zycia += 1

    def get_czas_zycia(self):
        return self.czas_zycia

    def akcja(self):
        return self.wykonaj_ruch()

    def wykonaj_ruch(self):
        j = randint(0, 3)
        kierunek = self.kierunki[j]
        for i in range(0, 4):
            if self.czy_kolizja(kierunek):
                self.kolizja(kierunek)
                return True
            elif not self.czy_wyjdzie_poza_mape(kierunek):
                self.wywolaj_zmiane_pola_kierunku(kierunek)
                return True
            else:
                kierunek = self.kierunki[(j + i + 1) % 4]

    def wywolaj_zmiane_pola_kierunku(self, kierunek):
        if kierunek == self.kierunek.LEFT:
            self.zmien_pole_na(self._x - 1, self._y)
        elif kierunek == self.kierunek.RIGHT:
            self.zmien_pole_na(self._x + 1, self._y)
        elif kierunek == self.kierunek.UP:
            self.zmien_pole_na(self._x, self._y - 1)
        elif kierunek == self.kierunek.DOWN:
            self.zmien_pole_na(self._x, self._y + 1)

    def kolizja(self, kierunek):
        if kierunek == self.kierunek.UP:
            atakowany = self._swiat.zwroc_organizm_pola(self._x, self._y - 1)
        elif kierunek == self.kierunek.DOWN:
            atakowany = self._swiat.zwroc_organizm_pola(self._x, self._y + 1)
        elif kierunek == self.kierunek.LEFT:
            atakowany = self._swiat.zwroc_organizm_pola(self._x - 1, self._y)
        elif kierunek == self.kierunek.RIGHT:
            atakowany = self._swiat.zwroc_organizm_pola(self._x + 1, self._y)
        else:
            atakowany = None
        if self.czy_ten_sam_gatunek(atakowany):
            self.rozmnoz()
            self.set_czy_rozmnozyl(True)
            atakowany.set_czy_rozmnozyl(True)
        else:
            self.wykonaj_walke(atakowany)

    def czy_walka(self, rodzaj, zwierze):
        return True

    def czy_wygral(self, atakowany):
        if self.czy_walka(self.RodzajAtaku.ATAKUJACY, atakowany) and atakowany.czy_walka(self.RodzajAtaku.ATAKOWANY,
                                                                                         self):
            if self.get_sila() < atakowany.get_sila():
                return self.WynikWalki.PRZEGRAL
            elif self.get_sila() > atakowany.get_sila() or (
                    self.get_sila() == atakowany.get_sila() and self.get_czas_zycia() >= atakowany.get_czas_zycia()):
                return self.WynikWalki.WYGRAL
            else:
                return self.WynikWalki.PRZEGRAL
        else:
            return self.WynikWalki.NIE_ODBYLO_SIE

    def czy_zjedzony(self):
        return False

    def rozmnoz(self):
        if not self.get_czy_rozmnozyl():
            i = 0
            r = self.kierunki[i]
            while self.czy_kolizja(r) or self.czy_wyjdzie_poza_mape(r):
                if i == 3:
                    return
                i += 1
                r = self.kierunki[i]
            self._swiat.dodaj_komunikat("Rozmnożono " + self.get_gatunek())
            t_x, t_y = self._x, self._y
            if r == self.kierunek.UP:
                t_y -= 1
            elif r == self.kierunek.DOWN:
                t_y += 1
            elif r == self.kierunek.LEFT:
                t_x -= 1
            elif r == self.kierunek.RIGHT:
                t_x += 1
            self._swiat.stworz_organizm(self.get_gatunek(), t_x, t_y)

    def wykonaj_walke(self, atakowany):
        if atakowany.czy_zjedzony():
            self._swiat.dodaj_komunikat(atakowany.get_gatunek() + " został zjedzony przez " + self.get_gatunek())
            atakowany.daj_sie_zjesc(self)
        else:
            wynik = self.czy_wygral(atakowany)
            if wynik == self.WynikWalki.WYGRAL:
                x, y = atakowany.get_x(), atakowany.get_y()
                self._swiat.dodaj_komunikat(self.get_gatunek() + " pokonał w walce " + atakowany.get_gatunek())
                atakowany.zniszcz_organizm()
                self.zmien_pole_na(x, y)
            elif wynik == self.WynikWalki.PRZEGRAL:
                self._swiat.dodaj_komunikat(atakowany.get_gatunek() + " pokonał w walce " + self.get_gatunek())
                self.zniszcz_organizm()
            elif wynik == self.WynikWalki.NIE_ODBYLO_SIE:
                return

    def aktualizuj_zmienne(self):
        if self._czy_rozmnozyl:
            self._cooldown_rozmnozenia -= 1
            if self._cooldown_rozmnozenia == 0:
                self.set_czy_rozmnozyl(False)
        self.zmien_wiek()

    def get_stan(self):
        stan = super(Zwierze, self).get_stan()
        stan = stan[:-1]
        return stan + " " + str(self.czas_zycia) + "\n"

    def ustaw_stan(self, text):
        super(Zwierze, self).ustaw_stan(text)
        self.czas_zycia = int(text[6])
