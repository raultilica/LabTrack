from domain.student import Student
from domain.laborator import Laborator
from domain.asignare import Asignare
from datetime import datetime
from repo.asignare import RepoAsignare

class RepoAsignareFile(RepoAsignare):
    def __init__(self, cale):
        RepoAsignare.__init__(self)
        self.__cale = cale
        self.__citeste_din_fisier()

    @staticmethod
    def creeaza_student(id_student, nume, grup):
        """
        Functia creeaza un student Student
        :param id_student: int
        :param nume: string
        :param grup: int
        :return: Student
        """
        return Student(int(id_student), nume, int(grup))

    @staticmethod
    def creeaza_laborator(id_laborator, descriere, deadline):
        """
        Functia creeaza un laborator Laborator
        :param id_laborator: string
        :param descriere: string
        :param deadline: datetime
        :return: Laborator
        """
        return  Laborator(id_laborator, descriere, datetime.strptime(deadline, "%d/%m/%Y"))

    def __citeste_din_fisier(self):
        """
        Functia citeste din fisierul self.__cale rand cu rand datele necesare pentru a crea o asignare Asignare
        """
        with open(self.__cale, "r") as f:
            for line in f:
                line = line.strip().split(",")
                id_asignare = int(line[0])
                student = self.creeaza_student(int(line[1]), line[2], int(line[3]))
                laborator = self.creeaza_laborator(line[4], line[5], line[6])
                asignare = Asignare(id_asignare, student, laborator)
                try:
                    nota = float(line[7])
                    asignare.set_nota(nota)
                except ValueError:
                    pass
                RepoAsignare.add(self, asignare)

    def __scrie_in_fisier(self):
        """
        Functia scrie in fisierul self.__cale rand cu rand datele necesare pentru a crea o asignare Asignare
        """
        with open(self.__cale, "w") as f:
            asignari = RepoAsignare.get_list(self)
            for asignare in asignari.values():
                asignare_format = f"{asignare.get_id()},{asignare.get_student().get_id()},{asignare.get_student().get_nume()},{asignare.get_student().get_grup()},{asignare.get_laborator().get_id()},{asignare.get_laborator().get_descriere()},{asignare.get_laborator().get_deadline().day}/{asignare.get_laborator().get_deadline().month}/{asignare.get_laborator().get_deadline().year},{asignare.get_nota()}\n"
                f.write(asignare_format)

    def clear_list(self):
        """
        Functia goloseste dictionarul curent
        """
        RepoAsignare.clear_list(self)
        self.__scrie_in_fisier()

    def add(self, asignare):
        """
        Functia adauga in dictionar o asignare
        :param asignare: Asignare
        """
        RepoAsignare.add(self, asignare)
        self.__scrie_in_fisier()

    def set_nota(self):
        """
        Functia scrie in fisier in caz ca o asignare a fost evaluata
        """
        self.__scrie_in_fisier()