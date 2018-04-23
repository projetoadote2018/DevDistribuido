from Models.Alunos import Alunos


def AlterarAluno(Id,Nome):
    for Aluno in Alunos:
        if Aluno["Id"] == Id:
            Aluno["Nome"] = Nome
            return Aluno
   
    