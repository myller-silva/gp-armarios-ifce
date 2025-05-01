# 📦 GP-Armários IFCE

Sistema web desenvolvido com Flask como parte da disciplina de Gestão de Projetos no Instituto Federal do Ceará (IFCE). 
O objetivo do projeto é simplificar a gestão e o controle do uso dos armários disponibilizados para os estudantes da instituição.

## 🚀 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## 📁 Estrutura do Projeto

```
gp-armarios-ifce/
├── back/
│   ├── app/                # Aplicação Flask
│   │   ├── __init__.py     # Inicialização da aplicação
│   │   ├── models.py       # Modelos do banco de dados
│   │   ├── routes.py       # Rotas e lógica de negócio
│   │   ├── templates/      # Templates HTML com Jinja2
│   │   └── static/         # Arquivos estáticos (CSS, JS, imagens)
│   ├── config.py           # Configurações da aplicação
│   ├── wsgi.py             # Ponto de entrada WSGI
│   ├── requirements.txt    # Dependências do projeto
├── docker-compose.yml      # Configuração do Docker Compose
└── README.md
```

## ⚙️ Instalação e Execução

### Clonando o Repositório

```bash
git clone https://github.com/myller-silva/gp-armarios-ifce.git
cd gp-armarios-ifce/back
```

### Criando Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

### Configuração do Banco de Dados

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Executando a Aplicação

```bash
flask run
```

A aplicação estará disponível em `http://localhost:5000`.

## 📫 Contato

Em caso de dúvidas ou sugestões, entre em contato pelo e-mail: **myller.silva@example.com**
