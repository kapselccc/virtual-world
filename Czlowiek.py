import pygame
import sys
from random import randint

from Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, swiat, x, y):
        super(Czlowiek, self).__init__(swiat, x, y)
        self._sila = 4
        self._inicjatywa = 5
        self._gatunek = "Czlowiek"
        self.cooldown = 0
        self.wlaczona_umiejetnosc = False
        self.aktywny = 0
        self.filename = "czlowiek.jpg"

    def wykonaj_ruch(self):
        quit_loop = False
        while not quit_loop:
            events = pygame.event.get()
            punkt = pygame.mouse.get_pos()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if self.cooldown == 0:
                            self.wlacz_umiejetnosc()
                            self.wykonaj_ruch()
                        else:
                            self.wykonaj_ruch()
                        return True
                    elif event.key == pygame.K_UP:
                        if self.czy_kolizja(self.kierunek.UP):
                            self.kolizja(self.kierunek.UP)
                            return True
                        elif not self.czy_wyjdzie_poza_mape(self.kierunek.UP):
                            self.zmien_pole_na(self._x, self._y - 1)
                            quit_loop = True
                            return True
                        break
                    elif event.key == pygame.K_DOWN:
                        if self.czy_kolizja(self.kierunek.DOWN):
                            self.kolizja(self.kierunek.DOWN)
                            return True
                        elif not self.czy_wyjdzie_poza_mape(self.kierunek.DOWN):
                            self.zmien_pole_na(self._x, self._y + 1)
                            quit_loop = True
                            return True
                        break
                    elif event.key == pygame.K_LEFT:
                        if self.czy_kolizja(self.kierunek.LEFT):
                            self.kolizja(self.kierunek.LEFT)
                            return True
                        elif not self.czy_wyjdzie_poza_mape(self.kierunek.LEFT):
                            self.zmien_pole_na(self._x - 1, self._y)
                            quit_loop = True
                            return True
                        break
                    elif event.key == pygame.K_RIGHT:
                        if self.czy_kolizja(self.kierunek.RIGHT):
                            self.kolizja(self.kierunek.RIGHT)
                            return True
                        elif not self.czy_wyjdzie_poza_mape(self.kierunek.RIGHT):
                            self.zmien_pole_na(self._x + 1, self._y)
                            quit_loop = True
                            return True
                        break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self._swiat.czy_nacisnieto_przycisk_zapisania(punkt):
                        self._swiat.zapisz_stan()
                    elif self._swiat.czy_nacisnieto_przycisk_wczytania(punkt):
                        self._swiat.wczytaj_stan()
                        return True

    def wlacz_umiejetnosc(self):
        self._swiat.dodaj_komunikat("Człowiek użył Tarzcy Alzura")
        self.cooldown = 10
        self.aktywny = 5
        self.wlaczona_umiejetnosc = True
        self._swiat.rysuj_swiat()

    def aktualizuj_umiejetnosc(self):
        if self.cooldown != 0:
            self.cooldown -= 1
        if self.aktywny != 0:
            self.aktywny -= 1
            if self.aktywny == 0:
                self.wlaczona_umiejetnosc = False
        if self.wlaczona_umiejetnosc is True:
            self._swiat.dodaj_komunikat("Tarcza Alzura jest Włączona")

    def zniszcz_organizm(self):
        self._swiat.zakoncz_gre()

    def czy_walka(self, rodzaj, zwierze):
        if self.wlaczona_umiejetnosc is True and rodzaj == self.RodzajAtaku.ATAKOWANY:
            self._swiat.dodaj_komunikat("Człowiek odparł atak " + zwierze.get_gatunek())
            self.przenies_na_losowe_miejsce(zwierze)
            return False
        else:
            return True

    def przenies_na_losowe_miejsce(self, zwierze):
        j = randint(0, 3)
        for i in range(0, 4):
            r = self.kierunki[(j + i) % 4]
            if self.czy_kolizja(r) or self.czy_wyjdzie_poza_mape(r):
                continue
            elif i == 3:
                return
            else:
                break
        x, y = self._x, self._y
        if r == self.kierunek.UP:
            y -= 1
        elif r == self.kierunek.DOWN:
            y += 1
        elif r == self.kierunek.LEFT:
            x -= 1
        elif r == self.kierunek.RIGHT:
            x += 1
        zwierze.zmien_pole_na(x, y)

    def get_stan(self):
        stan = super(Czlowiek, self).get_stan()
        stan = stan[:-1]
        return stan + " " + str(self.wlaczona_umiejetnosc) + " " + str(self.cooldown) + " " + str(self.aktywny) + "\n"

    def ustaw_stan(self, text):
        super(Czlowiek, self).ustaw_stan(text)
        self.wlaczona_umiejetnosc = bool(text[7])
        self.cooldown = int(text[8])
        self.aktywny = int(text[9])
