from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
from .postagem import Postagem
from .comentario import Comentario
from .denuncia import Denuncia
from .avaliacao import Avaliacao
from .postagem_removida import PostagemRemovida

class Usuaria(db.Model):
    __tablename__ = 'usuaria'
    __table_args__ = (
        Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True),
        Index('username_UNIQUE', 'username', unique=True)
    )

    id_usuaria = mapped_column(Integer, primary_key=True)
    matricula = mapped_column(Integer, nullable=False)
    username = mapped_column(String(15), nullable=False)
    descricao = mapped_column(String(250), nullable=False)
    role = mapped_column(MEDIUMTEXT, nullable=False)

    postagem: Mapped[List['Postagem']] = relationship('Postagem', uselist=True, back_populates='usuaria')
    # postagem_: Mapped['Postagem'] = relationship('Postagem', secondary='postagem_curtida', back_populates='usuaria_')
    comentario: Mapped[List['Comentario']] = relationship('Comentario', uselist=True, back_populates='usuaria')
    denuncia: Mapped[List['Denuncia']] = relationship('Denuncia', uselist=True, back_populates='usuaria')
    avaliacao: Mapped[List['Avaliacao']] = relationship('Avaliacao', uselist=True, back_populates='usuaria')
    postagem_removida: Mapped[List['PostagemRemovida']] = relationship('PostagemRemovida', uselist=True, back_populates='usuaria')

    