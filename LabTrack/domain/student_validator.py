from erori.erori import ValidError

class ValidatorStudent:
    @staticmethod
    def validate(student):
        """
        Functia valideaza daca idul este pozitiv, numele e nevid si daca grupul este pozitiv
        :param student: Student
        :return: ValueError daca exista erori, nimic in caz contrar
        """
        erori = []
        if student.get_id() < 0:
            erori.append(f"idul trebuie sa fie pozitiv")
        if student.get_nume() == "":
            erori.append(f"numele nu poate fi vid")
        if student.get_grup() < 0:
            erori.append(f"grupa trebuie sa fie pozitiva")
        if erori:
            raise ValidError("\n".join(erori))






