from domain.laborator_validator import ValidatorLaborator
from domain.student import Student
from domain.student_validator import ValidatorStudent
from repo.asignare import RepoAsignare
from repo.laborator import LaboratorRepo
from repo.student import RepoStudent
from repo.student_file import RepoStudentFile
from repo.laborator_file import RepoLaboratorFile
from repo.asignare_file import RepoAsignareFile
from service.asignare import ServiceAsignare
from service.laborator import ServiceLaborator
from service.student import ServiceStudent
from domain.laborator import Laborator
from domain.asignare import Asignare
from domain.asignare_validator import ValidatorAsignare
from datetime import datetime
import random
import unittest
from erori.erori import *

class Teste(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.student_validare = ValidatorStudent()
        cls.student_repo = RepoStudent()
        cls.student_serv = ServiceStudent(cls.student_validare, cls.student_repo)
        cls.laborator_validare = ValidatorLaborator()
        cls.laborator_repo = LaboratorRepo()
        cls.laborator_serv = ServiceLaborator(cls.laborator_validare, cls.laborator_repo)
        cls.validator_asignare = ValidatorAsignare()
        cls.asignare_repo = RepoAsignare()
        cls.asignare_serv = ServiceAsignare(cls.student_repo, cls.laborator_repo, cls.asignare_repo, cls.validator_asignare)

    def setUp(self):
        self.student_1 = Student(1, "Popescu I.", 217)
        self.student_2 = Student(2, "Iopescu I.", 912)
        self.student_modificare = Student(1, "Razvan Chiribuca", 123)
        self.student_invalid = Student(-1, "", -123)
        self.laborator_1 = Laborator("1_1", "laborator fermcat", datetime(2004, 12, 11))
        self.laborator_2 = Laborator("2_1", "laborator nefiresc", datetime(2004, 12, 11))
        self.laborator_invalid = Laborator("1_1", "", datetime(2004, 12, 12))
        self.asignare_1 = Asignare(1, self.student_1, self.laborator_1)
        self.asignare_2 = Asignare(2, self.student_2, self.laborator_2)

    """
    def pregatire(self):
        self.student_1 = Student(1, "Popescu I.", 217)
        self.student_2 = Student(2, "Iopescu I.", 912)
        self.student_modificare = Student(1, "Razvan Chiribuca", 123)
        self.student_invalid = Student(-1, "", -123)
        self.laborator_1 = Laborator("1_1", "laborator fermcat", datetime(2004, 12,11))
        self.laborator_2 = Laborator("2_1", "laborator nefiresc", datetime(2004, 12, 11))
        self.laborator_invalid = Laborator("1_1", "", datetime(2004, 12, 12))
        self.asignare_1 = Asignare(1, self.student_1, self.laborator_1)
        self.asignare_2 = Asignare(2, self.student_2, self.laborator_2)
    """

    def test_domeniu_student(self):
        #self.pregatire()
        assert self.student_1.get_id() == 1
        assert self.student_1.get_nume() == "Popescu I."
        assert self.student_1.get_grup() == 217
        self.student_1.set_nume("Popescu C.")
        self.student_1.set_grup(219)
        assert self.student_1.get_nume() == "Popescu C."
        assert self.student_1.get_grup() == 219
        #Teste student_validator
        try:
            self.student_validare.validate(self.student_1)
            assert True
        except ValidError:
            assert False
        try:
            self.student_validare.validate(self.student_invalid)
            assert False
        except ValidError:
            assert True

    def test_domeniu_laborator(self):
        #self.pregatire()
        #Teste Laborator
        assert self.laborator_1.get_id() == "1_1"
        assert self.laborator_1.get_descriere() == "laborator fermcat"
        assert self.laborator_1.get_deadline() == datetime(2004, 12, 11)
        self.laborator_1.set_descriere("laborator usor")
        self.laborator_1.set_deadline(datetime(2006, 6, 1))
        assert self.laborator_1.get_descriere() == "laborator usor"
        assert self.laborator_1.get_deadline() == datetime(2006, 6, 1)
        #Teste laborator_validator
        try:
            self.laborator_validare.validate(self.laborator_1)
            assert True
        except ValidError:
            assert False
        try:
            self.laborator_validare.validate(self.laborator_invalid)
            assert False
        except ValidError:
            assert True

    def test_domeniu_asignare(self):
        #self.pregatire()
        #Teste Asignare
        assert 1 == self.asignare_1.get_id()
        assert self.asignare_1.get_student().get_id() == self.student_1.get_id()
        assert self.asignare_1.get_laborator().get_descriere() == self.laborator_1.get_descriere()
        assert self.asignare_1.get_nota() is None
        self.asignare_1.set_nota(9.73)
        assert self.asignare_1.get_nota() == 9.73
        #Teste asignare_laborator
        try:
            self.validator_asignare.validate(self.asignare_1)
            assert True
        except ValidError:
            assert False

    def test_repo_student_file(self):
        repo = RepoStudentFile("teste_fisier")
        repo.clear_list()
        #self.pregatire()
        repo.adaugare(self.student_1)
        assert repo.size() == 1
        student_nou = Student(2, "Popescu Ionescu", 219)
        repo.modificare(1, student_nou)
        assert repo.size() == 1
        dictionar = repo.get_lista()
        assert dictionar[1].get_nume() == "Popescu Ionescu"
        repo.stergere(1)
        assert repo.size() == 0
        repo.clear_list()

    def test_repo_laborator_file(self):
        repo = RepoLaboratorFile("teste_fisier")
        repo.clear_list()
        #self.pregatire()
        repo.adaugare(self.laborator_1)
        assert repo.get_size() == 1
        repo.adaugare(self.laborator_2)
        assert repo.get_size() == 2
        dictionar = repo.get_lista_laboratoare()
        assert dictionar["2_1"].get_descriere() == "laborator nefiresc"
        repo.clear_list()

    def test_repo_asignare_file(self):
        repo = RepoAsignareFile("teste_fisier")
        repo.clear_list()
        assert repo.get_size() == 0
        repo.add(self.asignare_1)
        assert repo.get_size() == 1
        repo.delete_by_id(1)
        assert repo.get_size() == 0
        repo.clear_list()

    def test_repo_student(self):
        #self.pregatire()
        self.student_repo.clear_list()
        self.student_repo.adaugare(self.student_1)
        assert self.student_repo.size() == 1
        self.student_repo.adaugare(self.student_2)
        assert self.student_repo.size() == 2
        assert self.student_repo.get_student_by_id(1).get_nume() == "Popescu I."

    def test_repo_laborator(self):
        #self.pregatire()
        self.laborator_repo.clear_list()
        self.laborator_repo.adaugare(self.laborator_1)
        assert self.laborator_repo.get_size() == 1
        self.laborator_repo.adaugare(self.laborator_2)
        assert self.laborator_repo.get_size() == 2

    def test_repo_asignare(self):
        #self.pregatire()
        self.asignare_repo.clear_list()
        self.asignare_repo.add(self.asignare_1)
        assert self.asignare_repo.get_size() == 1
        assert self.asignare_1.get_id() == 1
        self.asignare_repo.add(self.asignare_2)
        assert self.asignare_repo.get_size() == 2
        assert self.asignare_repo.get_asignare_by_id(1).get_student().get_nume() == "Popescu I."

    def test_service_student_adaugare(self):
        #self.pregatire()
        self.student_repo.clear_list()
        self.student_serv.add(1, "Romascanu Petru", 219)
        self.student_serv.add(3, "Razvan Chiribuca", 231)
        self.student_serv.add(4, "Razvan Chiribuca", 912)
        self.student_serv.add(100, "Costel Nenea.", 930)
        assert self.student_serv.size() == 4
        assert self.student_serv.get_lista()[1].get_nume() == "Romascanu Petru"
        assert self.student_serv.get_lista()[100].get_grup() == 930
        try:
            self.student_serv.add(-1, "Ionescu P.", 100)
            assert False
        except ValidError:
            assert True
        try:
            self.student_serv.add(3, "", 910)
            assert False
        except ValidError:
            assert True
        try:
            self.student_serv.add(3, "Tudor C.", -123)
            assert False
        except ValidError:
            assert True
        try:
            self.student_serv.add(1, "Invalid ID", 734)
            assert False
        except RepoError:
            assert True
        assert self.student_serv.size() == 4

    def test_service_student_modificare(self):
        self.student_serv.actualizare(1, "Cozonac Petru", 713)
        assert self.student_serv.get_lista()[1].get_nume() == "Cozonac Petru"
        assert self.student_serv.get_lista()[3].get_nume() == "Razvan Chiribuca"
        self.student_serv.actualizare(3, "Razvan Chiribuca", 983)
        assert self.student_serv.get_lista()[3].get_nume() == "Razvan Chiribuca"
        try:
            self.student_serv.actualizare(5, "Alex B.", 100)
            assert False
        except RepoError:
            assert True
        try:
            self.student_serv.actualizare(5, "", 100)
            assert False
        except ValidError:
            assert True
        try:
            self.student_serv.actualizare(5, "Alex B.", -1)
            assert False
        except ValidError:
            assert True

    def test_service_student_cautare(self):
        lista_nevida = self.student_serv.cauta_student("Razvan Chiribuca")
        assert len(lista_nevida) == 2
        lista_vida = self.student_serv.cauta_student("Razvan Chiribuc")
        assert len(lista_vida) == 0
        lista_vida2 = self.student_serv.cauta_student("")
        assert len(lista_vida2) == 0

    def test_service_student_get_by_id(self):
        student = self.student_serv.get_student_by_id(1)
        assert student.get_id() == self.student_1.get_id()
        try:
            self.student_serv.get_student_by_id(-1)
            assert False
        except RepoError:
            assert True

    def test_service_student_generare_student(self):
        random.seed(2004)
        id_folosite = {1,3,4,100}
        student_random = self.student_serv.genereaza_student(5, id_folosite)
        assert student_random.get_nume() == "aFWfQBixgb"
        assert student_random.get_id() == 68
        assert student_random.get_grup() == 502
        self.student_serv.genereaza_studenti(3)
        assert self.student_serv.size() == 7
        assert self.student_serv.get_lista()[47].get_id() == 47
        assert self.student_serv.get_lista()[77].get_id() == 77

    """
    def ruleaza_teste_domeniu(self):
        self.testare_domeniu_student()
        self.testare_domeniu_laborator()
        self.testare_domeniu_asignare()
        print("Teste domeniu reusite!")

    def ruleaza_teste_repo(self):
        self.testare_repo_laborator()
        self.testare_repo_laborator_file()
        self.testare_repo_student()
        self.testare_repo_student_file()
        self.testare_repo_asignare()
        self.testare_repo_asignare_file()
        print("Teste repository reusite!")

    def ruleaza_teste_service(self):
        self.testare_service_student_adaugare()
        self.testare_service_student_modificare()
        self.testare_service_student_cautare()
        self.testare_service_student_get_by_id()
        self.testare_service_student_generare_student()
        print("Teste service reusite!")

    def ruleaza_teste(self):
        self.ruleaza_teste_domeniu()
        self.ruleaza_teste_repo()
        self.ruleaza_teste_service()
    """