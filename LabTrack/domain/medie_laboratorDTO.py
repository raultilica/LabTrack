class MedieLaboratorDTO:
    def __init__(self, numar_laborator, numar_problema, medie):
        self.__numar_laborator = numar_laborator
        self.__numar_problema = numar_problema
        self.__medie = medie

    def get_numar_laborator(self):
        return self.__numar_laborator

    def get_numar_problema(self):
        return self.__numar_problema

    def get_medie(self):
        return self.__medie