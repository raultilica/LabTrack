from erori.erori import RepoError

class RepoAsignare:
    def __init__(self):
        self.__lista = {}

    def add(self, asignare):
        """
        Functia primeste un obiect Asignare si il adauga un lista daca nu exista deja unul cu acelasi id
        :param asignare: obj Asignare
        :return: RepoError daca id-ul se repeta
        """
        if asignare.get_id() in self.__lista:
            raise RepoError("id duplicat")
        self.__lista[asignare.get_id()] = asignare

    def interschimba(self, lista_noua):
        """
        Functia schimba continutul listei self.__lista cu conntinutul unei alte liste
        :param lista_noua: dictionar
        """
        self.__lista = lista_noua

    def get_asignare_by_id(self, id_asignare):
        """
        Functia intoarce un obiect de tipul Asignare, daca exista in lista cu id-ul specificat
        :param id_asignare: int
        :return: RepoError daca nu exista o asignare cu id id_asignare, un obiect Asignare daca exista in dictionar
        """
        if id_asignare not in self.__lista:
            raise RepoError("id inexistent")
        return self.__lista[id_asignare]

    def delete_by_id(self, id_asignare):
        """
        Functia sterge din dictionar un obiect de tipul Asignare daca acesta exista
        :param id_asignare: int
        :return: RepoError daca nu exista un obiect Asignare in dictionar
        """
        if id_asignare not in self.__lista:
            raise RepoError("id inexistent")
        del self.__lista[id_asignare]

    def clear_list(self):
        """
        Functia elimina tot contintul dictionarului curent
        """
        self.__lista = {}

    def set_nota(self):
        """
        Folosita doar pentru repository cu fisier
        """
        pass

    def get_size(self):
        """
        Functia obtine lungimea dictionarului
        :return: lungimea dictionarului
        """
        return len(self.__lista)

    def get_list(self):
        """
        Functia obtine dictionarul curent
        :return: dictionarul curent
        """
        return self.__lista