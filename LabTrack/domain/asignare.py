from erori.erori import DomainError

class Asignare:
    def __init__(self, id_asignare, student, laborator):
        self.__id = id_asignare
        self.__student = student
        self.__laborator = laborator
        self.__nota = None

    def get_id(self):
        return self.__id

    def get_student(self):
        return self.__student

    def get_laborator(self):
        return self.__laborator

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0.0 < nota <= 10:
            self.__nota = nota
        else:
            raise DomainError("nota invalida")