import pygame
from random import randint

from Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, swiat, x, y):
        super(Antylopa, self).__init__(swiat, x, y)
        self.szansa_na_ucieczke = 50
        self._sila = 4
        self._inicjatywa = 4
        self._gatunek = "Antylopa"
        self.filename = "antylopa.png"

    def wywolaj_zmiane_pola_kierunku(self, kierunek):
        if kierunek == self.kierunek.LEFT:
            self.zmien_pole_na(self._x - 2, self._y)
        elif kierunek == self.kierunek.RIGHT:
            self.zmien_pole_na(self._x + 2, self._y)
        elif kierunek == self.kierunek.UP:
            self.zmien_pole_na(self._x, self._y - 2)
        elif kierunek == self.kierunek.DOWN:
            self.zmien_pole_na(self._x, self._y + 2)

    def czy_wyjdzie_poza_mape(self, kierunek):
        if kierunek == kierunek.LEFT:
            if self._x <= 1:
                return True
            return False
        elif kierunek == kierunek.RIGHT:
            if self._x >= self._swiat.width - 2:
                return True
            return False
        elif kierunek == kierunek.UP:
            if self._y <= 1:
                return True
            return False
        elif kierunek == kierunek.DOWN:
            if self._y >= self._swiat.height - 2:
                return True
            return False

    def czy_walka(self, rodzaj, zwierze):
        if rodzaj == self.RodzajAtaku.ATAKOWANY:
            if randint(0, 99) < self.szansa_na_ucieczke:
                self._swiat.dodaj_komunikat("Antylopa uniknęła walki")
                return False
            else:
                return True

    def przenies_na_losowe_miejsce(self):
        j = randint(0, 3)
        r = None
        for i in range(0, 4):
            r = self.kierunki[(j + i) % 4]
            if self.czy_kolizja(r) or self.czy_wyjdzie_poza_mape(r):
                continue
            elif i == 3:
                return
            else:
                break
        x, y = self._x, self._y
        if r == self.kierunek.UP:
            y -= 1
        elif r == self.kierunek.DOWN:
            y += 1
        elif r == self.kierunek.LEFT:
            x -= 1
        elif r == self.kierunek.RIGHT:
            x += 1
        self.zmien_pole_na(x, y)

    def kolizja(self, kierunek):
        if kierunek == self.kierunek.UP:
            atakowany = self._swiat.zwroc_organizm_pola(self._x, self._y - 2)
        elif kierunek == self.kierunek.DOWN:
            atakowany = self._swiat.zwroc_organizm_pola(self._x, self._y + 2)
        elif kierunek == self.kierunek.LEFT:
            atakowany = self._swiat.zwroc_organizm_pola(self._x - 2, self._y)
        elif kierunek == self.kierunek.RIGHT:
            atakowany = self._swiat.zwroc_organizm_pola(self._x + 2, self._y)
        else:
            atakowany = None
        if self.czy_ten_sam_gatunek(atakowany):
            self.rozmnoz()
            self.set_czy_rozmnozyl(True)
            atakowany.set_czy_rozmnozyl(True)
        else:
            self.wykonaj_walke(atakowany)

    def czy_kolizja(self, kierunek):
        if kierunek == self.kierunek.LEFT:
            if self._swiat.czy_zajete(self._x - 2, self._y):
                return True
        elif kierunek == self.kierunek.RIGHT:
            if self._swiat.czy_zajete(self._x + 2, self._y):
                return True
        elif kierunek == self.kierunek.UP:
            if self._swiat.czy_zajete(self._x, self._y - 2):
                return True
        elif kierunek == self.kierunek.DOWN:
            if self._swiat.czy_zajete(self._x, self._y + 2):
                return True

        return False
