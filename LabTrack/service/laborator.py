from domain.laborator import Laborator
from erori.erori import *
from datetime import datetime
import string
import random

class ServiceLaborator:
    def __init__(self, validator_laborator, laborator_repo):
        self.__validator = validator_laborator
        self.__repo = laborator_repo

    def add(self, id_laborator, descriere, deadline):
        """
        Functia adauga un obiect Laborator in repository-ul destinat
        :param id_laborator: string
        :param descriere: string
        :param deadline: datetime
        :return: ValueError daca numar_laborator <= 0, numar_problema <= 0, descriere == ""
                 ValueError daca id-ul a fost deja folosit
        """
        laborator = Laborator(id_laborator, descriere, deadline)
        self.__validator.validate(laborator)
        self.__repo.adaugare(laborator)

    def modificare(self, id_laborator, descriere, deadline):
        """
        Functia modifica un laborator existent cu date primite de la user
        :param id_laborator: string
        :param descriere: string
        :param deadline: detetime
        :return: ValueError daca datele sunt invalide, nu exista un laborator cu id-ul id_laborator
        """
        laborator_nou = Laborator(id_laborator, descriere, deadline)
        self.__validator.validate(laborator_nou)
        self.__repo.modificare(id_laborator, laborator_nou)

    def genereaza_laborator(self, numar_laboratoare, id_folosite):
        lista_ascii = string.ascii_letters
        while True:
            id_laborator = f"{random.randrange(1, (numar_laboratoare + self.__repo.get_size()) * 10)}_{random.randrange(1, (numar_laboratoare + self.__repo.get_size()) * 10)}"
            if id_laborator not in id_folosite:
                break
        id_folosite.add(id_laborator)
        descriere_laborator = ''.join(random.choices(lista_ascii, k=10))
        deadline = datetime(random.randrange(1970, datetime.now().year), random.randrange(1, 12), random.randrange(1, 28))
        return Laborator(id_laborator, descriere_laborator, deadline)

    def genereaza_laboratoare(self, numar_laboratoare):
        if numar_laboratoare <= 0:
            raise ServiceError("numar invalid de laboratoare")
        id_folosite = set()
        index = 0
        while index < numar_laboratoare:
            laborator = self.genereaza_laborator(numar_laboratoare, id_folosite)
            try:
                self.__repo.adaugare(laborator)
                index += 1
            except RepoError:
                id_folosite.add(laborator.get_id())

    #Nerecursiv
    """
    def cauta_dupa_data(self, data):
        
        Functia introduce intr-un dictionar toate obiectele Laborator care au ca deadline data data
        :param data: datetime
        :return: dictionar
        
        lista_laboratoare = {}
        for lab in self.__repo.get_lista_laboratoare().values():
            if lab.get_deadline() == data:
                lista_laboratoare[lab.get_id()] = lab
        return lista_laboratoare
        """

    #Recursiv
    def cauta_recursiv(self, lista, data, dictionar_final, index = 0):
        """
        Functia cauta recursiv intr o lista elementele care au data corespunzxatoare
        :param lista: lista
        :param data: obiect datetime
        :param dictionar_final: dictionar
        :param index: int
        :return: dictionar
        """
        if index == len(lista):
            return dictionar_final
        if lista[index][1].get_deadline() == data:
            dictionar_final[lista[index][0]] = lista[index][1]
        return self.cauta_recursiv(lista, data, dictionar_final, index + 1)

    def cauta_dupa_data(self, data):
        """
        Functia transforma un dictionar intr o lista
        :param data: datetime
        :return: un dictionar
        """
        dictionar_final = {}
        dic = self.__repo.get_lista_laboratoare()
        lista = [(key, value) for key, value in dic.items()]
        dictionar_final = self.cauta_recursiv(lista, data, dictionar_final)
        return dictionar_final

    def get_size(self):
        return self.__repo.get_size()

    def get_lista(self):
        return self.__repo.get_lista_laboratoare()

    def get_lab_by_id(self, id_lab):
        return self.__repo.get_laborator_by_id(id_lab)

    def delete_lab_by_id(self, id_lab):
        self.__repo.stergere(id_lab)

    def populare_laboratoare(self):
        self.add("1_1", "Creeaza o clasa de elevi", datetime(2025, 12, 25))
        self.add("2_1", "Implementeaza un algoritm de sortare", datetime(2025, 10, 15))
        self.add("3_2", "Creeaza o aplicatie CRUD", datetime(2025, 10, 15))
