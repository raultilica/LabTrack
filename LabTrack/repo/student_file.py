from repo.student import RepoStudent
from domain.student import Student

class RepoStudentFile(RepoStudent):
    def __init__(self, cale):
        RepoStudent.__init__(self)
        self.__cale = cale
        self.__citeste_din_fisier()

    def __citeste_din_fisier(self):
        """
        Functia citeste din fisierul self.__cale datele necesare pentru adaugarea in repo a obiectelor
        """
        with open(self.__cale, "r") as f:
            linii = f.readlines()

        for linie in linii:
            linie = linie.strip().split(",")
            id_student = int(linie[0])
            nume_student = linie[1]
            grup = int(linie[2])
            student = Student(id_student, nume_student, grup)
            RepoStudent.adaugare(self, student)

    def __scrie_in_fisier(self):
        """
        Functia scrie in fisierul self.__cale rand cu rand datele necesare pentru a crea un student Student
        """
        with open(self.__cale, "w") as f:
            studenti = RepoStudent.get_lista(self)
            for student in studenti.values():
                student_format = f"{student.get_id()},{student.get_nume()},{student.get_grup()}\n"
                f.write(student_format)

    def clear_list(self):
        """
        Functia goloseste dictionarul curent
        """
        RepoStudent.clear_list(self)
        self.__scrie_in_fisier()

    def adaugare(self, data):
        """
        Functia adauga in dictionar un Laborator
        :param data: Student
        """
        RepoStudent.adaugare(self, data)
        self.__scrie_in_fisier()

    def stergere(self, id_student):
        """
        Functia scrie in fisier datele ramase dupa eliminea unui Student
        :id_lab: int
        """
        RepoStudent.stergere(self, id_student)
        self.__scrie_in_fisier()

    def modificare(self, id_student, student_nou):
        """
        Functia scrie in fisier datele noi ale unui Student
        :param id_student: int
        :param student_nou: Student
        :return:
        """
        RepoStudent.modificare(self, id_student, student_nou)
        self.__scrie_in_fisier()


