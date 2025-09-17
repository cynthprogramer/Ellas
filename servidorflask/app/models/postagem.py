from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from run import db
# from .user import Usuaria
from .comentario import Comentario
from .denuncia import Denuncia
from .avaliacao import Avaliacao
from .postagem_removida import PostagemRemovida

Base = declarative_base()
metadata = Base.metadata

class Postagem(db.Model):
    __tablename__ = 'postagem'
    __table_args__ = (
        ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaPostagem'),
        Index('data_postagem_UNIQUE', 'data_postagem', unique=True),
        Index('fk_idUsuaria_idx', 'id_usuaria'),
        Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True),
        Index('idpostagem_UNIQUE', 'idpostagem', unique=True)
    )

    idpostagem = mapped_column(Integer, primary_key=True, nullable=False)
    data_postagem = mapped_column(DateTime, nullable=False)
    titulo = mapped_column(String(40), nullable=False)
    texto = mapped_column(String(250), nullable=False)
    id_usuaria = mapped_column(Integer, primary_key=True, nullable=False)

    usuaria: Mapped['Usuaria'] = relationship('Usuaria', back_populates='postagem')
    # usuaria_: Mapped['Usuaria'] = relationship('Usuaria', secondary='postagem_curtida', back_populates='postagem_')
    comentario: Mapped[List['Comentario']] = relationship('Comentario', uselist=True, back_populates='postagem')
    denuncia: Mapped[List['Denuncia']] = relationship('Denuncia', uselist=True, back_populates='postagem')
    avaliacao: Mapped[List['Avaliacao']] = relationship('Avaliacao', uselist=True, back_populates='postagem')
    postagem_removida: Mapped[List['PostagemRemovida']] = relationship('PostagemRemovida', uselist=True, back_populates='postagem')


# t_postagem_curtida = Table(
#     'postagem_curtida', metadata,
#     Column('id_usuaria', Integer, primary_key=True, nullable=False),
#     Column('id_postagem', Integer, primary_key=True, nullable=False),
#     ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemCurtida'),
#     ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaPostagemCurtida'),
#     Index('fk_idPostagem_idx', 'id_postagem'),
#     Index('id_postagem_UNIQUE', 'id_postagem', unique=True),
#     Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True)
# )

