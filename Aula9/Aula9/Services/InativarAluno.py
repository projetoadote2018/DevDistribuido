from Models.Alunos import Alunos


def InativarAluno(Id):
    for Aluno in Alunos:
        if Aluno["Id"] == Id:
            Aluno["Status"] = "Inativo"
            return Aluno
   