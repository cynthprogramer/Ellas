from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
# from .postagem import Postagem
# from .user import Usuaria
# from .denuncia import Denuncia


Base = declarative_base()
metadata = Base.metadata


class Comentario(db.Model):
    __tablename__ = 'comentario'
    __table_args__ = (
        ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemComentario'),
        ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaComentario'),
        Index('id_comentario_UNIQUE', 'id_comentario', unique=True),
        Index('id_postagem_UNIQUE', 'id_postagem', unique=True),
        Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True)
    )

    id_comentario = mapped_column(Integer, primary_key=True, nullable=False)
    id_usuaria = mapped_column(Integer, primary_key=True, nullable=False)
    id_postagem = mapped_column(Integer, primary_key=True, nullable=False)
    texto_comentario = mapped_column(String(250))

    postagem: Mapped['Postagem'] = relationship('Postagem', back_populates='comentario')
    usuaria: Mapped['Usuaria'] = relationship('Usuaria', back_populates='comentario')
    denuncia: Mapped[List['Denuncia']] = relationship('Denuncia', uselist=True, back_populates='comentario')



