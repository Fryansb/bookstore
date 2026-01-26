# 🚂 Deploy no Railway - Guia Completo

## 🎯 Passo a Passo (10 minutos)

### 1️⃣ Criar Conta no Railway
1. Acesse: https://railway.app
2. Clique em **"Login"**
3. Escolha **"Login with GitHub"**
4. Autorize o Railway a acessar seus repositórios
5. ✅ Você ganha **$5 de crédito grátis/mês** (suficiente para o projeto)

---

### 2️⃣ Criar Novo Projeto
1. No dashboard, clique em **"New Project"**
2. Selecione **"Deploy from GitHub repo"**
3. Escolha: **`Fryansb/bookstore`**
4. O Railway detecta automaticamente que é Django!

---

### 3️⃣ Adicionar PostgreSQL
1. No mesmo projeto, clique em **"+ New"**
2. Selecione **"Database"**
3. Escolha **"Add PostgreSQL"**
4. ✅ Railway cria e configura automaticamente!

---

### 4️⃣ Configurar Variáveis de Ambiente
1. Clique no serviço **bookstore** (não no database)
2. Vá na aba **"Variables"**
3. Clique em **"+ New Variable"** e adicione:

```env
DEBUG=False
SECRET_KEY=<GERAR_NOVA_CHAVE_SEGURA>
ALLOWED_HOSTS=<SEU_DOMINIO>.up.railway.app
PORT=8000
```

**Para gerar SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. O Railway já configura `DATABASE_URL` automaticamente! 🎉

---

### 5️⃣ Conectar Database ao App
1. No serviço **bookstore**, vá em **"Settings"**
2. Role até **"Service Variables"**
3. Clique em **"Add Reference"**
4. Selecione o PostgreSQL
5. Escolha **"DATABASE_URL"**
6. ✅ Conexão automática!

---

### 6️⃣ Deploy Automático
O Railway já iniciou o deploy! Acompanhe:
1. Vá na aba **"Deployments"**
2. Clique no deploy em andamento
3. Veja os logs em tempo real
4. Aguarde aparecer: ✅ **"Success"**

⏱️ Tempo: 3-5 minutos

---

### 7️⃣ Obter URL do Projeto
1. Vá na aba **"Settings"**
2. Role até **"Domains"**
3. Clique em **"Generate Domain"**
4. Railway cria: `seu-app.up.railway.app`
5. **Copie essa URL!**

---

### 8️⃣ Atualizar ALLOWED_HOSTS
1. Volte na aba **"Variables"**
2. Edite `ALLOWED_HOSTS`
3. Substitua por: `seu-app.up.railway.app`
4. Salve (deploy automático acontece)

---

### 9️⃣ Criar Superusuário (Importante!)
1. No dashboard, clique nos **3 pontinhos** do serviço
2. Selecione **"Run Command"** ou **"Shell"**
3. Execute:
```bash
python manage.py createsuperuser
```
4. Preencha:
   - Username: `admin`
   - Email: (seu email)
   - Password: (crie uma senha)
   - Confirme a senha

---

### 🎉 Pronto! Acesse sua API:

**Painel Admin:**
```
https://seu-app.up.railway.app/admin/
```

**API Endpoints:**
```
https://seu-app.up.railway.app/bookstore/v1/product/category/
https://seu-app.up.railway.app/bookstore/v1/product/product/
https://seu-app.up.railway.app/bookstore/v1/order/
```

---

## 📊 Monitoramento

**Ver Logs:**
- Dashboard → Serviço → Aba "Deployments" → "View Logs"

**Uso de Créditos:**
- Dashboard → "Usage" (menu lateral)
- Você tem $5/mês grátis
- Este projeto usa ~$3-4/mês

**Reiniciar Serviço:**
- Settings → "Restart"

---

## ⚙️ Dicas Importantes

### ✅ Vantagens do Railway:
- Deploy automático a cada push no GitHub
- PostgreSQL incluído e configurado automaticamente
- Logs em tempo real
- CLI opcional (railway CLI)
- SSL/HTTPS automático

### ⚠️ Limitações Free Tier:
- $5 crédito/mês (~500 horas de runtime)
- Serviço para se ficar inativo por muito tempo
- 1 projeto ativo por vez
- 100 GB tráfego/mês

### 🔄 Deploy Contínuo:
Qualquer push na branch `main` do GitHub dispara deploy automático!

---

## 🐛 Troubleshooting

**Erro: "Application failed to start"**
```bash
# Ver logs detalhados:
1. Deployments → Clique no deploy
2. Veja a seção "Build Logs" e "Deploy Logs"
```

**Erro: "Database connection failed"**
```bash
# Verifique:
1. PostgreSQL está "Active"?
2. DATABASE_URL está configurada?
3. Settings → Service Variables → DATABASE_URL existe?
```

**Erro: "Static files not found"**
```bash
# No shell do Railway:
python manage.py collectstatic --no-input
```

**Erro: "Bad Request (400)"**
```bash
# Verifique ALLOWED_HOSTS:
1. Variables → ALLOWED_HOSTS
2. Deve conter: seu-dominio.up.railway.app
```

---

## 📋 Checklist de Deploy

- [ ] Conta Railway criada
- [ ] Projeto GitHub conectado
- [ ] PostgreSQL adicionado
- [ ] Variáveis de ambiente configuradas
- [ ] DATABASE_URL conectada
- [ ] Domínio gerado
- [ ] ALLOWED_HOSTS atualizado
- [ ] Deploy concluído (status: Success)
- [ ] Superusuário criado
- [ ] Admin acessível
- [ ] APIs testadas
- [ ] Link enviado para EBAC

---

## 🎓 Para Entregar na EBAC

Envie este link no PR #9:
```
https://seu-app.up.railway.app/admin/
```

Inclua também os endpoints da API:
- Categorias: `/bookstore/v1/product/category/`
- Produtos: `/bookstore/v1/product/product/`
- Pedidos: `/bookstore/v1/order/`

---

## 🔗 Links Úteis

- **Dashboard Railway**: https://railway.app/dashboard
- **Documentação**: https://docs.railway.app
- **Status**: https://railway.app/status
- **Discord Support**: https://discord.gg/railway

---

**Curso:** Backend Python - EBAC  
**Módulo:** Cloud Deploy  
**Plataforma:** Railway  
**Data:** Janeiro 2026
