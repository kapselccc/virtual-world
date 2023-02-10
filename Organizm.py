from enum import Enum
from abc import ABC, abstractmethod
import defines
import pygame


class Organizm(ABC):

    class kierunek(Enum):
        LEFT, RIGHT, UP, DOWN = 1, 2, 3, 4

    kierunki = (kierunek.LEFT, kierunek.RIGHT, kierunek.UP, kierunek.DOWN)

    def __init__(self, swiat, x, y):
        self._czy_rozmnozyl = False
        self._sila = 0
        self._inicjatywa = 0
        self._gatunek = "o"
        self._swiat = swiat
        self._x = x
        self._y = y
        self.filename = ""
        self.zdjecie = None
        self._cooldown_rozmnozenia = 0

    def get_gatunek(self):
        return self._gatunek

    def get_sila(self):
        return self._sila

    def get_inicjatywa(self):
        return self._inicjatywa

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_czy_rozmnozyl(self):
        return self._czy_rozmnozyl

    def set_czy_rozmnozyl(self, b):
        if b:
            self._cooldown_rozmnozenia = defines.COOLDOWN_DO_ROZMNOZENIA
        self._czy_rozmnozyl = b

    def zmien_pole_na(self, x, y):
        self._swiat.aktualizuj_mape(self, x, y)
        self._x = x
        self._y = y

    def czy_wyjdzie_poza_mape(self, kierunek):
        if kierunek == kierunek.LEFT:
            if self._x == 0:
                return True
            return False
        elif kierunek == kierunek.RIGHT:
            if self._x == self._swiat.width - 1:
                return True
            return False
        elif kierunek == kierunek.UP:
            if self._y == 0:
                return True
            return False
        elif kierunek == kierunek.DOWN:
            if self._y == self._swiat.height - 1:
                return True
            return False

    def czy_kolizja(self, kierunek):
        if kierunek == self.kierunek.LEFT:
            if self._swiat.czy_zajete(self._x - 1, self._y):
                return True
        elif kierunek == self.kierunek.RIGHT:
            if self._swiat.czy_zajete(self._x + 1, self._y):
                return True
        elif kierunek == self.kierunek.UP:
            if self._swiat.czy_zajete(self._x, self._y - 1):
                return True
        elif kierunek == self.kierunek.DOWN:
            if self._swiat.czy_zajete(self._x, self._y + 1):
                return True

        return False

    def akcja(self):
        return True

    def zniszcz_organizm(self):
        self._swiat.usun_organizm(self)

    def zwieksz_sile(self, n):
        self._sila += n

    def czy_ten_sam_gatunek(self, organizm):
        if self.get_gatunek() is organizm.get_gatunek():
            return True
        else:
            return False

    def zaladuj_zdjecie(self):
        self.zdjecie = pygame.image.load("grafika/" + self.filename)
        self.zdjecie = pygame.transform.scale(self.zdjecie, (defines.OBIEKT_WIDTH - 2, defines.OBIEKT_WIDTH - 2))

    def get_zdjecie(self):
        return self.zdjecie

    def aktualizuj_zmienne(self):
        if self._czy_rozmnozyl is True:
            self._cooldown_rozmnozenia -= 1
            if self._cooldown_rozmnozenia == 0:
                self.set_czy_rozmnozyl(False)

    @abstractmethod
    def czy_zjedzony(self):
        pass

    def get_stan(self):
        return self.get_gatunek() + " " + str(self._x) + " " + str(self._y) + " " + str(self._sila) + " " \
               + str(self._czy_rozmnozyl) + " " + str(self._cooldown_rozmnozenia) + "\n"

    def ustaw_stan(self, text):
        i = 0
        if not text[1].isdigit():
            i = 1
        self._sila = int(text[3 + i])
        self._czy_rozmnozyl = bool(text[4 + i])
        self._cooldown_rozmnozenia = int(text[5 + i])
