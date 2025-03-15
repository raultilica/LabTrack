from erori.erori import ValidError

class ValidatorAsignare:
    @staticmethod
    def validate(asignare):
        """
        Functia valideaza daca o asignare are id-ul valid
        :param asignare: Asignare
        :return: ValueError daca exista eroare, nimic in caz contrar
        """
        erori = []
        if asignare.get_id() <= 0:
            erori.append("id-ul trebuie sa fie pozitiv")
        if erori:
            raise ValidError('\n'.join(erori))
