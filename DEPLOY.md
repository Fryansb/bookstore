# 🚀 Guia de Deploy - Render

Este guia explica como fazer o deploy do Bookstore API no Render.

## 📋 Pré-requisitos

- Conta no GitHub (já tem ✅)
- Conta no Render (criar em https://render.com)
- Repositório GitHub com código atualizado

## 🔧 Passos para Deploy

### 1. Criar conta no Render
1. Acesse https://render.com
2. Clique em "Get Started for Free"
3. Faça login com GitHub
4. Autorize o Render a acessar seus repositórios

### 2. Criar Web Service
1. No dashboard do Render, clique em "New +"
2. Selecione "Web Service"
3. Conecte seu repositório: `Fryansb/bookstore`
4. Configure:
   - **Name**: `bookstore-api`
   - **Region**: `Frankfurt (EU Central)` ou `Oregon (US West)`
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn bookstore.wsgi:application`
   - **Instance Type**: `Free`

### 3. Adicionar Banco de Dados PostgreSQL
1. No dashboard do Render, clique em "New +"
2. Selecione "PostgreSQL"
3. Configure:
   - **Name**: `bookstore-db`
   - **Database**: `bookstore`
   - **User**: (gerado automaticamente)
   - **Region**: Mesma região do Web Service
   - **PostgreSQL Version**: `15`
   - **Instance Type**: `Free`
4. Clique em "Create Database"
5. **Copie a Internal Database URL** (formato: `postgresql://...`)

### 4. Configurar Variáveis de Ambiente
No seu Web Service, vá em "Environment" e adicione:

```
DEBUG=False
SECRET_KEY=<GERE_UMA_CHAVE_SEGURA>
ALLOWED_HOSTS=bookstore-api.onrender.com
DATABASE_URL=<COLE_A_INTERNAL_DATABASE_URL>
```

**Para gerar SECRET_KEY segura:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy Automático
1. Salve as variáveis de ambiente
2. O Render iniciará o deploy automaticamente
3. Aguarde ~5-10 minutos
4. Acesse: `https://bookstore-api.onrender.com/admin/`

### 6. Criar Superusuário
No dashboard do Render, vá em "Shell" e execute:
```bash
python manage.py createsuperuser
```

## 🔗 Endpoints da API

Após deploy, sua API estará disponível em:

- **Admin**: https://bookstore-api.onrender.com/admin/
- **Categorias**: https://bookstore-api.onrender.com/bookstore/v1/product/category/
- **Produtos**: https://bookstore-api.onrender.com/bookstore/v1/product/product/
- **Pedidos**: https://bookstore-api.onrender.com/bookstore/v1/order/

## 📝 Notas Importantes

### ⚠️ Limitações do Plano Free
- O serviço "dorme" após 15 minutos de inatividade
- Primeira requisição após inatividade pode demorar ~30 segundos
- PostgreSQL free tem limite de 1GB
- Build time limitado a 30 minutos

### 🔄 Deploy Contínuo
Qualquer push para a branch `main` no GitHub dispara deploy automático no Render.

### 🐛 Troubleshooting

**Erro: "Application failed to start"**
- Verifique logs no dashboard do Render
- Confirme se todas variáveis de ambiente estão configuradas
- Verifique se DATABASE_URL está correto

**Erro: "Static files not found"**
- Confirme se `build.sh` tem permissão de execução
- Verifique se `whitenoise` está instalado

**Erro: "Database connection failed"**
- Use a **Internal Database URL** (não External)
- Confirme se o banco PostgreSQL está no estado "Available"

## 🎯 Checklist de Deploy

- [ ] Conta Render criada
- [ ] Repositório GitHub conectado
- [ ] Web Service configurado
- [ ] PostgreSQL database criado
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy concluído com sucesso
- [ ] Superusuário criado
- [ ] API testada e funcionando
- [ ] Link enviado para EBAC

## 📚 Recursos

- [Render Docs - Django](https://render.com/docs/deploy-django)
- [Render Community Forum](https://community.render.com/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)

---

**Desenvolvido para:** EBAC - Backend Python  
**Módulo:** Deploy em Cloud  
**Data:** Janeiro 2026
