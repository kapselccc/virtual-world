import pygame

from Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, swiat, x, y):
        super(Wilk, self).__init__(swiat, x, y)
        self._sila = 9
        self._inicjatywa = 5
        self._gatunek = "Wilk"
        self.filename = "wilk.png"
