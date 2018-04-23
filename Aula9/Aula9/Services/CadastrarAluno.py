from Server import Alunos


def CadastrarAluno(Id, Nome, Status):
    Aluno = {"Id":Id,"Nome":Nome, "Status": Status}
    Alunos.append(Aluno)
   
    return Aluno
