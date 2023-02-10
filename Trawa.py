import pygame

from Roslina import Roslina



class Trawa(Roslina):
    def __init__(self, swiat, x, y):
        super(Trawa, self).__init__(swiat, x, y)
        self._sila = 0
        self._gatunek = "Trawa"
        self.filename = "trawa.jpg"
