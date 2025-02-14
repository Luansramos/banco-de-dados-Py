from sqlalchemy import create_engine, Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#cria banco de dados ou conecta em um existente atravez do link direto
db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# tabelas

#banco de dados de um biblioteca:
#   tabela de usuarios

class Usuario(Base):
    __tablename__ = "usuarios" #da nome manualmente para a tabela, (boa pratica)
    
    id = Column("id", Integer, primary_key=True, autoincrement=True) # nome do campo , tipo primitivo
    nome = Column('nome',String)
    email = Column('email',String)
    senha = Column('senha',String)
    ativo = Column('ativo', Boolean)
    
    def __init__(self,nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
    
#    tabela de livros
class Livro(Base):
    
    __tablename__ = "Livros"
    
    id = Column('id',Integer,primary_key=True, autoincrement=True)
    titulo = Column('titulo',String)
    qtde_paginas = Column('qtde_paginas',Integer)
    dono = Column('dono', ForeignKey("usuarios.id") ) #ForeignKey = item de outra tabela 
    
    
    def __init__(self,  titulo, qtde_paginas, dono ):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

#       --->>--->>CRUD<<---<<---

#    --->>c - create <<---
'''
Usuario = Usuario(nome="lira2", email="luan2@email.com", senha= 123)
session.add(Usuario)
session.commit()


Livro = Livro(titulo='o fim',qtde_paginas=50, dono=usuario_lira.id) #add livro
session.add(Livro)
session.commit()
'''

#   --->> R - READ <<---
#lista_usuario = session.query(Usuario).all()
usuario_lira2 = session.query(Usuario).filter_by(email='luan2@email.com').first()

print(usuario_lira2)
print(usuario_lira2.email)
print(usuario_lira2.ativo)


#    --->> atulizar <<---
'''
usuario_lira2.id = 2 #variavel.nome = "atualizaçao"
session.add(usuario_lira2)
session.commit()
'''

#   --->> delete <<---

'''
session.delete(usuario_lira)
session.commit()
'''