from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
#from .user import Usuaria
#from .denuncia import Denuncia
#from .postagem_removida import PostagemRemovida
#from .postagem import Postagem

Base = declarative_base()
metadata = Base.metadata


class Avaliacao(db.Model):
    __tablename__ = 'avaliacao'
    __table_args__ = (
        ForeignKeyConstraint(['id_denuncia'], ['denuncia.id_denuncia'], name='fk_idDenuncia'),
        ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemAvaliacao'),
        ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaAvaliacao'),
        Index('fk_idDenuncia_idx', 'id_denuncia'),
        Index('fk_idPostagem_idx', 'id_postagem'),
        Index('fk_idUsuariaAvaliacao_idx', 'id_usuaria'),
        Index('id_avaliacao_UNIQUE', 'id_avaliacao', unique=True),
        Index('id_postagem_UNIQUE', 'id_postagem', unique=True)
    )

    id_avaliacao = mapped_column(Integer, primary_key=True, nullable=False)
    id_postagem = mapped_column(Integer, primary_key=True, nullable=False)
    id_usuaria = mapped_column(Integer, primary_key=True, nullable=False)
    id_denuncia = mapped_column(Integer, primary_key=True, nullable=False)
    texto_avaliacao = mapped_column(String(250))

    denuncia: Mapped['Denuncia'] = relationship('Denuncia', back_populates='avaliacao')
    postagem: Mapped['Postagem'] = relationship('Postagem', back_populates='avaliacao')
    usuaria: Mapped['Usuaria'] = relationship('Usuaria', back_populates='avaliacao')
    postagem_removida: Mapped[List['PostagemRemovida']] = relationship('PostagemRemovida', uselist=True, back_populates='avaliacao')

