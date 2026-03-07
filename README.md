# 🎬 Locadora Virtual API

Uma API REST desenvolvida em **Python com FastAPI** para gerenciamento de um catálogo de filmes.
O projeto foi criado com foco em **prática de backend, containers e DevOps**, utilizando PostgreSQL, Docker, testes automatizados e pipeline CI.

---

# 📌 Objetivo do Projeto

Este projeto foi desenvolvido para praticar conceitos importantes de desenvolvimento backend e infraestrutura moderna:

* Construção de APIs com **FastAPI**
* Persistência de dados com **PostgreSQL**
* Containerização com **Docker**
* Orquestração local com **Docker Compose**
* Testes automatizados com **Pytest**
* Pipeline CI com **GitHub Actions**

---

# 🧱 Arquitetura do Projeto

```
locadora/
│
├── app/
│   ├── main.py          # Entrypoint da API
│   ├── crud.py          # Operações de banco
│   ├── db.py            # Conexão com PostgreSQL
│   └── wait_for_db.py   # Script que aguarda o banco subir
│
├── tests/               # Testes automatizados
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# 🚀 Tecnologias Utilizadas

* Python 3.10
* FastAPI
* PostgreSQL
* Psycopg2
* Docker
* Docker Compose
* Pytest
* GitHub Actions

---

# 📦 Executando o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Marins14/Locadora.git
```

---

## 2️⃣ Subir os containers

```bash
docker compose up --build
```

Isso iniciará:

* API FastAPI
* Banco PostgreSQL

---

## 3️⃣ Acessar a documentação automática

FastAPI gera automaticamente documentação interativa:

```
http://localhost:8000/docs
```

Interface Swagger para testar endpoints diretamente pelo navegador.

---

# 📡 Endpoints da API

## Listar filmes

```
GET /filmes
```

---

## Buscar filme

```
GET /filmes/{titulo}
```

---

## Adicionar filme

```
PUT /filmes/incluir/{titulo}/{quantidade}
```

---

## Remover unidades do filme

```
PUT /filmes/remover/{titulo}/{quantidade}
```

---

## Excluir filme do catálogo

```
PUT /filmes/excluir/{titulo}
```

---

# 🧪 Testes

Os testes utilizam **Pytest** e criam automaticamente a estrutura necessária no banco de dados.

Executar localmente:

```bash
pytest
```

---

# ⚙️ Pipeline CI

O projeto possui pipeline automatizado via **GitHub Actions** que executa:

* Instalação de dependências
* Testes automatizados
* Verificação de formatação com Black
* Build da imagem Docker

Arquivo:

```
.github/workflows/main.yml
```

---

# 🐳 Docker

## Build manual da imagem

```bash
docker build -t locadora-api .
```

## Rodar container

```bash
docker run -p 8000:8000 locadora-api
```

---

# 🗄 Banco de Dados

O banco utilizado é **PostgreSQL**.

Tabela principal:

```
filmes
```

Estrutura:

```
id SERIAL PRIMARY KEY
titulo TEXT
quantidade INTEGER
```

O projeto utiliza a extensão:

```
unaccent
```

para permitir consultas ignorando acentuação.

Exemplo:

```
"Senhor dos Anéis" == "Senhor dos Aneis"
```

---

# 🔒 Variáveis de Ambiente

A aplicação utiliza variáveis de ambiente para conexão com o banco:

```
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

---

# 🧠 Aprendizados

Este projeto permitiu praticar:

* Desenvolvimento de APIs REST
* Manipulação de banco de dados com Python
* Uso de containers
* Integração contínuaCOPY wait_for_db.py /app
* Estruturação de projetos backend
* Boas práticas de automação

---

# 📈 Possíveis Melhorias Futuras

* Alembic para migrações de banco
* Autenticação com JWT
* Deploy em Kubernetes
* Observabilidade com Prometheus + Grafana
* Publicação automática de imagem Docker

---

# 👨‍💻 Autor

**Matheus Marins**

Engenheiro de Computação com foco em **Linux, Infraestrutura, Automação e DevOps**.
