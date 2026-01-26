# 🐍 Deploy no PythonAnywhere - Guia Passo a Passo

## 🎯 Por que PythonAnywhere?
- ✅ **100% Gratuito** (sem cartão de crédito)
- ✅ **Recomendado pelo professor EBAC**
- ✅ Usa SQLite (já configurado no projeto)
- ✅ Estável e confiável
- ⏱️ Tempo total: ~15-20 minutos

---

## 📋 Passo a Passo Completo

### 1️⃣ Criar Conta (2 minutos)

1. Acesse: https://www.pythonanywhere.com
2. Clique em **"Pricing & signup"**
3. Escolha **"Create a Beginner account"** (FREE)
4. Preencha:
   - Username: (escolha um nome único)
   - Email: seu email
   - Password: crie uma senha
5. Confirme o email
6. ✅ Login na plataforma

---

### 2️⃣ Abrir Console Bash (1 minuto)

1. No dashboard, clique em **"Consoles"**
2. Clique em **"Bash"** (console novo)
3. Um terminal vai abrir no navegador

---

### 3️⃣ Clonar Repositório GitHub (2 minutos)

No console Bash, execute:

```bash
# Clone seu repositório
git clone https://github.com/Fryansb/bookstore.git

# Entre na pasta
cd bookstore

# Veja os arquivos
ls -la
```

✅ Você deve ver: `manage.py`, `requirements.txt`, etc.

---

### 4️⃣ Criar Virtual Environment (3 minutos)

```bash
# Criar virtualenv com Python 3.10 (PythonAnywhere free tier)
mkvirtualenv bookstore-env --python=python3.10

# O ambiente será ativado automaticamente (aparece (bookstore-env) no prompt)

# Instalar dependências
pip install -r requirements.txt

# Aguarde ~2-3 minutos para instalar tudo
```

**Se der erro em algum pacote**, instale manualmente:
```bash
pip install Django==5.1.15 djangorestframework==3.16.1 django-extensions==4.1 gunicorn==21.2.0 whitenoise==6.6.0 python-decouple==3.8 dj-database-url==2.1.0
```

⚠️ **Importante:** Django 6.0+ requer Python 3.12. PythonAnywhere free tier usa Python 3.10, então usamos Django 5.1.15.

---

### 5️⃣ Configurar Django para PythonAnywhere (2 minutos)

```bash
# Criar arquivo .env
cat > .env << EOF
DEBUG=False
SECRET_KEY=#3*3mo%n)zb6vwz4t78@$vbu^g-g@s438blj+--cta5c56hbeo
ALLOWED_HOSTS=seu-username.pythonanywhere.com
DATABASE_URL=
EOF

# Coletar arquivos estáticos
python manage.py collectstatic --no-input

# Rodar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Digite: admin / seu@email.com / senha123 (ou sua preferência)
```

---

### 6️⃣ Configurar Web App (5 minutos)

1. **Vá em "Web"** (menu superior)
2. Clique em **"Add a new web app"**
3. Clique **"Next"** (confirma o domínio free)
4. Escolha **"Manual configuration"** (não escolha Django!)
5. Escolha **"Python 3.10"**
6. Clique **"Next"**

---

### 7️⃣ Configurar WSGI File (3 minutos)

1. Na página **Web**, role até **"Code"**
2. Clique no link do **"WSGI configuration file"**
   - Exemplo: `/var/www/seu_username_pythonanywhere_com_wsgi.py`
3. **DELETE TODO O CONTEÚDO** do arquivo
4. **Cole este código**:

```python
import os
import sys

# Adicionar o projeto ao path
path = '/home/seu_username/bookstore'  # ⚠️ MUDE "seu_username" para seu username!
if path not in sys.path:
    sys.path.append(path)

# Configurar Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'bookstore.settings'

# Carregar variáveis de ambiente
from pathlib import Path
from decouple import Config, RepositoryEnv

BASE_DIR = Path(path)
env_file = BASE_DIR / '.env'
config = Config(RepositoryEnv(str(env_file)))

# Importar WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. **IMPORTANTE**: Substitua `seu_username` pelo seu username do PythonAnywhere
6. Clique em **"Save"** (canto superior direito)

---

### 8️⃣ Configurar Virtualenv (1 minuto)

1. Volte para a página **Web**
2. Role até **"Virtualenv"**
3. Clique em **"Enter path to a virtualenv"**
4. Digite:
```
/home/seu_username/.virtualenvs/bookstore-env
```
5. ⚠️ **Mude "seu_username"** para seu username real
6. Clique no ✅ para confirmar

---

### 9️⃣ Configurar Static Files (2 minutos)

1. Na página **Web**, role até **"Static files"**
2. Clique em **"Enter URL"** e adicione:

**URL:** `/static/`  
**Directory:** `/home/seu_username/bookstore/staticfiles`

3. Clique no ✅

4. Adicione outro:

**URL:** `/admin/`  
**Directory:** `/home/seu_username/.virtualenvs/bookstore-env/lib/python3.10/site-packages/django/contrib/admin/static/admin`

5. ⚠️ **Mude "seu_username"** nos dois paths

---

### 🔟 Reload e Testar! (1 minuto)

1. No topo da página **Web**, clique no botão verde **"Reload"**
2. Aguarde ~10 segundos
3. Clique no link do seu site:
```
https://seu-username.pythonanywhere.com
```

---

## 🎉 Acesse sua API!

**Admin:**
```
https://seu-username.pythonanywhere.com/admin/
```
Login: `admin` / `senha123`

**API Endpoints:**
```
https://seu-username.pythonanywhere.com/bookstore/v1/product/category/
https://seu-username.pythonanywhere.com/bookstore/v1/product/product/
https://seu-username.pythonanywhere.com/bookstore/v1/order/
```

---

## 🐛 Troubleshooting

### ❌ Erro 500 - Internal Server Error

**Solução 1:** Ver logs de erro
```bash
# No console Bash:
tail -n 50 /var/log/seu_username.pythonanywhere.com.error.log
```

**Solução 2:** Verificar ALLOWED_HOSTS
```bash
cd ~/bookstore
nano .env
# Confirme: ALLOWED_HOSTS=seu-username.pythonanywhere.com
```

**Solução 3:** Verificar path no WSGI
- Abra o WSGI file e confirme que `seu_username` está correto

---

### ❌ Erro "ImproperlyConfigured"

```bash
# Reinstalar dependências
workon bookstore-env
pip install --upgrade Django djangorestframework python-decouple dj-database-url
```

---

### ❌ Static files não carregam

```bash
# Recoletar static files
cd ~/bookstore
workon bookstore-env
python manage.py collectstatic --no-input --clear
```

Depois:
1. Web → Reload

---

### ❌ "DisallowedHost at /"

**Edite settings.py diretamente:**
```bash
nano ~/bookstore/bookstore/settings.py
```

Procure por `ALLOWED_HOSTS` e adicione:
```python
ALLOWED_HOSTS = ['seu-username.pythonanywhere.com', 'localhost', '127.0.0.1']
```

Salve (Ctrl+O, Enter, Ctrl+X) e Reload.

---

### ❌ ModuleNotFoundError: decouple

```bash
workon bookstore-env
pip install python-decouple
```

Web → Reload

---

## 📝 Comandos Úteis

**Ativar virtualenv:**
```bash
workon bookstore-env
```

**Ver logs em tempo real:**
```bash
tail -f /var/log/seu_username.pythonanywhere.com.error.log
```

**Atualizar código do GitHub:**
```bash
cd ~/bookstore
git pull origin main
workon bookstore-env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
# Web → Reload
```

**Rodar comandos Django:**
```bash
cd ~/bookstore
workon bookstore-env
python manage.py shell
python manage.py dbshell
python manage.py createsuperuser
```

---

## 🔄 Deploy Contínuo (Atualizações)

Quando você fizer mudanças no código:

```bash
cd ~/bookstore
git pull origin main
workon bookstore-env
pip install -r requirements.txt  # Se mudou dependências
python manage.py migrate  # Se mudou models
python manage.py collectstatic --no-input  # Se mudou CSS/JS
```

Depois: **Web → Reload**

---

## 📊 Limitações Free Tier

- ⚠️ 1 web app por conta
- ⚠️ CPU limitada (pode ser lento em picos)
- ⚠️ 512 MB de storage
- ⚠️ Limite de requisições/dia
- ⚠️ SQLite apenas (MySQL precisa upgrade)
- ✅ Suficiente para projetos educacionais!

---

## 🎓 Para Entregar na EBAC

Envie este link no PR #9:

```
https://seu-username.pythonanywhere.com/admin/
```

Inclua também:
- API Categorias: `/bookstore/v1/product/category/`
- API Produtos: `/bookstore/v1/product/product/`
- API Pedidos: `/bookstore/v1/order/`

---

## 🔗 Links Úteis

- **Dashboard:** https://www.pythonanywhere.com/user/seu_username/
- **Consoles:** https://www.pythonanywhere.com/user/seu_username/consoles/
- **Web:** https://www.pythonanywhere.com/user/seu_username/webapps/
- **Files:** https://www.pythonanywhere.com/user/seu_username/files/
- **Help Forum:** https://www.pythonanywhere.com/forums/

---

**Curso:** Backend Python - EBAC  
**Módulo:** Cloud Deploy  
**Plataforma:** PythonAnywhere  
**Data:** Janeiro 2026

**🎯 Dica Final:** Se tiver qualquer erro, copie a mensagem e consulte os logs em `/var/log/` ou peça ajuda ao tutor EBAC!
