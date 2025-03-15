from datetime import datetime
from erori.erori import *

class Consola:
    def __init__(self, srv_student, srv_laborator, srv_asignare):
        self.__service_student = srv_student
        self.__service_laborator = srv_laborator
        self.__service_asignare = srv_asignare
        self.__lista_comenzi = {
            "adaugare": self.meniu_adaugare,
            "stergere": self.meniu_stergere,
            "modifica": self.meniu_modificare,
            "cautare": self.meniu_cautare,
            "afisare": self.meniu_afisare,
            "generare": self.meniu_generare,
            "filtrare": self.meniu_filtrare
        }
    @staticmethod
    def afiseaza_studenti(lista_studenti):
        if len(lista_studenti) == 0:
            print("nu exista studenti")
        else:
            for student in lista_studenti.values():
                print(f"ID: {student.get_id():<5} Nume: {student.get_nume():<15} Grup: {student.get_grup():}")

    @staticmethod
    def afiseaza_laboratoare(lista_laboratoare):
        if len(lista_laboratoare) == 0:
            print("nu exista laboratoare adaugate")
        else:
            for laborator in lista_laboratoare.values():
                print(f"ID: {laborator.get_id():<10} Descriere: {laborator.get_descriere():<15} Deadline: {laborator.get_deadline().strftime('%d/%m/%Y')}")

    def afisare_asignari(self):
        lista_asignari = self.__service_asignare.get_list()
        if len(lista_asignari) == 0:
            print("nu exista asignari")
        else:
            for asignare in lista_asignari.values():
                print(f"ID asignare: {asignare.get_id()}, Nume student: {asignare.get_student().get_nume()},  laborator: {asignare.get_laborator().get_id()}, nota: {asignare.get_nota()}")

    @staticmethod
    def afisare_filtrare(lista):
        if len(lista) == 0:
            print("nu exista asignari care se corespunda datelor introduse")
        else:
            for asignare in lista:
                print(f"ID Asignare: {asignare.get_id()}, Nume Student: {asignare.get_student().get_nume()}, Nota: {asignare.get_nota()}")

    @staticmethod
    def afisare_mediisub5_studenti(lista):
        if len(lista) == 0:
            print("nu exista studenti cu medii sub 5 la laboratoare")
        else:
            for medieDTO in lista:
                if medieDTO.get_medie() < 5:
                    print(f"Nume student: {medieDTO.get_nume()}, Medie laboratoare: {medieDTO.get_medie()}")
    @staticmethod
    def afisare_mediisub5labs(lista):
        if len(lista) == 0:
            print("nu exista laboratoare pentru care media e sub 5")
        else:
            for medieDTO in lista:
                if medieDTO.get_medie() < 5:
                    print(f"Numar Laborator: {medieDTO.get_numar_laborator()}, Numar Problema: {medieDTO.get_numar_problema()}, Medie: {medieDTO.get_medie()}")

    def afisare_studenti_full_list(self):
        lista_studenti = self.__service_student.get_lista()
        self.afiseaza_studenti(lista_studenti)

    def afisare_laboratoare_full_list(self):
        lista_laboratoare = self.__service_laborator.get_lista()
        self.afiseaza_laboratoare(lista_laboratoare)

    def adauga_student(self):
        id_stud = input("id student:\n>>>")
        id_stud = int(id_stud)
        nume_student = input("nume student:\n>>>")
        grup_student = input("grup student:\n>>>")
        grup_student= int(grup_student)
        self.__service_student.add(id_stud, nume_student, grup_student)
        print("Operatie reusita!")

    def adauga_laborator(self):
        numar_laborator = int(input("numar laborator:\n>>>"))
        numar_problema = int(input("numar problema:\n>>>"))
        descriere = input("descrierea problemei:\n>>>")
        deadline = input("termen de predare, format D/MM/YYYY:\n>>>")
        deadline = datetime.strptime(deadline, "%d/%m/%Y")
        self.__service_laborator.add(f"{numar_laborator}_{numar_problema}", descriere, deadline)
        print("Operatie reusita!")

    def adauga_asignare(self):
        id_asignare = int(input("introdu un id de asignare, numar\n>>>"))
        self.afisare_studenti_full_list()
        if self.__service_student.size() == 0:
            return
        id_student = int(input("selecteaza un id valid\n>>>"))
        self.afisare_laboratoare_full_list()
        if self.__service_laborator.get_size() == 0:
             return
        id_laborator = input("selecteaza un id valid\n>>>")
        int(id_laborator)
        self.__service_asignare.add(id_asignare, id_student, id_laborator)
        print("Operatie reusita!")

    def adaugare_nota(self):
        self.afisare_asignari()
        if self.__service_asignare.get_size() == 0:
            return
        id_asignare = int(input("Introdu un id valid\n>>>"))
        nota = float(input("Introdu o nota valid\n>>>"))
        self.__service_asignare.noteaza(id_asignare, nota)
        print("Operatie reusita!")

    def stergere_student(self):
        self.afisare_studenti_full_list()
        if self.__service_student.size() == 0:
            return
        id_student = int(input("selecteaza un id\n>>>"))
        self.__service_asignare.delete_by_student_id(id_student)
        print("Operatie reusita!")

    def stergere_laborator(self):
        self.afisare_laboratoare_full_list()
        if self.__service_laborator.get_size() == 0:
            return
        id_lab = input("introdu un id\n>>>")
        int(id_lab)
        self.__service_asignare.delete_by_lab_id(id_lab)
        print("Operatie reusita!")

    def modificare_student(self):
        self.afisare_studenti_full_list()
        if self.__service_student.size() == 0:
            return
        id_student = input("introdu un id\n>>>")
        id_student = int(id_student)
        nume_student = input("nume student:\n>>>")
        grup_student = input("grup student:\n>>>")
        grup_student = int(grup_student)
        self.__service_student.actualizare(id_student, nume_student, grup_student)
        print("Operatie reusita!")

    def modificare_laborator(self):
        self.afisare_laboratoare_full_list()
        if self.__service_laborator.get_size() == 0:
            return
        id_lab = input("introdu un id de laborator\n>>>>")
        int(id_lab)
        descriere = input("introdu descrierea\n>>>")
        data = input("introdu data, format DD/MM/YYYY\n>>>")
        data = datetime.strptime(data, "%d/%m/%Y")
        self.__service_laborator.modificare(id_lab, descriere, data)
        print("Operatie reusita!")

    def cautare_student(self):
        nume_student = input("introdu numele studentului\n>>>")
        lista_studenti = self.__service_student.cauta_student(nume_student)
        self.afiseaza_studenti(lista_studenti)

    def cautare_laborator(self):
        data = input("introdu data, format 'DD/MM/YYYY'\n>>>")
        data = datetime.strptime(data, "%d/%m/%Y")
        lista_laboratoare = self.__service_laborator.cauta_dupa_data(data)
        self.afiseaza_laboratoare(lista_laboratoare)

    def generare_studenti(self):
        numar_studenti = int(input("introdu un numar de studenti de generat\n>>>"))
        self.__service_student.genereaza_studenti(numar_studenti)
        print("Operatie reusita!")

    def generare_laboratoare(self):
        numar_laboratoare = int(input("introdu un numar de laboratoare de generat\n>>>"))
        self.__service_laborator.genereaza_laboratoare(numar_laboratoare)
        print("Operatie reusita!")

    def ordonare_laborator_nume(self):
        self.afisare_laboratoare_full_list()
        if self.__service_laborator.get_size() == 0:
            return
        id_laborator = input("introdu un id de laborator\n>>>")
        int(id_laborator)
        lista = self.__service_asignare.ordonare_laborator_nume(id_laborator)
        self.afisare_filtrare(lista)

    def ordonare_laborator_nota(self):
        self.afisare_laboratoare_full_list()
        if self.__service_laborator.get_size() == 0:
            return
        id_laborator = input("introdu un id de laborator\n>>>")
        int(id_laborator)
        lista = self.__service_asignare.ordonare_laborator_nota(id_laborator)
        self.afisare_filtrare(lista)

    def statistica_sub5_studenti(self):
        lista = self.__service_asignare.lista_medii_studenti()
        self.afisare_mediisub5_studenti(lista)

    def statistica_sub5_laboratoare(self):
        lista = self.__service_asignare.lista_medii_laboratoare()
        self.afisare_mediisub5labs(lista)

    def meniu_adaugare(self):
        print("'adauga_student', pentru a adauga un nou student")
        print("'adauga_laborator', pentru a adauga un nou laborator")
        print("'adauga_asignare', pentru a asigna un laborator unui student")
        print("'adaugare_nota', pentru a nota un laborator asignat")
        optiune = input('>>>').strip().lower()
        if optiune == 'adauga_student':
            self.adauga_student()
        elif optiune == 'adauga_laborator':
            self.adauga_laborator()
        elif optiune == 'adauga_asignare':
            self.adauga_asignare()
        elif optiune == 'adaugare_nota':
            self.adaugare_nota()
        else:
            print("comanda invalida")

    def meniu_stergere(self):
        print("'stergere_student', pentru a sterge un student dupa id")
        print("'stergere_laborator', pentru a sterge o tema de laborator dupa id")
        optiune = input('>>>').strip().lower()
        if optiune == "stergere_student":
            self.stergere_student()
        elif optiune == "stergere_laborator":
            self.stergere_laborator()
        else:
            print("comanda invalida")

    def meniu_modificare(self):
        print("'modificare_student', pentru a modifica un student")
        print("'modificare_laborator', pentru a modifica un laborator")
        optiune = input('>>>').strip().lower()
        if optiune == "modificare_student":
            self.modificare_student()
        elif optiune == 'modificare_laborator':
            self.modificare_laborator()
        else:
            print("comanda invalida")

    def meniu_cautare(self):
        print("'cautare_student'   - pentru a cauta un student in functie de nume")
        print("'cautare_laborator' - pentru a cauta un laborator in functie de deadline")
        optiune = input(">>>").strip().lower()
        if optiune == "cautare_student":
            self.cautare_student()
        elif optiune == "cautare_laborator":
            self.cautare_laborator()
        else:
            print("comanda invalida")

    def meniu_afisare(self):
        print("'afisare_studenti'    - pentru a afisa lista de studenti")
        print("'afisare_laboratoare' - pentru a afisa lista de laboratoare")
        print("'afisare_asignari'     - pentru a afisa lista de asignari")
        comenzi = {
            "afisare_studenti": self.afisare_studenti_full_list,
            "afisare_laboratoare": self.afisare_laboratoare_full_list,
            "afisare_asignari": self.afisare_asignari
        }
        optiune = input(">>>")
        if optiune in comenzi:
            comenzi[optiune]()
        else:
            print("comanda invalida")

    def meniu_generare(self):
        print("'generare_studenti'    - pentru a genera random studenti")
        print("'generare_laboratoare' - pentru a genera random laboratoare")
        optiune = input("introdu optiunea\n>>>").strip().lower()
        if optiune == "generare_studenti":
            self.generare_studenti()
        elif optiune == "generare_laboratoare":
            self.generare_laboratoare()
        else:
            print("optiune invalida")

    def meniu_filtrare(self):
        print("'ordonare_laborator_nume'          - pentru a ordona lista de studenti in functie de numele acestora, in functie de un laborator dat")
        print("'ordonare_laborator_nota'          - pentru a ordona lista de studenti in functie de notele acestora la un anumit laborator dat")
        print("'statistica_sub5_studenti'         - pentru a afisa studentii cu medii la laboratoare sub 5")
        print("'statistica_sub5_laboratoare'      - pentru a afisa laboratoarele la care media e sub 5")
        optiune = input("introdu optiunea\n>>>").strip().lower()
        if optiune == "ordonare_laborator_nume":
            self.ordonare_laborator_nume()
        elif optiune == "ordonare_laborator_nota":
            self.ordonare_laborator_nota()
        elif optiune == "statistica_sub5_studenti":
            self.statistica_sub5_studenti()
        elif optiune == "statistica_sub5_laboratoare":
            self.statistica_sub5_laboratoare()
        else:
            print("comanda invalida")

    def run(self):
        while True:
            print("'adaugare'   - optiuni de adaugare")
            print("'stergere'   - optiuni de stergere")
            print("'modifica'   - optiuni de modificare")
            print("'cautare'    - optiuni de cautare")
            print("'afisare'    - optiuni de afisare")
            print("'generare'   - optiuni de generare")
            print("'filtrare'   - optiuni de filtrare")
            print("'populare    - introduce studenti si laboratoare valide")
            print("'exit'     - termina programul")
            optiune = input(">>>")
            optiune = optiune.lower()
            if optiune in self.__lista_comenzi:
                try:
                    self.__lista_comenzi[optiune]()
                except ValueError:
                    print(f"Eroare de conversie: datele introduse nu pot fi convertite la tipul necesar")
                except DomainError as de:
                    print(f"Eroare de domeniu: {de}")
                except RepoError as re:
                    print(f"Eroare de repository: {re}")
                except ValidError as vde:
                    print(f"Eroare de validare: \n{vde}")
                except ServiceError as se:
                    print(f"Eroare de service: {se}")
            elif optiune == 'populare':
                try:
                    self.__service_student.populare_students()
                    self.__service_laborator.populare_laboratoare()
                    print("reusit")
                except ValueError:
                    print("deja populat cu aceste valori")
            elif optiune == 'exit':
                return
            else:
                print("comanda invalida")


