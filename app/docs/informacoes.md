## Estrutura Geral
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

### Arquivos e Pastas

- **`.env`**: Contém variáveis de ambiente, como configurações do Flask (`FLASK_APP`, `FLASK_ENV`).

- **`requirements.txt`**: Lista de dependências do projeto

- **`run.py`**: Arquivo para inicializar a aplicação Flask.

---

### Diretório `app/`

Este é o diretório principal da aplicação, contendo a lógica do projeto.

- **`__init__.py`**: Inicializa a aplicação Flask, registra as rotas e inicializa extensões.

- **`config.py`**: Configurações gerais da aplicação.

- **`database/`**: Contém configurações relacionadas ao banco de dados e o banco

- **`docs/`**: Explicação da estrutura de pastas.

- **`extensions/`**: Configurações de extensões do Flask.

- **`models/`**: Contém os modelos do banco de dados. Exemplo: `livros.py`, que define a tabela `Livros`.

- **`repositories/`**: Camada de acesso ao banco de dados. Exemplo: `livros_repository.py`, que contém funções para manipular os dados de livros.

- **`routes/`**: Define as rotas da API. Exemplo: `routes.py`, que contém endpoints como `/livros` e `/doar`.

- **`services/`**: Contém a lógica, validações.

**Fluxo:**

1. **Controller (Rota):** Recebe a requisição do usuário e chama o Service adequado.
2. **Service:** Processa a lógica de negócio e solicita ao Repository as operações necessárias no banco de dados.
3. **Repository:** Executa as operações de leitura e escrita no banco de dados.
4. **Service:** Recebe os dados do Repository, aplica a lógica necessária e retorna para o usuário.

### Diretório `migrations/`

Gerenciado pelo Flask-Migrate, contém arquivos para controle de versões do banco de dados.

- **`versions/`**: Armazena os scripts de migração gerados.