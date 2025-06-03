from typing import List

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, String, Table
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class Usuaria(Base): #substituir para db.model 
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
    postagem_: Mapped['Postagem'] = relationship('Postagem', secondary='postagem_curtida', back_populates='usuaria_')
    comentario: Mapped[List['Comentario']] = relationship('Comentario', uselist=True, back_populates='usuaria')
    denuncia: Mapped[List['Denuncia']] = relationship('Denuncia', uselist=True, back_populates='usuaria')
    avaliacao: Mapped[List['Avaliacao']] = relationship('Avaliacao', uselist=True, back_populates='usuaria')
    postagem_removida: Mapped[List['PostagemRemovida']] = relationship('PostagemRemovida', uselist=True, back_populates='usuaria')


class Postagem(Base):
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
    usuaria_: Mapped['Usuaria'] = relationship('Usuaria', secondary='postagem_curtida', back_populates='postagem_')
    comentario: Mapped[List['Comentario']] = relationship('Comentario', uselist=True, back_populates='postagem')
    denuncia: Mapped[List['Denuncia']] = relationship('Denuncia', uselist=True, back_populates='postagem')
    avaliacao: Mapped[List['Avaliacao']] = relationship('Avaliacao', uselist=True, back_populates='postagem')
    postagem_removida: Mapped[List['PostagemRemovida']] = relationship('PostagemRemovida', uselist=True, back_populates='postagem')


class Comentario(Base):
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


t_postagem_curtida = Table(
    'postagem_curtida', metadata,
    Column('id_usuaria', Integer, primary_key=True, nullable=False),
    Column('id_postagem', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['id_postagem'], ['postagem.idpostagem'], name='fk_idPostagemCurtida'),
    ForeignKeyConstraint(['id_usuaria'], ['usuaria.id_usuaria'], name='fk_idUsuariaPostagemCurtida'),
    Index('fk_idPostagem_idx', 'id_postagem'),
    Index('id_postagem_UNIQUE', 'id_postagem', unique=True),
    Index('id_usuaria_UNIQUE', 'id_usuaria', unique=True)
)


class Denuncia(Base):
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


class Avaliacao(Base):
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


class PostagemRemovida(Base):
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
