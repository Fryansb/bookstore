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
