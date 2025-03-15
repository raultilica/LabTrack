class Laborator:
    def __init__(self, id_laborator, descriere, deadline):
        """
        Constructorul clasei Laborator
        :param id_laborator: string
        :param descriere: string
        :param deadline: datetime
        """
        self.__id = id_laborator
        self.__descriere = descriere
        self.__deadline = deadline

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def get_id(self):
        return self.__id

    def set_descriere(self, descriere_noua):
        self.__descriere = descriere_noua

    def set_deadline(self, deadline_nou):
        self.__deadline = deadline_nou