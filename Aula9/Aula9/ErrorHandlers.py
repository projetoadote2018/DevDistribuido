from flask import jsonify
from Server import App, Response



@App.errorhandler(500)
def TratarInternalServerError(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Temos um problema"
    Response["Dados"] = "Detalhe do erro: {0}".format(error)

    return jsonify(Response)

@App.errorhandler(404)
def TratarNotFound(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Ação não encontrada."
    Response["Dados"] = "Detalhe do erro: {0}".format(error)

    return jsonify(Response)

@App.errorhandler(400)
def TratarNotFound(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Requisição invalida."
    Response["Dados"] = "Detalhe do erro: {0}".format(error)

    return jsonify(Response)

@App.errorhandler(403)
def TratarNotFound(error):
    Response["Status"] = "Erro"
    Response["Mensagem"] = "Acesso Proibido."
    Response["Dados"] = "Detalhe do erro: {0}".format(error)

    return jsonify(Response)