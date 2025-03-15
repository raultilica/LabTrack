from ui.interfata import Consola
from testare.teste import Teste
from repo.laborator import LaboratorRepo
from service.laborator import ServiceLaborator
from service.student import ServiceStudent
from domain.laborator_validator import ValidatorLaborator
from domain.student_validator import ValidatorStudent
from service.asignare import ServiceAsignare
from repo.student import RepoStudent
from repo.asignare import RepoAsignare
from domain.asignare_validator import ValidatorAsignare
from repo.student_file import RepoStudentFile
from repo.laborator_file import RepoLaboratorFile
from repo.asignare_file import RepoAsignareFile

#Teste().ruleaza_teste()

"""
#Repo
repo_student = RepoStudent()
repo_laborator = LaboratorRepo()
repo_asignare = RepoAsignare()
"""

#Repo fisiere
repo_student = RepoStudentFile("repo/studenti")
repo_laborator = RepoLaboratorFile("repo/laboratoare")
repo_asignare = RepoAsignareFile("repo/asignari")


vld_laborator = ValidatorLaborator()
vld_student = ValidatorStudent()
vld_asignare = ValidatorAsignare()

srv_laborator = ServiceLaborator(vld_laborator, repo_laborator)
srv_student = ServiceStudent(vld_student, repo_student)
srv_asignare = ServiceAsignare(repo_student, repo_laborator, repo_asignare, vld_asignare)


Consola(srv_student, srv_laborator, srv_asignare).run()

