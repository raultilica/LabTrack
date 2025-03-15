from erori.erori import RepoError

class RepoStudent:
    def __init__(self):
        self.__dictionar = {}

    def adaugare(self, data):
        """
        Functia adauga in dictionar un obiect
        :param data: obiect Student
        Output:
            ValueError daca id-ul este deja folosit
        """
        if data.get_id() in self.__dictionar:
            raise RepoError("id duplicat")
        self.__dictionar[data.get_id()] = data

    def stergere(self, id_student):
        """
        Functia sterge un obiect Student in functie de un id
        :param id_student: int
        Output:
            ValueError daca id-ul nu exista in dictionar
        """
        if id_student in self.__dictionar:
            del self.__dictionar[id_student]
        else:
            raise RepoError("id invalid")

    def modificare(self, id_student, student_nou):
        """
        Functia modifica un student Student
        :param id_student: int
        :param student_nou: Student
        :return:
        """
        if id_student not in self.__dictionar:
            raise RepoError("id-ul nu exista")
        student = self.__dictionar[id_student]
        student.set_nume(student_nou.get_nume())
        student.set_grup(student_nou.get_grup())

    def get_lista(self):
        """
        Functia obtine lungimea dictionarului curent
        :return: int
        """
        return self.__dictionar

    def clear_list(self):
        """
        Functia goloseste dictionarul curent
        """
        self.__dictionar = {}

    def size(self):
        """
        Functia obtine lungimea dictionarului curent
        :return: int
        """
        return len(self.__dictionar)

    def get_student_by_id(self, id_student):
        """
        Functia obtine un obiect Student in functie de un id
        :param id_student: int
        Output:
            RepoError daca id-ul nu exista in dictionar
        """
        if id_student in self.__dictionar:
            return self.__dictionar[id_student]
        else:
            raise RepoError("nu exista niciun student cu acest id")
