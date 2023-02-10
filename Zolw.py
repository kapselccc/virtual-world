import pygame
from random import randint
from Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, swiat, x, y):
        super(Zolw, self).__init__(swiat, x, y)
        self._sila = 2
        self._inicjatywa = 1
        self._gatunek = "Zolw"
        self.szansa_na_ruch = 25
        self.filename = "zolw.png"

    def czy_walka(self, rodzaj, zwierze):
        if rodzaj == self.RodzajAtaku.ATAKOWANY:
            if zwierze.get_sila() < 5:
                self._swiat.dodaj_komunikat("Zolw odparł atak " + zwierze.get_gatunek())
                return False
            else:
                return True
        else:
            return True

    def akcja(self):
        if randint(0, 99) < self.szansa_na_ruch:
            return self.wykonaj_ruch()
        else:
            return True
