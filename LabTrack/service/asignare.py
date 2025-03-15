from domain.asignare import Asignare
from domain.medieDTO import MedieDTO
from domain.medie_laboratorDTO import MedieLaboratorDTO
from sortari import insertion_sort, comb_sort
from erori.erori import *

class ServiceAsignare:
    def __init__(self, repo_student, repo_laborator, repo_asignare, validator_asignare):
        self.__repo_student = repo_student
        self.__repo_laborator = repo_laborator
        self.__repo_asignare = repo_asignare
        self.__validator_asignare = validator_asignare

    def add(self, id_asignare, id_student, id_laborator):
        """
        Functia adauga o asignare intre un student si un laborator in repository-ul destinat
        :param id_asignare: int - identificator unic pentru asignare
        :param id_student: int - identificatorul studentului
        :param id_laborator: int - identificatorul laboratorului
        :return: ServiceError daca studentul este deja asignat la acelasi laborator
                 RepoError daca id_asignare se repeta sau daca id_student/id_laborator nu exista
        """
        student = self.__repo_student.get_student_by_id(id_student)
        laborator = self.__repo_laborator.get_laborator_by_id(id_laborator)
        lista_asignari = self.__repo_asignare.get_list()
        for asignare in lista_asignari.values():
            if asignare.get_student().get_id() == id_student and asignare.get_laborator().get_id() == id_laborator:
                raise ServiceError(f"Studentul {student.get_nume()} are deja asignat laboratorul {laborator.get_id()}")
        asignare = Asignare(id_asignare, student, laborator)
        self.__validator_asignare.validate(asignare)
        self.__repo_asignare.add(asignare)

    def delete_by_student_id(self, id_student):
        """
        Functia sterge o asignare intre un student si un laborator pe baza id-ului de student
        :param id_student: int - identificatorul studentului
        :return: RepoError daca nu exista studentul cu id_student
        """
        lista_noua = {}
        lista_asignari = self.__repo_asignare.get_list()
        for asignare in lista_asignari.values():
            if asignare.get_student().get_id() != id_student:
                lista_noua[asignare.get_id()] = asignare
        self.__repo_asignare.interschimba(lista_noua)
        self.__repo_student.stergere(id_student)

    def delete_by_lab_id(self, id_lab):
        """
        Functia sterge o asignare intre un student si un laborator, pe baza id-ului de lab
        :param id_lab: int - identificatorul laboratorului
        :return: RepoError daca nu exista laboratorul cu id_lab
        """
        lista_noua = {}
        lista_asignari = self.__repo_asignare.get_list()
        for asignare in lista_asignari.values():
            if asignare.get_laborator().get_id() != id_lab:
                lista_noua[asignare.get_id()] = asignare
        self.__repo_asignare.interschimba(lista_noua)
        self.__repo_laborator.stergere(id_lab)

    def noteaza(self, id_asignare, nota):
        """
        Functia seteaza nota pentru o asignare dintre un lab si un student
        :param id_asignare: int - identificatorul asignarii
               nota: int - nota
        :return: RepoError daca nu exista asignarea cu id_asignare
        """
        asignare = self.__repo_asignare.get_asignare_by_id(id_asignare)
        asignare.set_nota(nota)
        self.__repo_asignare.set_nota()

    def lista_laboratore_id(self, id_laborator):
        """
        Functia otbine o lista cu toate asignarile asociate unui laborator dat
        :param id_laborator: int - identificatorul laboratorului
        :return: lista de obiecte Asignare care au laboratorul specificat
        """
        lista_asignari = self.__repo_asignare.get_list()
        lista_asignari_valide = []
        for asignare in lista_asignari.values():
            if asignare.get_laborator().get_id() == id_laborator:
                lista_asignari_valide.append(asignare)
        return lista_asignari_valide

    def ordonare_laborator_nume(self, id_laborator):
        """
        Functia returneaza lista asignarilor pentru un laborator dat, ordonata alfabetic dupa numele studentului
        :param id_laborator: int - identificatorul laboratorului
        :return: lista de obiecte Asignare ordonata alfabetic dupa numele studentului
        """
        lista_asignari_valide = self.lista_laboratore_id(id_laborator)
        #lista_asignari_valide.sort(key=lambda asignare_sortare: asignare_sortare.get_student().get_nume())
        insertion_sort(lista_asignari_valide, key=lambda asignare_sortare: asignare_sortare.get_student().get_nume())
        return lista_asignari_valide

    def ordonare_laborator_nota(self, id_laborator):
        """
        Functia returneaza lista asignarilor pentru un laborator dat, ordonata descrescator dupa nota studentului
        :param id_laborator: int - identificatorul laboratorului
        :return: lista de obiecte Asignare care au o nota asignata, ordonata descrescator dupa nota
        """
        lista_asignari_valide = self.lista_laboratore_id(id_laborator)
        lista_asignari_valide = list(filter(lambda asignare: asignare.get_nota() is not None, lista_asignari_valide))
        #lista_asignari_valide.sort(key = lambda asignare_sortare: asignare_sortare.get_nota(), reverse = True)
        comb_sort(lista_asignari_valide, key = lambda asignare_sortare: asignare_sortare.get_nota(), reverse = True)
        return lista_asignari_valide

    def get_lista_note_in_functie_de_student(self):
        """
        Functia calculeaza suma notelor si numarul de note pentru fiecare student care are asignari notate
        :return: un dictionar unde cheia este id-ul studentului, iar valoarea este o lista [suma_notelor, numar_note]
        """

        asignari = self.__repo_asignare.get_list()
        asignari = dict(filter(lambda x: x[1].get_nota() is not None, asignari.items()))
        lista_note = {}
        for asignare in asignari.values():
            id_student = asignare.get_student().get_id()
            if id_student not in lista_note:
                lista_note[id_student] = [0, 0]
            lista_note[id_student][0] += asignare.get_nota()
            lista_note[id_student][1] += 1
        return lista_note

    def lista_medii_studenti(self):
        """
        Functia returneaza o lista de obiecte MedieDTO, fiecare reprezentand media notelor pentru un student
        :return: lista de obiecte MedieDTO, unde fiecare obiect contine numele studentului si media notelor sale
        """
        lista = self.get_lista_note_in_functie_de_student()
        obiecte = []
        for id_student in lista:
            nume_student = self.__repo_student.get_student_by_id(id_student).get_nume()
            medie = lista[id_student][0] / lista[id_student][1]
            medie_obiect = MedieDTO(nume_student, medie)
            obiecte.append(medie_obiect)
        return obiecte

    def get_lista_note_in_functie_de_laborator(self):
        """
        Functia calculeaza suma notelor si numarul de note pentru fiecare laborator care are asignari notate
        :return: un dictionar unde cheia este id-ul laboratorului, iar valoarea este o lista [suma_notelor, numar_note]
        """
        asignari = self.__repo_asignare.get_list()
        asignari = dict(filter(lambda x: x[1].get_nota() is not None, asignari.items()))
        lista_note = {}
        for asignare in asignari.values():
            id_laborator = asignare.get_laborator().get_id()
            if id_laborator not in lista_note:
                lista_note[id_laborator] = [0, 0]
            lista_note[id_laborator][0] += asignare.get_nota()
            lista_note[id_laborator][1] += 1
        return lista_note

    def lista_medii_laboratoare(self):
        """
        Functia returneaza o lista de obiecte MedieLaboratorDTO, fiecare reprezentand media notelor pentru un laborator
        :return: lista de obiecte MedieLaboratorDTO, unde fiecare obiect contine id-ul laboratorului si media notelor sale
        """

        lista = self.get_lista_note_in_functie_de_laborator()
        obiecte = []
        for id_laborator in lista:
            id_taiat = id_laborator.split("_")
            medie = lista[id_laborator][0] / lista[id_laborator][1]
            obiect = MedieLaboratorDTO(id_taiat[0], id_taiat[1], medie)
            obiecte.append(obiect)
        return obiecte

    def get_size(self):
        return self.__repo_asignare.get_size()

    def get_list(self):
        return self.__repo_asignare.get_list()