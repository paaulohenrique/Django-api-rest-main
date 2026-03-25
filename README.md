🚀 Django API REST – Gerenciamento de Clientes
API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de clientes, com suporte a autenticação JWT, paginação e documentação automática.
📌 Sobre o Projeto
Este projeto implementa uma API estruturada e versionada (api/v1) com foco em boas práticas de desenvolvimento backend.
A aplicação permite o gerenciamento de clientes e foi projetada para ser escalável, com suporte para novos modelos e funcionalidades.
🧱 Arquitetura
Estrutura modular por versão de API (api/v1)
Separação em camadas: models, serializers, viewsets e routers
Padrão REST para comunicação
Preparado para expansão com novos recursos
⚙️ Tecnologias Utilizadas
Django
Django REST Framework
Autenticação JWT
PostgreSQL / SQLite
Swagger (documentação automática)
🚀 Funcionalidades
CRUD completo de clientes
API versionada (v1)
Autenticação com JWT
Proteção de rotas com token
Paginação de resultados
Documentação interativa com Swagger
Integração com banco de dados relacional
🔐 Autenticação
A API utiliza JWT para autenticação.
Obter token:
POST /api/token/
Usar token:
Authorization: Bearer SEU_TOKEN
📡 Endpoints (exemplo)
GET /api/v1/clientes/ → Lista clientes
POST /api/v1/clientes/ → Cria cliente
GET /api/v1/clientes/{id}/ → Detalhe
PUT /api/v1/clientes/{id}/ → Atualiza
DELETE /api/v1/clientes/{id}/ → Remove
📄 Documentação da API
A documentação interativa pode ser acessada em:
/api/docs/
🗄️ Banco de Dados
SQLite para desenvolvimento
PostgreSQL para produção
Configuração feita via settings do Django.
▶️ Como Executar
Backend
git clone <seu-repositorio>
cd backend

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
API disponível em:
http://127.0.0.1:8000/
🧪 Testes
python manage.py test
📌 Melhorias Futuras
Implementação de novos modelos (Product, Order)
Validações avançadas nos serializers
Deploy em ambiente de produção
Logs e monitoramento
🛠️ Ferramentas
Git e GitHub
Postman para testes de API
