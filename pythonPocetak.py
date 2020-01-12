class Karta(object):
#dvorana, redovi, mjesta u redovima
    __karta_info = {1:('A',8,10),
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
        return Karta.__karta_info.keys()

    @staticmethod
    def vrste():
        return list(Karta.__vrsta_karte)

    def __init__(self,broj,vrsta,dostupna = False):
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

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r)' % (self.__broj, self.__vrsta, self.__dostupna)

    def __str__(self):
        return self.vrsta.title() + ' ' + self.vrsta

for vrsta in Karta.vrste():
    for broj in Karta.brojevi():
        k = Karta (broj, vrsta)
        print('%r %s %d %d' % (k, k, k.red, k.mjesto))
    

