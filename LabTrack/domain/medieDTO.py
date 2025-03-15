class MedieDTO:
    def __init__(self, nume, medie):
        self.__nume = nume
        self.__medie = medie

    def get_nume(self):
        return self.__nume

    def get_medie(self):
        return self.__medie