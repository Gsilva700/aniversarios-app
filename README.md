
Um aplicativo para registrar datas de aniversário e enviar notificações (e-mail, SMS ou WhatsApp) no dia do aniversário.

## Funcionalidades

- Cadastro de aniversários com nome, data de aniversário, e-mail e telefone.
- Verificação diária de aniversários.
- Envio automático de:
  - E-mails.
  - SMS (via Twilio).
  - Mensagens no WhatsApp (via Twilio).

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **Flask**: Framework para o backend.
- **SQLite**: Banco de dados.
- **Twilio**: API para envio de SMS e WhatsApp.
- **SMTP**: Protocolo para envio de e-mails.
- **Agendador de Tarefas do Windows**: Para execução diária do script.

## Como Usar

Crie uma conta no Twilio e obtenha as credenciais (ACCOUNT_SID, AUTH_TOKEN e número de telefone).

Configure um e-mail do Gmail e gere uma senha de app em Gmail.

### Configuração
Configure as variáveis de ambiente no código:

TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER no arquivo verificar_aniversarios.py.

EMAIL_USER e EMAIL_PASSWORD no arquivo verificar_aniversarios.py.

### Executando o Projeto
Inicie o servidor Flask:

Use o Postman ou curl para enviar uma requisição POST:

Agende a verificação diária no Windows usando o Agendador de Tarefas.

## Estrutura do Projeto

aniversarios-app/
├── app.py               # Backend Flask
├── verificar_aniversarios.py  # Script de verificação
├── database.db          # Banco de dados SQLite
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação

### Contribuição

Contribuições são bem-vindas!

