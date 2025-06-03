from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
#from .avaliacao import Avaliacao
#from .user import Usuaria
#from .postagem import Postagem


Base = declarative_base()
metadata = Base.metadata

class PostagemRemovida(db.Model):
    __tablename__ = 'postagem_removida'
    __table_args__ = (
        ForeignKeyConstraint(['id_avaliacao'], ['avaliacao.id_avaliacao'], name='fk_idAvaliacaoRemove'),
        ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemRemovida'),
        ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaPostagemRemovida'),
        Index('fk_idPostagem_idx', 'id_postagem'),
        Index('fk_idUsuaria_idx', 'id_usuaria'),
        Index('id_avaliacao_UNIQUE', 'id_avaliacao', unique=True),
        Index('id_postagem_UNIQUE', 'id_postagem', unique=True),
        Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True)
    )

    justificativa = mapped_column(String(250), nullable=False)
    id_usuaria = mapped_column(Integer, primary_key=True, nullable=False)
    id_postagem = mapped_column(Integer, primary_key=True, nullable=False)
    id_avaliacao = mapped_column(Integer, primary_key=True, nullable=False)

    avaliacao: Mapped['Avaliacao'] = relationship('Avaliacao', back_populates='postagem_removida')
    postagem: Mapped['Postagem'] = relationship('Postagem', back_populates='postagem_removida')
    usuaria: Mapped['Usuaria'] = relationship('Usuaria', back_populates='postagem_removida')
