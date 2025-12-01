import requests
import json


class SuapController:
    
    def login_suap(matricula, senha):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        
        json_data = {
            'password': senha,
            'username': matricula,
        }
        response = requests.post('https://suap.ifrn.edu.br/api/token/pair', headers=headers, json=json_data)

        dados = json.loads(response.text)
        access = dados['access']
        refresh = dados['refresh']

        headers = {
            'Accept': 'application/json',
            'Authorization': "Bearer {0}".format(access),
            'X-CSRFToken': access
        }

        response = requests.get('https://suap.ifrn.edu.br/api/eu/', headers=headers)
        return response.text