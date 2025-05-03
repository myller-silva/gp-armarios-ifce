#!/bin/bash

# echo "Ativando ambiente virtual..."
# source venv/bin/activate

echo "Inicializando diretório de migração (caso ainda não exista)..."
flask db init

echo "Criando migração..."
flask db migrate -m "Initial migration"

echo "Aplicando migração ao banco de dados..."
flask db upgrade

echo "Banco de dados pronto!"
