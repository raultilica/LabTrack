class Student:
    def __init__(self, id_student, nume, grup):
        """
        Constructorul clasei Student
        :param id_student: int
        :param nume: string
        :param grup: int
        """
        self.__id_student = id_student
        self.__nume_student = nume
        self.__grup = grup

    def get_id(self):
        return self.__id_student

    def get_nume(self):
        return self.__nume_student

    def get_grup(self):
        return int(self.__grup)

    def set_nume(self, nume_nou):
        self.__nume_student = nume_nou

    def set_grup(self, grup_nou):
        self.__grup = grup_nou