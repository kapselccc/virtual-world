import sys
from random import randint

import pygame

import defines
from Antylopa import Antylopa
from Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
from Cyber_owca import Cyber_owca
from Czlowiek import Czlowiek
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from Wilcze_Jagody import Wilcze_Jagody
from Wilk import Wilk
from Zolw import Zolw


class Swiat:
    white = (255, 255, 255)

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.gatunki = ["Antylopa", "Lis", "Owca", "Wilk", "Zolw", "Cyber-owca", "Barszcz Sosnowskiego", "Guarana",
                        "Mlecz", "Trawa", "Wilcze Jagody"]
        self.tura = 0
        self.stop_game = False
        self.mapa = []
        self.wczytano_stan = False
        for x in range(0, height):
            x = []
            self.mapa.append(x)
            for y in range(0, width):
                x.append(None)
        self.organizmy = []
        self.komunikat = ""
        self.screen = pygame.display.set_mode((defines.MAP_WIDTH + 200, defines.MAP_HEIGHT + 200))
        pygame.display.set_caption("Wirtualny Świat: Kacper Cencelewski 184848")

    def wyswietl_mape(self):
        self.screen.fill(Swiat.white)
        self.rysuj_ramke()
        for element in self.organizmy:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(defines.MAP_X + element.get_x() * defines.OBIEKT_WIDTH,
                                                                 defines.MAP_Y + element.get_y() * defines.OBIEKT_WIDTH,
                                                                 defines.OBIEKT_WIDTH, defines.OBIEKT_WIDTH))
            pygame.Surface.blit(self.screen, element.get_zdjecie(),
                                (defines.MAP_X + element.get_x() * defines.OBIEKT_WIDTH + 1,
                                 defines.MAP_Y + element.get_y() * defines.OBIEKT_WIDTH + 1))

    def stworz_organizm(self, gatunek, x, y):
        if gatunek == "Antylopa":
            self.organizmy.append(Antylopa(self, x, y))
        elif gatunek == "Barszcz Sosnowskiego":
            self.organizmy.append(Barszcz_Sosnowskiego(self, x, y))
        elif gatunek == "Czlowiek":
            self.organizmy.append(Czlowiek(self, x, y))
        elif gatunek == "Guarana":
            self.organizmy.append(Guarana(self, x, y))
        elif gatunek == "Lis":
            self.organizmy.append(Lis(self, x, y))
        elif gatunek == "Mlecz":
            self.organizmy.append(Mlecz(self, x, y))
        elif gatunek == "Owca":
            self.organizmy.append(Owca(self, x, y))
        elif gatunek == "Trawa":
            self.organizmy.append(Trawa(self, x, y))
        elif gatunek == "Wilcze Jagody":
            self.organizmy.append(Wilcze_Jagody(self, x, y))
        elif gatunek == "Wilk":
            self.organizmy.append(Wilk(self, x, y))
        elif gatunek == "Zolw":
            self.organizmy.append(Zolw(self, x, y))
        elif gatunek == "Cyber-owca":
            self.organizmy.append(Cyber_owca(self, x, y))

        self.mapa[y][x] = self.organizmy[len(self.organizmy) - 1]
        self.organizmy[len(self.organizmy) - 1].zaladuj_zdjecie()

    def aktualizuj_mape(self, organizm, x, y):
        self.mapa[organizm.get_y()][organizm.get_x()] = None
        self.mapa[y][x] = organizm

    def rysuj_ramke(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(defines.MAP_X - 15, defines.MAP_Y - 15,
                                                             defines.MAP_WIDTH + 30, defines.MAP_HEIGHT + 30))
        pygame.draw.rect(self.screen, (159, 254, 1), pygame.Rect(defines.MAP_X - 10, defines.MAP_Y - 10,
                                                                 defines.MAP_WIDTH + 20, defines.MAP_HEIGHT + 20))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(defines.MAP_X, defines.MAP_Y,
                                                                   defines.MAP_WIDTH, defines.MAP_HEIGHT))

    def stworz_pierwsze_organizmy(self):
        x = randint(0, self.width - 1)
        y = randint(0, self.height - 1)
        self.stworz_organizm("Czlowiek", x, y)
        for i in range(0, defines.POCZATKOWA_LICZBA_ZWIERZAT + defines.POCZATKOWA_LICZBA_ROSLIN):
            while not self.mapa[y][x] is None:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
            if i < defines.LICZBA_GATUNKOW_ZWIERZAT:
                self.stworz_organizm(self.gatunki[i], x, y)
            elif i < defines.POCZATKOWA_LICZBA_ZWIERZAT:
                self.stworz_organizm(self.gatunki[randint(0, defines.LICZBA_GATUNKOW_ZWIERZAT - 1)], x, y)
            elif i - defines.POCZATKOWA_LICZBA_ZWIERZAT < defines.LICZBA_GATUNKOW_ROSLIN:
                self.stworz_organizm(
                    self.gatunki[i - defines.POCZATKOWA_LICZBA_ZWIERZAT + defines.LICZBA_GATUNKOW_ZWIERZAT], x, y)
            else:
                self.stworz_organizm(self.gatunki[randint(defines.LICZBA_GATUNKOW_ZWIERZAT,
                                                          defines.LICZBA_GATUNKOW_ZWIERZAT + defines.LICZBA_GATUNKOW_ROSLIN - 1)],
                                     x, y)

    def usun_organizm(self, organizm):
        self.mapa[organizm.get_y()][organizm.get_x()] = None
        self.organizmy.remove(organizm)

    def czy_zajete(self, x, y):
        if self.width > x >= 0 and 0 <= y < self.height:
            if self.mapa[y][x] is not None:
                return True
            else:
                return False
        else:
            return False

    def czy_ten_sam_gatunek(self, o1, o2):
        if o1.get_gatunek() == o2.get_gatunek():
            return True
        else:
            return False

    def dodaj_komunikat(self, text):
        self.komunikat += text + "\n"

    def wyswietl_komunikat(self):
        kom = self.komunikat.split("\n")
        i = 0
        for komunikat in kom:
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(komunikat, True, (0, 0, 0))
            self.screen.blit(text, (defines.MAP_X + 10, defines.MAP_Y + defines.MAP_HEIGHT + 20 + i * 20))
            i += 1
        self.komunikat = ""

    def wyswietl_ture(self):
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render("Tura: " + str(self.tura), True, (0, 0, 0))
        self.screen.blit(text, (defines.MAP_X + defines.MAP_WIDTH - 100, 10))

    def zwroc_organizm_pola(self, x, y):
        return self.mapa[y][x]

    def aktualizuj_ture(self):
        self.tura += 1
        for org in self.organizmy:
            org.aktualizuj_zmienne()

    def wykonaj_ture(self):
        while not self.stop_game:
            self.organizmy.sort(key=lambda x: x.get_inicjatywa(), reverse=True)
            self.aktualizuj_ture()
            for org in self.organizmy:
                if not self.stop_game:
                    if org.get_gatunek() == "Czlowiek":
                        org.aktualizuj_umiejetnosc()
                        self.rysuj_swiat()
                    if not org.akcja():
                        self.stop_game = True
                        break
                else:
                    break
        self.wyswietl_koniec()

    def rysuj_swiat(self):
        self.wyswietl_mape()
        self.wyswietl_ture()
        self.wyswietl_komunikat()
        self.wyswietl_przyciski()
        pygame.display.flip()

    def zakoncz_gre(self):
        self.stop_game = True

    def wyswietl_koniec(self):
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("Człowiek umarł w " + str(self.tura) + " turze", True, (0, 0, 0))
        self.screen.fill(Swiat.white)
        self.screen.blit(text, (60, defines.MAP_HEIGHT / 2,))
        pygame.display.flip()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

    def zapisz_stan(self):
        self.wczytano_stan = True
        with open("stan_gry.txt", "w") as file:
            file.write(str(self.tura) + "\n")
            for org in self.organizmy:
                file.write(org.get_stan())

    def read_x(self, text):
        text = text.split()
        if text[1].isdigit():
            return int(text[1])
        else:
            return int(text[2])

    def read_y(self, text):
        text = text.split()
        if text[1].isdigit():
            return int(text[2])
        else:
            return int(text[3])

    def wczytaj_stan(self):
        self.organizmy.clear()
        self.mapa.clear()
        self.komunikat = ""
        for x in range(0, self.height):
            x = []
            self.mapa.append(x)
            for y in range(0, self.width):
                x.append(None)
        with open("stan_gry.txt", "r") as file:
            linia = file.readlines()
        self.tura = int(linia[0][:-1])
        for i in range(1, len(linia)):
            x = self.read_x(linia[i])
            y = self.read_y(linia[i])
            linia[i] = linia[i].split()
            if linia[i][1].isdigit():
                self.stworz_organizm(linia[i][0], x, y)
            else:
                self.stworz_organizm(f'{linia[i][0]} {linia[i][1]}', x, y)
            self.organizmy[i - 1].ustaw_stan(linia[i])

    def wyswietl_przyciski(self):
        pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(defines.MAP_X, defines.MAP_Y - defines.BUTTON_HEIGHT - 20,
                                                             defines.BUTTON_WIDTH, defines.BUTTON_HEIGHT))
        font = pygame.font.Font('freesansbold.ttf', 19)
        text = font.render("Zapisz stan", True, (255, 255, 255))
        self.screen.blit(text, (defines.MAP_X + 30, defines.MAP_Y - defines.BUTTON_HEIGHT - 5))
        if self.wczytano_stan:
            text2 = text = font.render("Wczytaj ze stanu", True, (255, 255, 255))
            pygame.draw.rect(self.screen, (50, 50, 50),
                             pygame.Rect(defines.MAP_X + defines.BUTTON_WIDTH + 20, defines.MAP_Y - defines.BUTTON_HEIGHT - 20,
                                         defines.BUTTON_WIDTH, defines.BUTTON_HEIGHT))
            self.screen.blit(text2, (defines.MAP_X + defines.BUTTON_WIDTH + 30, defines.MAP_Y - defines.BUTTON_HEIGHT - 5))

    def czy_nacisnieto_przycisk_zapisania(self, punkt):
        if(defines.MAP_X <= punkt[0] <= defines.MAP_X + defines.BUTTON_WIDTH and
                defines.MAP_Y - defines.BUTTON_HEIGHT - 20 <= punkt[1] <= defines.MAP_Y - defines.BUTTON_HEIGHT - 20 + defines.BUTTON_HEIGHT):
            return True
        else:
            return False

    def czy_nacisnieto_przycisk_wczytania(self, punkt):
        if (defines.MAP_X + defines.BUTTON_WIDTH + 20 <= punkt[0] <= defines.MAP_X + defines.BUTTON_WIDTH + 20 + defines.BUTTON_WIDTH and
                defines.MAP_Y - defines.BUTTON_HEIGHT - 20 <= punkt[1] <= defines.MAP_Y - defines.BUTTON_HEIGHT - 20 + defines.BUTTON_HEIGHT):
            return True
        else:
            return False
