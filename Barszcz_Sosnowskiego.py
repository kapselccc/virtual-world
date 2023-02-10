from random import randint
from Zwierze import Zwierze

import pygame

import defines
from Roslina import Roslina


class Barszcz_Sosnowskiego(Roslina):
    def __init__(self, swiat, x, y):
        super(Barszcz_Sosnowskiego, self).__init__(swiat, x, y)
        self._sila = 10
        self._gatunek = "Barszcz Sosnowskiego"
        self.filename = "barszcz_sosnowskiego.png"

    def daj_sie_zjesc(self, organizm):
        x, y = self.get_x(), self.get_y()
        self.zniszcz_organizm()
        if organizm.get_gatunek() != "Cyber-owca":
            organizm.zniszcz_organizm()
        else:
            organizm.zmien_pole_na(x, y)

    def akcja(self):
        self.zabij_do_okola()
        los = randint(0, 99)
        if los < self.szansa_na_zasianie:
            self.zasiej()
            self.set_czy_rozmnozyl(True)
        return True

    def zabij_do_okola(self):
        for i in range(0, 4):
            x, y = self._x, self._y
            if i == 0 and x < defines.WIDTH - 1:
                x += 1
            elif i == 1 and x > 0:
                x -= 1
            elif i == 2 and y < defines.HEIGHT - 1:
                y += 1
            elif i == 3 and y > 0:
                y -= 1
            else:
                continue
            organizm = self._swiat.zwroc_organizm_pola(x, y)
            if organizm is not None and isinstance(organizm, Zwierze) and organizm.get_gatunek() != "Cyber-owca":
                self._swiat.dodaj_komunikat(organizm.get_gatunek() + " zbliżył się do Barszczu Sosnowskiego")
                organizm.zniszcz_organizm()
