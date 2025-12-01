from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)


with app.app_context():
    from app.models.user import Usuaria
    from app.models.postagem import Postagem
    from app.models.postagem_removida import PostagemRemovida
    from app.models.denuncia import Denuncia
    from app.models.comentario import Comentario
    from app.models.avaliacao import Avaliacao

    db.create_all()