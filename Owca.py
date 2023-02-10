import pygame

from Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, swiat, x, y):
        super(Owca, self).__init__(swiat, x, y)
        self._sila = 4
        self._inicjatywa = 4
        self._gatunek = "Owca"
        self.filename = "owca.png"
