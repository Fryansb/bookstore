# Bookstore API

Projeto Django REST Framework desenvolvido durante o curso Backend Python da EBAC.

## 📚 Descrição

API REST para gerenciamento de uma livraria (bookstore), construída com Django e Django REST Framework.

## 🚀 Tecnologias

- Python 3.12+
- Django 6.0.1
- Django REST Framework 3.16.1
- Poetry (gerenciador de dependências)
- pytest (testes)
- factory-boy (fixtures para testes)
- Docker & Docker Compose
- PostgreSQL (produção)
- Heroku (deployment)
- GitHub Actions (CI/CD)

## 📦 Instalação

### Pré-requisitos
- Python 3.12 ou superior
- Poetry instalado globalmente

### Setup do projeto

```bash
# Clone o repositório
git clone https://github.com/Fryansb/bookstore.git
cd bookstore

# Instale as dependências com Poetry
poetry install

# Execute as migrações
poetry run python manage.py migrate

# Inicie o servidor de desenvolvimento
poetry run python manage.py runserver
```

## 🧪 Executar Testes

```bash
poetry run pytest
```

## 📂 Estrutura do Projeto

```
bookstore/
├── api/                    # App principal da API
├── bookstore/              # Configurações do projeto Django
│   ├── settings.py        # Configurações (inclui rest_framework)
│   ├── urls.py
│   └── wsgi.py
├── manage.py              # Utilitário Django
├── pyproject.toml         # Dependências do Poetry
└── poetry.lock            # Lock file do Poetry
```

## ⚙️ Configuração

O projeto está configurado com:
- Django REST Framework habilitado em `INSTALLED_APPS`
- SQLite como banco de dados (desenvolvimento)
- Debug mode ativado (apenas desenvolvimento)

## 📝 Exercício EBAC

Este projeto foi desenvolvido seguindo as aulas do módulo REST API:

**Aulas implementadas:**
- ✅ Aula 1-3: Conceitos de REST API, HTTP, JSON
- ✅ Aula 4: Setup com Poetry e Black
- ✅ Aula 5: Inicialização do projeto Django
- ✅ Aula 6: Criação do app e migrações
- ✅ Docker e Docker Compose
- ✅ CI/CD com GitHub Actions
- ✅ Deployment no Heroku

**Exercício:**
- ✅ Django REST Framework adicionado via `poetry add djangorestframework`
- ✅ `poetry.lock` atualizado com `poetry update`
- ✅ `rest_framework` adicionado ao `INSTALLED_APPS`
- ✅ Projeto testado e funcional
- ✅ Pipeline CI/CD configurada
- ✅ Deploy automático no Heroku

## 🌐 Deploy no Heroku

### Pré-requisitos
- Conta no Heroku
- Heroku CLI instalado
- GitHub Actions Secrets configurados:
  - `HEROKU_API_KEY`: Token de API do Heroku
  - `HEROKU_APP_NAME`: Nome da aplicação no Heroku
  - `HEROKU_EMAIL`: Email da conta Heroku

### Variáveis de Ambiente no Heroku

Configure as seguintes variáveis no Heroku:

```bash
# Secret Key do Django
heroku config:set SECRET_KEY="sua-secret-key-aqui" -a seu-app-name

# Configurações do PostgreSQL (criadas automaticamente ao adicionar o Postgres)
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=nome_do_database
SQL_USER=usuario
SQL_PASSWORD=senha
SQL_HOST=host_do_postgres
SQL_PORT=5432
```

### Deploy Manual

```bash
# Login no Heroku
heroku login

# Criar aplicação (se ainda não existir)
heroku create seu-app-name

# Configurar stack para container
heroku stack:set container -a seu-app-name

# Adicionar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev -a seu-app-name

# Adicionar remote do Heroku
heroku git:remote -a seu-app-name

# Deploy
git push heroku main:main

# Executar migrações
heroku run python manage.py migrate -a seu-app-name

# Criar superuser
heroku run python manage.py createsuperuser -a seu-app-name
```

### Deploy Automático via GitHub Actions

O deploy automático é executado sempre que há push na branch `main`. O workflow:

1. Executa build e testes
2. Faz code review
3. Deploy no Heroku (apenas na branch main)

Para configurar:
1. Adicione os secrets no GitHub: Settings > Secrets > Actions
2. Todo merge na main irá disparar o deploy automaticamente

## 🔗 Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)

## 👤 Autor

**Fryansb**
- GitHub: [@Fryansb](https://github.com/Fryansb)

## 📄 Licença

Projeto educacional desenvolvido para o curso Backend Python - EBAC.

---

**Curso:** Backend Python - EBAC  
**Módulo:** Django REST Framework  
**Data:** Janeiro 2026
