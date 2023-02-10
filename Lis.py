import pygame

from Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, swiat, x, y):
        super(Lis, self).__init__(swiat, x, y)
        self._sila = 3
        self._inicjatywa = 7
        self._gatunek = "Lis"
        self.filename = "lis.png"

    def czy_walka(self, rodzaj, zwierze):
        if rodzaj == self.RodzajAtaku.ATAKUJACY and zwierze.get_sila() > self._sila:
            self.wykonaj_ruch()
            return False
        else:
            return True