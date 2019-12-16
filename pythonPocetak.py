class Karta(object):
#dvorana, redovi, mjesta u redovima
    __karte_info - {1:('A',8,10),
                    2:('B',5,6),
                    3:('C',12,20),
                    4:('D',23,12),
                    5:('E',20,10),
                    6:('F',7,4),
                    7:('G',13,14),
                    8:('H',7,8),
                    9:('I',2,8),
                    10:('J',30,22)
                    }
    
                    
    __vrsta_karte = ['standardna','djecja','studentska','pretplata']

    
    @staticmethod
    def brojevi():
        return  Karta.__karte_info.keys()

    @staticmethod
    def vrsta():
        return list(Karta.__vrsta_karte)

    def __init__(self,broj,vrsta,dostupna-false):
        self.__broj=broj
        self.__vrsta=vrsta
        self.__dostupna=dostupna

    @property
    def broj(self):
        return self.__broj

    @property
    def vrsta(self):
        return self.__vrsta

    @property
    def dvorana(self):
        return Karta.__karta_info[self.__broj][0]

    @property
    def red(self):
        return Karta.__karta_info[self.__broj][1]

    @property
    def mjesto(self):
        return Karta.__karta_info[self.__broj][2]

    @property
    def dostupna(self):
        return self.__dostupna

    @dostupna.setter
    def dostupna(self,value):
        self.__dostupna=value
    
    
    
