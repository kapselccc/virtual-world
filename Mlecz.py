import pygame
from random import randint

from Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, swiat, x, y):
        super(Mlecz, self).__init__(swiat, x, y)
        self._sila = 0
        self._gatunek = "Mlecz"
        self.filename = "mlecz.png"

    def akcja(self):
        czy_zasiano = False
        for i in range(0, 4):
            r = randint(0, 99)
            if r < self.szansa_na_zasianie:
                self.zasiej()
                czy_zasiano = True
        if czy_zasiano:
            self.set_czy_rozmnozyl(True)
        return True
