# API simples de Doação de Livros

Este projeto é uma API desenvolvida em Flask para gerenciar doações de livros como parte de um Desafio no VNW no módulo de Back-end.

## Estrutura do Projeto

A estrutura do projeto segue uma arquitetura organizada em camadas, com separação de responsabilidades:

```
.
├── requirements.txt
├── run.py
├── app/
│   ├── __init__.py
│   ├── config/
│   ├── database/
│   ├── docs/
│   ├── extensions/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── services/
├── migrations/
```

Mais informações: [Link](./app/docs/informacoes.md)

## Endpoints da API

### **GET /**

Retorna uma mensagem.

```json
{
  "message": "API doação de livros"
}
```

---

### **GET /livros**

Lista todos os livros disponíveis no banco de dados.

### **POST /doar**

Adiciona um novo livro ao banco de dados.

**Corpo da Requisição:**
```json
{
  "titulo": "Livro B",
  "categoria": "Educação",
  "autor": "Autor B",
  "image_url": "http://exemplo.com/imagem2.jpg"
}
```

**Exemplo de Resposta:**
- Sucesso:
  ```json
  "Livro adicionado com sucesso."
  ```
- Erro:
  ```json
  "Dados insuficientes."
  ```

## Configuração do Banco de Dados

O projeto utiliza SQLite como banco de dados padrão. A configuração está localizada em `app/database/config.py`.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Davi-D18/desafio-2-livros.git
   cd desafio-2-livros
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Renomei o arquivo `.env.example` para `.env` 

4. Inicie o servidor:
   ```bash
   python run.py
   ```

4. Acesse a API em `localhost:5000`.