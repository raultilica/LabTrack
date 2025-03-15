from erori.erori import ValidError

class ValidatorLaborator:
    @staticmethod
    def validate(laborator):
        """
        Functia valideaza daca numaru laboratului, adica arg[0] este pozitiv, numarul problemei, adica arg[1] este pozitiva si daca descrierea e nevida
        :param laborator: Laborator
        :return: ValueError daca exista erori, nimic in caz contrar
        """
        erori = []
        arg = laborator.get_id().split("_")
        if int(arg[0]) <= 0:
            erori.append("numarul laboratorului este invalid")
        if int(arg[1]) <= 0:
            erori.append("numarul problemei este invalid")
        if laborator.get_descriere() == "":
            erori.append("descrierea nu poate fi nula")
        if erori:
            raise ValidError('\n'.join(erori))