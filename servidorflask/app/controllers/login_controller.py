from app.controllers.suap_controller import SuapController
import json

class LoginController:
    
    def login(formulario):
        matricula = formulario.matricula.data
        senha = formulario.senha.data
        resposta = json.loads(SuapController.login_suap(matricula, senha))
        return resposta