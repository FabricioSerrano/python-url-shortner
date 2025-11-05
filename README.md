# 🔗 Python URL Shortener

## 📌 Visão Geral

Este projeto é um **encurtador de URLs** desenvolvido em Python com **FastAPI**, mas com foco especial em **arquitetura escalável**. Embora o código em si seja simples, o objetivo é simular os desafios reais de sistemas que lidam com altíssimos volumes de requisições — como é o caso de encurtadores de links em produção.

---

## 🧠 Arquitetura e Estratégia

O sistema foi projetado para suportar escalabilidade horizontal e alta disponibilidade, utilizando:

- **Cassandra**: Banco de dados distribuído, ideal para escrita massiva e replicação.
- **Redis**:
  - Uma instância para **INCR** (geração de IDs únicos).
  - Outra instância para **cache aside** (armazenamento temporário de URLs).
- **Hashids**: Gera códigos curtos e únicos a partir de IDs numéricos.
- **Docker**: Empacotamento da aplicação para ambientes isolados.
- **Kubernetes**: Orquestração de containers para escalabilidade e resiliência.

---

## 🧩 Estrutura do Projeto

- **shortner/**: Lógica principal de encurtamento e redirecionamento.
- **deployment/**: Arquivos de configuração para Docker e Kubernetes.

---

## ⚙️ Tecnologias e Dependências

- Python 3.11+
- FastAPI
- Cassandra
- Redis (Cluster)
- Hashids
- Ruff (linting)
- Docker
- Kubernetes

*Este Readme foi gerado com Inteligência Artificial e melhorado por Inteligência Natural*