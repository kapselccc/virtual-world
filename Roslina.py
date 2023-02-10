from Organizm import Organizm
from random import randint
from abc import ABC, abstractmethod


class Roslina(Organizm, ABC):
    @abstractmethod
    def __init__(self, swiat, x, y):
        super(Roslina, self).__init__(swiat, x, y)
        self.szansa_na_zasianie = 5
        self.set_czy_rozmnozyl(True)

    def daj_sie_zjesc(self, organizm):
        x, y = self.get_x(), self.get_y()
        self.zniszcz_organizm()
        organizm.zmien_pole_na(x, y)

    def czy_zjedzony(self):
        return True

    def zasiej(self):
        if not self._czy_rozmnozyl:
            j = randint(0, 3)
            r = self.kierunki[j]
            for i in range(0, 4):
                if not self.czy_kolizja(r) and not self.czy_wyjdzie_poza_mape(r):
                    self.posadz_rosline(r)
                    self._swiat.dodaj_komunikat(self.get_gatunek() + " zasiał/a nową roślinę")
                    break
                else:
                    r = self.kierunki[(j + i + 1) % 4]

    def posadz_rosline(self, kierunek):
        t_x, t_y = self._x, self._y
        if kierunek == self.kierunek.UP:
            t_y -= 1
        elif kierunek == self.kierunek.DOWN:
            t_y += 1
        elif kierunek == self.kierunek.LEFT:
            t_x -= 1
        elif kierunek == self.kierunek.RIGHT:
            t_x += 1
        else:
            print("Podano zły argument dla funkcji posadz_rosline()")
            return
        self._swiat.stworz_organizm(self.get_gatunek(), t_x, t_y)

    def akcja(self):
        los = randint(0, 99)
        if los < self.szansa_na_zasianie:
            self.zasiej()
            self.set_czy_rozmnozyl(True)
            return True
        else:
            return True
