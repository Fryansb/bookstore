# 🚀 Deploy Online

- 🔗 **Acesse o projeto:** [https://ryansb.pythonanywhere.com](https://ryansb.pythonanywhere.com)
- 🔑 **Admin:** [https://ryansb.pythonanywhere.com/admin/](https://ryansb.pythonanywhere.com/admin/)
	- Usuário: admin
	- Senha: admin123

### Endpoints principais:
- [API Products](https://ryansb.pythonanywhere.com/bookstore/v1/product/product/)
- [API Category](https://ryansb.pythonanywhere.com/bookstore/v1/product/category/)
- [API Order](https://ryansb.pythonanywhere.com/bookstore/v1/order/)

# Bookstore API

Projeto Django REST Framework desenvolvido durante o curso Backend Python da EBAC.

## 📚 Descrição

API REST completa para gerenciamento de uma livraria (bookstore) com sistema de produtos, categorias e pedidos.

## 🔗 Links Importantes

- [Repositório GitHub](https://github.com/Fryansb/bookstore)
- [PR CI/CD #9](https://github.com/Fryansb/bookstore/pull/9)
- [GitHub Actions](https://github.com/Fryansb/bookstore/actions)
- [Painel Admin (Deploy)](https://ryansb.pythonanywhere.com/admin/)
- [API Categorias (Deploy)](https://ryansb.pythonanywhere.com/bookstore/v1/product/category/)
- [API Produtos (Deploy)](https://ryansb.pythonanywhere.com/bookstore/v1/product/product/)
- [API Pedidos (Deploy)](https://ryansb.pythonanywhere.com/bookstore/v1/order/)

## 🚀 Tecnologias

- Python 3.12+
- Django 6.0.1
- Django REST Framework 3.16.1
- PostgreSQL 14 (Docker)
- Docker & Docker Compose
- Poetry (gerenciador de dependências)
- pytest + factory-boy (testes)
- GitHub Actions (CI/CD)

## 📦 Instalação

### Opção 1: Com Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/Fryansb/bookstore.git
cd bookstore

# Configure as variáveis de ambiente
cp env.dev .env

# Inicie os containers
docker-compose up -d

# Execute as migrações
docker-compose exec web python manage.py migrate

# Crie um superusuário
docker-compose exec web python manage.py createsuperuser

# Acesse: http://localhost:8000/admin/
```

### Opção 2: Desenvolvimento Local

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

**Credenciais de acesso:**
- **Usuário**: admin
- **Senha**: (fornecida pelo instrutor)

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

**Exercício:**
- ✅ Django REST Framework adicionado via `poetry add djangorestframework`
- ✅ `poetry.lock` atualizado com `poetry update`
- ✅ `rest_framework` adicionado ao `INSTALLED_APPS`
- ✅ Projeto testado e funcional

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
