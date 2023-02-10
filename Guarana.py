import pygame

from Roslina import Roslina


class Guarana(Roslina):
    def __init__(self, swiat, x, y):
        super(Guarana, self).__init__(swiat, x, y)
        self._sila = 0
        self._gatunek = "Guarana"
        self.filename = "guarana.jpg"

    def daj_sie_zjesc(self, organizm):
        x, y = self._x, self._y
        self.zniszcz_organizm()
        organizm.zwieksz_sile(3)
        organizm.zmien_pole_na(x, y)
