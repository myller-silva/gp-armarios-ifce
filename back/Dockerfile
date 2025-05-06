# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo para o diretório de trabalho
COPY . .

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Exponha a porta em que o Flask será executado
EXPOSE 5000

# Comando padrão (se o ENTRYPOINT terminar com sucesso, esse comando é executado)
CMD ["flask", "run", "--host=0.0.0.0"]
