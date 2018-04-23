from Server import App,Response
from flask import jsonify, request

@App.route("/Alunos", methods=["GET"])
def ListarAlunos():
    from Services.ListarAlunos import ListarAlunos
    Response["Dados"] = ListarAlunos()
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = "Ok meu filho"

    return jsonify(Response)



@App.route("/Alunos/add", methods=["POST"])
def CadastrarAluno():
    from Services.CadastrarAluno import CadastrarAluno
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Status = Dados["Status"]

    Response["Dados"] = CadastrarAluno(Id,Nome,Status)
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = "Ok"

    return jsonify(Response)

@App.route("/Alunos/<Id>", methods = ["GET"])
def ConsultarAlunoPorId(Id):
    from Services.ConsultarPorId import ConsultarPorId
   
    Response["Status"] = "Sucesso"
    Response["Dados"] = ConsultarPorId(Id)
    Response["Mensagem"] = "Aluno encontrado!"
        
        

    return jsonify(Response)


@App.route("/Alunos/alter", methods=["PUT"])
def AlterarAluno():
    from Services.AlterarAluno import AlterarAluno
    
    Dados = request.get_json()

    Id = Dados["Id"]
    Nome = Dados["Nome"]

    Response["Dados"] = AlterarAluno(Id,Nome)
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = "Ok"

    return jsonify(Response)

@App.route("/Alunos/del/<Id>", methods = ["DELETE"])
def InativarAluno(Id):
    from Services.InativarAluno import InativarAluno
    InativarAluno(Id)

    Response["Status"] = "Sucesso"
    Response["Dados"] =  ""
    Response["Mensagem"] = "Aluno encontrado!"

    return jsonify(Response)