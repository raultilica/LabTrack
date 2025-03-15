from erori.erori import RepoError

class LaboratorRepo:
    def __init__(self):
        self.__dictionar = {}

    def adaugare(self, data):
        """
        Functia adauga in dictionar un obiect
        :param data: obiect Laborator
        Output:
            ValueError daca id-ul rezultat din laborator_tema este deja folosit
        """
        if data.get_id() in self.__dictionar:
            raise RepoError(f"pentru laboratorul {data.get_id().split("_")[0]} exista deja tema {data.get_id().split("_")[1]}")
        self.__dictionar[data.get_id()] = data

    def modificare(self, id_laborator, laborator_nou):
        """
        Functia modifica datele unui laborator
        :param id_laborator: string
        :param laborator_nou: Laborator
        """
        if id_laborator not in self.__dictionar:
            raise RepoError("id inexistent")
        laborator = self.__dictionar[id_laborator]
        laborator.set_descriere(laborator_nou.get_descriere())
        laborator.set_deadline(laborator_nou.get_deadline())

    def get_lista_laboratoare(self):
        """
        Functia obtine dictionarul curent
        :return: dictionar
        """
        return self.__dictionar

    def get_size(self):
        """
        Functia obtine lungimea dictionarului curent
        :return: int
        """
        return len(self.__dictionar)

    def clear_list(self):
        """
        Functia sterge continutul dictionarului curent+
        """
        self.__dictionar = {}

    def get_laborator_by_id(self, id_cautat):
        """
        Functia obtine un obiect laborator in functia de un id
        :param id_cautat: int
        Output:
            ValueError daca id-ul nu exista
        """
        if id_cautat in self.__dictionar:
            return self.__dictionar[id_cautat]
        else:
            raise RepoError("nu exista niciun laborator cu acest id")

    def stergere(self, id_lab):
        """
        Functia sterge un obiect laborator
        :param id_lab: int
        Output:
            ValueError daca id-ul nu exista
        """
        if id_lab in self.__dictionar:
            del self.__dictionar[id_lab]
        else:
            raise RepoError("id inexistetent")