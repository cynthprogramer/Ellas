from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
#importando as classes 
#from .user import Usuaria
#from .postagem import Postagem
#from .comentario import Comentario
#from .avaliacao import Avaliacao


Base = declarative_base()
metadata = Base.metadata


class Denuncia(db.Model):
    __tablename__ = 'denuncia'
    __table_args__ = (
        ForeignKeyConstraint(['id_comentario'], ['comentario.id_comentario'], name='fk_idComentarioDenunciado'),
        ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemDenunciada'),
        ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaDenuncia'),
        Index('fk_idComentarioDenunciado_idx', 'id_comentario'),
        Index('fk_idUsuariaDenuncia_idx', 'id_usuaria'),
        Index('id_denuncia_UNIQUE', 'id_denuncia', unique=True),
        Index('id_postagem_UNIQUE', 'id_postagem', unique=True)
    )

    id_denuncia = mapped_column(Integer, primary_key=True, nullable=False)
    id_postagem = mapped_column(Integer, primary_key=True, nullable=False)
    id_usuaria = mapped_column(Integer, primary_key=True, nullable=False)
    id_comentario = mapped_column(Integer, primary_key=True, nullable=False)
    titulo_denuncia = mapped_column(String(50))
    texto_denuncia = mapped_column(String(250))

    comentario: Mapped['Comentario'] = relationship('Comentario', back_populates='denuncia')
    postagem: Mapped['Postagem'] = relationship('Postagem', back_populates='denuncia')
    usuaria: Mapped['Usuaria'] = relationship('Usuaria', back_populates='denuncia')
    avaliacao: Mapped[List['Avaliacao']] = relationship('Avaliacao', uselist=True, back_populates='denuncia')
