from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route("/")
def home():
    u = models.Usuaria(username='john', matricula='98998', descricao='blala', role='admin')
    db.session.add(u)
    db.session.commit()
    return "pagina inicial"


from app import models


#crie o banquinho no mysql
# with app.app_context() as ctx:
#     db.create_all()