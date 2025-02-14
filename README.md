# 📚 Biblioteca - Projeto de Estudo Pessoal

Este projeto foi desenvolvido para fins de **estudo pessoal**, visando aprofundar conhecimentos em **Python** e **SQLAlchemy ORM** para manipulação de bancos de dados relacionais.

## 🚀 Tecnologias Utilizadas
- **Python**
- **SQLAlchemy** (ORM para bancos de dados relacionais)
- **SQLite** (Banco de dados leve e eficiente)

## 📌 Funcionalidades
✅ **Modelagem do Banco de Dados** com SQLAlchemy ORM  
✅ **Criação de tabelas** para usuários e livros  
✅ **Relacionamentos** entre tabelas utilizando ForeignKey  
✅ **Operações CRUD (Create, Read, Update, Delete)** para gerenciamento de usuários e livros  
✅ **Persistência de Dados** utilizando sessões e commits no banco SQLite  

## 🛠 Configuração e Execução

### 1️⃣ **Instalar as dependências**
Certifique-se de ter o Python instalado. Depois, instale o SQLAlchemy:
```bash
pip install sqlalchemy
```

### 2️⃣ **Executar o projeto**
Basta rodar o arquivo Python para criar as tabelas e testar as operações CRUD:
```bash
python main.py
```

## 📂 Estrutura do Projeto
```
📂 biblioteca
 ├── 📄 main.py  # Código principal com as operações CRUD
 ├── 📄 meubanco.db  # Banco de dados SQLite (gerado automaticamente)
 ├── 📄 README.md  # Documentação do projeto
```

## 📝 Como Usar
### Criar um novo usuário:
```python
usuario = Usuario(nome="João", email="joao@email.com", senha="1234")
session.add(usuario)
session.commit()
```

### Cadastrar um livro:
```python
livro = Livro(titulo='Python Avançado', qtde_paginas=350, dono=usuario.id)
session.add(livro)
session.commit()
```

### Consultar usuários:
```python
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nome, usuario.email)
```

### Atualizar dados de um usuário:
```python
usuario = session.query(Usuario).filter_by(email='joao@email.com').first()
usuario.nome = "João Silva"
session.commit()
```

### Deletar um usuário:
```python
session.delete(usuario)
session.commit()
```


