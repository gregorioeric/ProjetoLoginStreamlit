# 📝 Guia Completo de Comandos Git

Este guia ensina passo a passo como configurar o Git, iniciar um repositório local e enviar o projeto para o GitHub.  
Cada comando contém uma explicação detalhada e exemplos de saída para facilitar o entendimento.

---

## 1️⃣ Configuração Global do Git

Antes de começar a usar o Git, configure seu **nome** e **e-mail** globais. Eles serão usados em todos os seus commits.

```bash
git config --global --list
```
**Descrição:**  
Lista todas as configurações globais do Git (nome, e-mail, editor, etc).

**Exemplo de saída:**
```
user.name=Eric Gregorio
user.email=eric@email.com
core.editor=code --wait
```

```bash
git config --global user.name "seu nome ou username do github"
```
**Descrição:**  
Define seu nome de usuário global para o Git. Esse nome aparecerá em todos os commits.

```bash
git config --global user.email seuemail@dominio.com
```
**Descrição:**  
Define o e-mail global que será vinculado aos commits no Git.

---

## 2️⃣ Inicialização do Repositório Local

```bash
git init
```
**Descrição:**  
Inicializa um **novo repositório Git** na pasta atual, criando a pasta oculta `.git`.

**Exemplo de saída:**
```
Initialized empty Git repository in C:/MeusProjetos/Projeto/.git/
```

---

## 3️⃣ Configuração de Branch

Por padrão, o Git pode criar o branch `master`. Vamos renomear para `main` (padrão atual do GitHub):

```bash
git branch -m main
```
**Descrição:**  
Renomeia o branch atual para **main**.

```bash
git branch --show-current
```
**Descrição:**  
Mostra o **branch atual** que você está utilizando.  

**Exemplo de saída:**
```
main
```

```bash
git branch -vv
```
**Descrição:**  
Lista todos os branches locais, mostrando:
- O último commit
- Qual branch remoto (upstream) está vinculado (se existir)

**Exemplo de saída:**
```
* main  abc1234 [origin/main] Mensagem do último commit
```

---

## 4️⃣ Preparação para Commit

```bash
git add .
```
**Descrição:**  
Adiciona **todas as alterações** (arquivos novos, modificados e removidos) à área de preparação (staging area).

```bash
git commit -m "seu commit"
```
**Descrição:**  
Registra as alterações adicionadas com uma **mensagem de commit** descritiva.

**Exemplo de saída:**
```
[main (root-commit) abc1234] seu commit
 5 files changed, 120 insertions(+)
 create mode 100644 index.html
```

---

## 5️⃣ Configuração do Repositório Remoto

Após criar um repositório no GitHub, conecte o repositório local ao remoto:

```bash
git remote add origin "link do repositório do github que você criou"
```
**Descrição:**  
Cria uma conexão remota chamada **origin** com o link do repositório do GitHub.

```bash
git remote -v
```
**Descrição:**  
Lista os repositórios remotos conectados.  
Mostra os URLs para **fetch** (baixar) e **push** (enviar).

**Exemplo de saída:**
```
origin  https://github.com/usuario/meu-projeto.git (fetch)
origin  https://github.com/usuario/meu-projeto.git (push)
```

---

## 6️⃣ Envio do Projeto para o GitHub

```bash
git push -u origin main
```
**Descrição:**  
Envia o branch `main` para o repositório remoto `origin`.  
O parâmetro `-u` (**--set-upstream**) cria um vínculo entre o branch local e o remoto, permitindo que nas próximas vezes você use apenas:

```bash
git push
git pull
```

**Exemplo de saída:**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 1.23 KiB | 1.23 MiB/s, done.
To https://github.com/usuario/meu-projeto.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

---

## 7️⃣ Próximos Commits

Após a primeira configuração, para enviar novas alterações basta fazer:

```bash
git add .
git commit -m "mensagem do commit"
git push
```

O Git já sabe para onde enviar devido ao `-u` configurado na primeira vez.

---

## ✅ Dicas Úteis

- Ver o status do repositório:
```bash
git status
```

- Ver o histórico de commits:
```bash
git log --oneline --graph --decorate
```

- Clonar um repositório existente:
```bash
git clone URL_DO_REPOSITORIO
```

---

> **Pronto!** Agora você tem um guia completo em Markdown para iniciar e enviar seus projetos para o GitHub usando Git.
