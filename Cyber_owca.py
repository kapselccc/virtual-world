from Zwierze import Zwierze


class Cyber_owca(Zwierze):
    def __init__(self, swiat, x, y):
        super(Cyber_owca, self).__init__(swiat, x, y)
        self._sila = 11
        self._inicjatywa = 4
        self._gatunek = "Cyber-owca"
        self.filename = "cyber-owca.png"

    def akcja(self):
        if not self.czy_istnieje_barszcz():
            return self.wykonaj_ruch()
        else:
            kierunek = self.zwroc_kierunek()
            if self.zwroc_odleglosc_od_barszczu() > 1:
                if self.czy_kolizja(kierunek):
                    self.kolizja(kierunek)
                    return True
                elif not self.czy_wyjdzie_poza_mape(kierunek):
                    self.wywolaj_zmiane_pola_kierunku(kierunek)
                    return True
            else:
                self.kolizja(kierunek)
        return True

    def czy_istnieje_barszcz(self):
        for i in range(0, len(self._swiat.organizmy)):
            if self._swiat.organizmy[i].get_gatunek() == "Barszcz Sosnowskiego":
                return True
        return False

    def znajdz_najblizszy_barszcz(self):
        x = []
        y = []
        min_odleglosc = -1
        index = -1
        for i in range(0, len(self._swiat.organizmy)):
            if self._swiat.organizmy[i].get_gatunek() == "Barszcz Sosnowskiego":
                x.append(self._swiat.organizmy[i].get_x())
                y.append(self._swiat.organizmy[i].get_y())
        for i in range(0, len(x)):
            d_x = abs(self._x - x[i])
            d_y = abs(self._y - y[i])
            temp = d_x + d_y
            if min_odleglosc < 0:
                min_odleglosc = temp
                index = i
            elif min_odleglosc > temp:
                min_odleglosc = temp
                index = i
        return self._swiat.zwroc_organizm_pola(x[index], y[index])

    def zwroc_kierunek(self):
        barszcz = self.znajdz_najblizszy_barszcz()
        x = barszcz.get_x()
        y = barszcz.get_y()
        d_x = abs(self._x - x)
        d_y = abs(self._y - y)
        if d_x >= d_y:
            if self._x > x:
                return self.kierunek.LEFT
            else:
                return self.kierunek.RIGHT
        else:
            if self._y > y:
                return self.kierunek.UP
            else:
                return self.kierunek.DOWN

    def zwroc_odleglosc_od_barszczu(self):
        barszcz = self.znajdz_najblizszy_barszcz()
        x = barszcz.get_x()
        y = barszcz.get_y()
        d_x = abs(self._x - x)
        d_y = abs(self._y - y)
        return d_x + d_y
