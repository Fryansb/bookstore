FROM python:3.12-slim

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

# Copia arquivos de dependências
COPY pyproject.toml poetry.lock ./

# Instala dependências do projeto
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia código do projeto
COPY . .

# Comando padrão para iniciar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
