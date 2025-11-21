# Platinium APIs 🚀

API REST desenvolvida em Python usando Azure Functions para o aplicativo de Inteligência Emocional Platinium.

## 📋 Sobre o Projeto

Esta API fornece endpoints para gerenciar produtos, usuários e funcionalidades do app Platinium, focado em inteligência emocional e bem-estar.

## 🛠️ Tecnologias

- **Python 3.11+**
- **Azure Functions** (Serverless)
- **Azure SQL Database**
- **pyodbc** - Conexão com SQL Server
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📁 Estrutura do Projeto
```
platinium_api/
├── src/
│   ├── functions/         # Azure Functions individuais
│   ├── shared/
│   │   ├── database/      # Conexão e queries do banco
│   │   └── utils/         # Funções utilitárias (responses, etc)
│   └── models/            # Models de dados
├── function_app.py        # Arquivo principal das Functions
├── host.json              # Configuração do Azure Functions
├── local.settings.json    # Variáveis de ambiente (não versionado)
├── requirements.txt       # Dependências Python
└── README.md
```

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.11 ou superior
- Azure Functions Core Tools
- Acesso ao banco de dados Azure SQL

### Instalação

1. **Clone o repositório:**
```bash
   git clone https://github.com/lnmonteiro/platinium_api.git
   cd platinium_api
```

2. **Crie e ative o ambiente virtual:**
```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
   pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
   
   Crie o arquivo `local.settings.json`:
```json
   {
     "IsEncrypted": false,
     "Values": {
       "AzureWebJobsStorage": "",
       "FUNCTIONS_WORKER_RUNTIME": "python",
       "DB_CONNECTION_STRING": "Driver={ODBC Driver 18 for SQL Server};Server=seu-servidor.database.windows.net;Database=seu-banco;Uid=seu-usuario;Pwd=sua-senha;Encrypt=yes;TrustServerCertificate=no;"
     }
   }
```

5. **Execute localmente:**
```bash
   func start
```

A API estará disponível em `http://localhost:7071`

## 📡 Endpoints

### `GET /api/hello`
Endpoint de teste para verificar se a API está funcionando.

**Parâmetros de Query:**
- `name` (opcional): Nome para saudação personalizada

**Exemplo de Resposta:**
```json
{
  "status": "success",
  "timestamp": "2025-11-21T01:30:00.000000Z",
  "data": {
    "message": "Olá, Lucas! Bem-vindo à API!"
  }
}
```

### `GET /api/products`
Retorna a lista de produtos disponíveis (ebooks, cursos, etc).

**Exemplo de Resposta:**
```json
{
  "status": "success",
  "timestamp": "2025-11-21T01:30:00.000000Z",
  "total": 2,
  "data": {
    "produtos": [
      {
        "Criado por": "Karen Monteiro",
        "Nome": "Autoestima",
        "Tipo de Produto": "Ebook",
        "Descrição": "Um guia prático de autoestima...",
        "Badges": "Autoconsciência em Ação;Força Interna",
        "Duração": 0,
        "Páginas": 25,
        "Preço": "19.90",
        "Desconto plano básico": "0.05",
        "Desconto plano VIP": "0.25"
      }
    ]
  }
}
```

## 🔒 Segurança

- ⚠️ **Nunca commite o arquivo `local.settings.json`** - ele contém informações sensíveis
- 🔐 Use variáveis de ambiente para credenciais
- 🛡️ Mantenha as dependências atualizadas

## 🚢 Deploy no Azure

### Via Azure Portal
1. Crie um Function App no Azure
2. Configure as variáveis de ambiente no Application Settings
3. Faça deploy via VS Code ou Azure CLI

### Via Azure CLI
```bash
func azure functionapp publish 
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é privado e pertence a Karen Monteiro / Platinium.

## 👥 Autores

- **Lucas Monteiro** - *Desenvolvimento* - [@lnmonteiro](https://github.com/lnmonteiro)
- **Karen Monteiro** - *Idealizadora* - Platinium

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através do GitHub.

---

⭐️ Desenvolvido com Python e ☕ para o Platinium App
