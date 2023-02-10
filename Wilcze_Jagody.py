import pygame

from Roslina import Roslina


class Wilcze_Jagody(Roslina):
    def __init__(self, swiat, x, y):
        super(Wilcze_Jagody, self).__init__(swiat, x, y)
        self._sila = 99
        self._gatunek = "Wilcze Jagody"
        self.filename = "wilcze_jagody.png"

    def daj_sie_zjesc(self, organizm):
        self.zniszcz_organizm()
        organizm.zniszcz_organizm()
