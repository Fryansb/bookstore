# Imagem base - Python slim (versão enxuta)
FROM python:3.12-slim

# Definindo variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Definindo diretório de trabalho da aplicação
WORKDIR /app

# Copiando todos os arquivos do projeto
COPY . .

# Instalando dependências do projeto
RUN pip install --upgrade pip && \
    pip install django djangorestframework pytest factory-boy

# Expondo a porta 8000
EXPOSE 8000

# Comando para executar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
