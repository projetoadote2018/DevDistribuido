from Server import Alunos


def ConsultarPorId(Id):
    for Aluno in Alunos:
        if Aluno["Id"] == Id:
            return Aluno