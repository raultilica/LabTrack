from repo.laborator import LaboratorRepo
from domain.laborator import Laborator
from datetime import datetime

class RepoLaboratorFile(LaboratorRepo):
    def __init__(self, cale):
        LaboratorRepo.__init__(self)
        self.__cale = cale
        self.__citeste_din_fisier()

    def __citeste_din_fisier(self):
        """
        Functia citeste din fisierul self.__cale rand cu rand datele necesare pentru a crea un lab Laborator
        """
        with open(self.__cale, "r") as f:
            for line in f:
                line = line.strip().split(",")
                id_laborator = line[0]
                descriere = line[1]
                deadline = datetime.strptime(line[2], "%d/%m/%Y")
                laborator = Laborator(id_laborator, descriere, deadline)
                LaboratorRepo.adaugare(self, laborator)

    def __scrie_in_fisier(self):
        """
        Functia scrie in fisierul self.__cale rand cu rand datele necesare pentru a crea un lab Laborator
        """
        with open(self.__cale, "w") as f:
            labs = LaboratorRepo.get_lista_laboratoare(self)
            for lab in labs.values():
                format_lab = f"{lab.get_id()},{lab.get_descriere()},{lab.get_deadline().day}/{lab.get_deadline().month}/{lab.get_deadline().year}\n"
                f.write(format_lab)

    def clear_list(self):
        """
        Functia goloseste dictionarul curent
        """
        LaboratorRepo.clear_list(self)
        self.__scrie_in_fisier()

    def adaugare(self, data):
        """
        Functia adauga in dictionar un Laborator
        :param data: Laborator
        """
        LaboratorRepo.adaugare(self, data)
        self.__scrie_in_fisier()

    def modificare(self, id_laborator, data):
        """
        Functia scrie in fisier datele noi ale unui Laborator
        :param id_laborator: string
        :param data: Laborator
        :return:
        """
        LaboratorRepo.modificare(self, id_laborator, data)
        self.__scrie_in_fisier()

    def stergere(self, id_lab):
        """
        Functia scrie in fisier datele ramase dupa eliminea unui Laborator
        :id_lab: string
        """
        LaboratorRepo.stergere(self, id_lab)
        self.__scrie_in_fisier()

