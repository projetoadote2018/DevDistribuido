from flask import Flask

App = Flask(__name__)
#Dados
from Models.Alunos import Alunos 
from Models.Response import Response

#Servidor
from Routes import *
from ErrorHandlers import *





if __name__ == "__main__":
    App.run(port=80)