from domain.student import Student
from erori.erori import *
import random
import string

class ServiceStudent:
    def __init__(self, validator_student, student_repo):
        self.__repo = student_repo
        self.__validator = validator_student

    def add(self, id_student, nume, grup):
        """
        Functia adauga un obiect Student in repository-ul destinatie
        :param id_student: int
        :param nume: string
        :param grup: int
        :return: ValueError daca numar_laborator <= 0, numar_problema <= 0, descriere == ""
                 ValueError daca id-ul a fost deja folosit
        """
        student = Student(id_student, nume, grup)
        self.__validator.validate(student)
        self.__repo.adaugare(student)

    def actualizare(self, id_student, nume, grup):
        """
        Functia actualizeaza un obiect Student din repository-ul destinatie
        :param id_student: int
        :param nume: string
        :param grup: int
        :return: ValueError daca numar_laborator <= 0, numar_problema <= 0, descriere == ""
                 ValueError daca id-ul nu exista
        """
        student_nou = Student(id_student, nume, grup)
        self.__validator.validate(student_nou)
        self.__repo.modificare(id_student, student_nou)

    #Nerecursiv
    """
    def cauta_student(self, nume):
        Functia cauta in repository-ul de studenti, studentii al caror nume coincide cu numele nume
        :param nume: string
        :return: lista_studenti
        lista_studenti = {}
        for student in self.__repo.get_lista().values():
            if student.get_nume() == nume:
                lista_studenti[student.get_id()] = student
        return lista_studenti
    """

    #Recursiv
    def cauta_recursiv(self, lista, nume, dictionar_final, index = 0):
        """
        Functia cauta recursiv intr o lista elementele care un nume corespunzator
        :param lista: lista
        :param nume: string
        :param dictionar_final: dictionar
        :param index: int
        :return: dictionar
        """
        if index == len(lista):
            return dictionar_final
        if lista[index][1].get_nume() == nume:
            dictionar_final[lista[index][0]] = lista[index][1]
        return self.cauta_recursiv(lista, nume, dictionar_final, index + 1)

    def cauta_student(self, nume):
        """
        Functia transforma un dictionar intr o lista
        :param nume: string
        :return: un dictionar
        """
        dictionar_final = {}
        dic = self.__repo.get_lista()
        lista = [(key, value) for key, value in dic.items()]
        dictionar_final = self.cauta_recursiv(lista, nume, dictionar_final)
        return dictionar_final

    def genereaza_student(self, numar_studenti, id_folosite):
        """
        Functia genereaza date aleatorii, valide, pentru a putea fi creat un nou obiect de tip Student
        :param numar_studenti: int
        :param id_folosite: set
        :return: student Student
        """
        lista_ascii = string.ascii_letters
        while True:
            id_student = random.randrange(1, (numar_studenti +  self.__repo.size())* 10)
            if id_student not in id_folosite:
                break
        id_folosite.add(id_student)
        nume_student = ''.join(random.choices(lista_ascii, k=10))
        grupa = random.randrange(100, 999)
        return Student(id_student, nume_student, grupa)

    def genereaza_studenti(self, numar_studenti):
        """
        Functia genereaza un numar egal cu numar_studenti de obiecte de tip Student, care vor fi adaugare in repo
        :param numar_studenti: int
        :return: ValueError daca numarul de studenti este invalid, nimic in caz contrar
        """
        if numar_studenti <= 0:
            raise ServiceError("numar invalid de studenti")
        id_folosite = set()
        index = 0
        while index < numar_studenti:
            student = self.genereaza_student(numar_studenti, id_folosite)
            try:
                self.__repo.adaugare(student)
                index += 1
            except RepoError:
                id_folosite.add(student.get_id())

    def get_lista(self):
        """
        Functia obtine dictionarul curent
        :return:
        """
        return self.__repo.get_lista()

    def size(self):
        """
        Functia obtine numarul de obiecte din repository-ul curent
        :return:
        """
        return self.__repo.size()

    def get_student_by_id(self, id_student):
        """
        Functia obtine studentul cu id-ul id_student
        :param id_student: int
        :return: Student
        """
        return self.__repo.get_student_by_id(id_student)

    def populare_students(self):
        self.add(1, "Ana Popescu", 213)
        self.add(3, "Katalin Nagy", 121)
        self.add(4, "Ioan Ionescu", 231)