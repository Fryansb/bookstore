FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
FROM python:3.8-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Cria diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências do projeto
RUN poetry install --no-interaction --no-ansi

# Comando padrão para iniciar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]# Dockerfile inicial para o projeto Bookstore
FROM python:3.8-slim

WORKDIR /app

FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY . .

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install --no-root

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
