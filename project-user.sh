#!/bin/bash

# Verifica se foi passado um argumento
if [ $# -eq 0 ]; then
    echo "Uso: $0 nome_projeto"
    exit 1
fi

# Argumento é o nome do projeto
nome_projeto=$1

# Cria a pasta com o nome do projeto
mkdir $nome_projeto

# Copia os arquivos para a pasta do projeto
cp -r /home/rpereira/Projects/FastApi/fast_base_login/* $nome_projeto

# Entra na pasta do projeto
cd $nome_projeto

# Entra dentro da pasta copiada app
cd app

# Executa os comandos dentro da pasta do projeto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Imprime a mensagem no console
echo -e "\n\n Projeto criado, por favor alterar no arquivo app.py na linha 21 o nome do banco de dados do mongo."
