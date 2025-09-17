from flask import Flask

app = Flask(__name__)


from .user import Usuaria
from .postagem import Postagem
from .postagem_removida import PostagemRemovida
from .denuncia import Denuncia
from .comentario import Comentario
from .avaliacao import Avaliacao