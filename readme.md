# TaskManagerAPI

O taskManagerAPI trata-se de uma **API** (**Interface de programação de aplicativo**) para o usuário organizar as atividades do dia à dia onde o mesmo pode criar uma nova tarefa, atualizar e deletar a mesma, essa API é integrada com a API do google calendar, logo toda vez que o usuário adicionar, a mesma será adicionada na agenda vinculada com esta API, da mesma maneira se o mesmo deletar alguma tarefa, a mesma será removida da agenda vinculada a esta API.

## Tecnologias utilizadas

- Python
- Django
- Djangorestframework
- Djangorestframework-simplejwt
- Sqlite
- Google cloud platform
- Google Calendar API

## Funcionalidades

- **Adicicionar uma nova tarefa**, o usuário pode criar uma nova tarefa passando os parâmetro, title, description, date, time e time_end, onde apenas o title, date, time e time_end são obrigatórios;

- **Buscar tarefas**, o usuário pode buscar tarefas com base no ID, período de datas e títulos;

- **Deletar tarefas** O usuário pode apagar tarefas fornecendo o ID da tarefa;

- **Atualizar tarefa**, o usuário pode atualizar tarefas passando o ID da tarefa como parâmetro, porém essa atualização será ignorada no google calendar;

## Preparando o ambiente

1. Configure o ambiente no google cloud platform conforme está cendo pedido nesse link <https://developers.google.com/calendar/api/quickstart/python?hl=pt-br>;
2. Após configurar tudo, baixe o json com suas credenciais salve com o nome **credentials.json**;
3. Crie uma nova agenda no google calendar, logo em seguida vá nas configurações da mesma role até ver o calendar ID, ou ID da agenda, copie esse código e reseve em algum lugar;
4. Crie uma pasta: **mkdir task_manager**;
5. Entre na pasta: **cd <diretório da pasta criada>**
6. Clone o repositório: **git clone** <https://github.com/Denilsoj/task_manager_api.git>;
7. Mova o arquivo credentials.json para o diretório /task_manager/task_manager_api/tasks/auth;
8. Crie um ambiente virtual: **python3 -m venv venv**;
9. Ative o ambiente virtual: **source venv/bin/activate**;
10. Entre na pasta do projeto **cd task_manage_api**
11. Baixe as dependencias: **pip install -r requirements.txt**;
12. Faça as migrações da sua base de dados: **python task_manager_api/manage.py migrate**
13. Crie o arquivo **.env** para configurar as variáveis de ambientes;
14. Copie todas as variáveis de ambientes do arquivo **.env-exaple** e coloque no seu **.env**;
15. Substitua os valores das variáveis de ambiente, na CALENDAR_ID coloque o seu calendar ID que foi reservado no 3 passo, já na SECRET_KEY gere uma nova com o comando: **python -c  "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"** e atribua esse valor na SECRET_KEY;
16. Start o servidor com o comando: **python task_manager_api/manage.py runserver**.

***Obeservação:*** Para desativar o ambiente virtual digite no terminal **deactivate**
  
## Rotas

- Para manipulação de usuários: <http://127.0.0.1:8000/users/>
- Para manipulação Tarefas: <http://127.0.0.1:8000/tasks/>
- Para gerar um token: <http://127.0.0.1:8000/token/>
- Para gerar um novo token access: <http://127.0.0.1:8000/token/refresh/>

## Modo de Uso

***Todos os dados do body devem ser no formato Json***

***Fluxo de uso**

1. Crie um novo usuário na rota <http://127.0.0.1:8000/users/>
2. Gere um jwt na rota <http://127.0.0.1:8000/token/>
3. Crie uma nova tarefa <http://127.0.0.1:8000/tasks/>

 **Pode manipular as tarefas da maneira que assim preferir, só lembre de autenticar o usuário, instruções de como fazer logo abaixo.**

### Rota de Users

#### POST <http://127.0.0.1:8000/users/>
  
***Observações: Os campos username e email são do tipo unique, logo precisam serem únicos***

Body:

    {

     "username": "denilson",
     "password": "123456",
     "email": "denilson@email.com",
     "first_name": "Denilson",
     "last_name": "Oliveira"

    }

Response:

    {

    "id": "1",
    "username": "denilson",
    "email": "denilson@email.com"

    }

#### PUT <http://127.0.0.1:8000/users/1/>

  Forneça o id do usuário na rota: "**/1/**"

  Body:

    {

    "password": "1234567",

    }

Response:

    {

    "id": "1",
    "username": "denilson",
    "email": "denilson@email.com"

    }

### Rota de token

#### Rota <http://127.0.0.1:8000/token/>

***Observações: Para gerar um token é necessário fornecer as credenciais de um usuário cadastrado na base de dados, juntamente com os seus dados corretos***

#### POST
  
Body:

    {

    "username": "denilson",
    "password": "1234567"
  
    }

Response:

    {

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjQzMDQ2NywiaWF0IjoxNzI2MzQ0MDY3LCJqdGkiOiI3NmFmMjhkYjA1MDE0ZTNlODA0MjA0OTdjNDZiMzNmMiIsInVzZXJfaWQiOjF9.ajAaOgIOLr85VbTvsqpa8Ejl8cEdjOOsN6popEwYcHI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NTE2ODY3LCJpYXQiOjE3MjYzNDQwNjcsImp0aSI6Ijk2NTU3ZWU3YzU2OTQyYzU5YjU2ODE0OGY2YWE0Y2Q1IiwidXNlcl9pZCI6MX0.OzXUryc57SFz98DZl9y5TwtQcTPGBWfjKHik7a7OZuk"

    }

A resposta correspode a dois tokens, um access de curta duração e um refresh de longa durção, que será utilizado para gerar um outro token de acess.

#### POST <http://127.0.0.1:8000/token/refresh/>

  ***Observações: Quando o token expira é necessário fazer o refresh do mesmo, e é nessa rota que conseguimos fazer o refresh**
  
  Insira o token de longa duração que é obtido na response da rota <http://127.0.0.1:8000/token/>
  
  Body:

    {

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjQzMDQ2NywiaWF0IjoxNzI2MzQ0MDY3LCJqdGkiOiI3NmFmMjhkYjA1MDE0ZTNlODA0MjA0OTdjNDZiMzNmMiIsInVzZXJfaWQiOjF9.ajAaOgIOLr85VbTvsqpa8Ejl8cEdjOOsN6popEwYcHI"
    
    }

Response:

Gerará um novo token access.

    {

    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NTE2ODY3LCJpYXQiOjE3MjYzNDQwNjcsImp0aSI6Ijk2NTU3ZWU3YzU2OTQyYzU5YjU2ODE0OGY2YWE0Y2Q1IiwidXNlcl9pZCI6MX0.OzXUryc57SFz98DZl9y5TwtQcTPGBWfjKHik7a7OZRTY&78k"
    
    }

### Rota <http://127.0.0.1:8000/tasks/>

***Observações: Para acessar essa rota é necessario que seja feita a autenticação do usuário com o JWT access gerado, tabém preste atenção no periodo de expiração do jwt, está configurado para dois dias***

Para autenticar o usuário no Insomnia siga os seguintes passos

1. Vá em Auth
2. Click em Inherit from parent
3. Depois selecione Bearer Token
4. Certifique-se que o checkbox ENABLED esteja selecionado
5. Cole o jwt access gerado na rota de token, no campo ***TOKEN***

#### POST <http://127.0.0.1:8000/tasks/>

***Observações:**

1. Os campos title e date são obrigatórios;
2. Os campo title deve ser unico, na data e no usuário que ele foi criado, ou seja se o evento com mesmo titulo for criado em dias diferentes, ou por outro outro usuário no mesmo dia, ele será criado normalmente;
3. Os campos time_start e time_end são correspondente ao horário do evento, onde correspondem ao início e fim respectivamente, eles também não podem serem iguais;
4. Quando os horários não são fornecidos, o evento é adotado como o dia inteiro;
5. A tarefa ficará vinculada ao usuário autenticado;
6. google_event_id é o id do evento gerado no google calendar;
7. É possível fazer consultas baseados em textos compostos pelo título.

Body:

    {
        "title": "Trabalho Engenharia de Software",
        "description": "Trabalho para amanhã",
        "date": "2024-09-12",
        "time_start": "09:12:20",
        "time_end": "22:10:10"
    }

Response:

    {
        "id": 1,
        "title": "Trabalho Engenharia de Software",
        "description": "Trabalho para amanhã",
        "date": "2024-09-12",
        "time_start": "09:12:21",
        "time_end":  "22:10:10",
        "google_event_id": "kl8gtepmfa1dq2r4s2lmetp72s",
        "user": {
            "id": 1,
            "username": "denilson"
        }
    }

 ***Criando tarefas apenas com o title e date**

Body:

    {
        "title": "Trabalho de Matemática",
        "date": "2024-09-13"
    }

Response:

    {
        "id": 2,
        "title": "Trabalho de Matemática",
        "description": "",
        "date": "2024-09-13",
        "time_start": "00:00:00",
        "time_end": "23:59:59",
        "google_event_id": "k0h0j9lmrgkmeo302f7vn49jo8",
        "user": {
            "id": 1,
            "username": "denilson"
        }
}

#### GET <http://127.0.0.1:8000/tasks/>

***Buscando todas as tarefas criadas ao usuário autenticado**

Response:

        [
            {
                "id": 1,
                "title": "Trabalho Engenharia de Software",
                "description": "Trabalho para amanhã",
                "date": "2024-09-12",
                "time_start": "09:12:21",
                "time_end":  "22:10:10",
                "google_event_id": "kl8gtepmfa1dq2r4s2lmetp72s",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }  ,
            {
                "id": 2,
                "title": "Trabalho de Matemática",
                "description": "",
                "date": "2024-09-13",
                "time_start": "00:00:00",
                "time_end": "23:59:59",
                "google_event_id": "k0h0j9lmrgkmeo302f7vn49jo8",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }
        ]

#### GET <http://127.0.0.1:8000/tasks/2/>

***Buscando tarefa pelo id**

Forneça o id da tarefa no final da rota, lembre-se de colocar a "***/*** " no final.

Response:

    {
        "id": 2,
        "title": "Trabalho de Matemática",
        "description": null,
        "date": "2024-09-13",
        "time_start": "00:00:00",
        "time_end": "23:59:59",
        "google_event_id": "k0h0j9lmrgkmeo302f7vn49jo8",
        "user": {
            "id": 1,
            "username": "denilson"
        }
    }

#### GET <http://127.0.0.1:8000/tasks/?start_date=2024-09-08&end_date=2024-09-13>

***Buscando tarefas baseada em períodos**

Forneça os queryparams start_date e end_date, quando querer fazer consultas em um intervalo de período, já quando querer fazer consultas apenas em um dia específico basta passar a querystring star_date.

Response:

        [
            
            {
                "id": 1,
                "title": "Trabalho de engenharia de software",
                "description": "Trabalho para amanhã",
                "date": "2024-09-08",
                "time_start": "09:30:20",
                "time_end": "22:30:20",
                "google_event_id": "oh22rsscprlurobhhlt7non34f5",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            },
            {
                "id": 2,
                "title": "Trabalho de Matemática",
                "description": "",
                "date": "2024-09-13",
                "time_start": "00:00:00",
                "time_end": "23:59:59",
                "google_event_id": "k0h0j9lmrgkmeo302f7vn49jo8",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }
            {
                "id": 3,
                "title": "Trabalho de POO",
                "description": "Trabalho para amanhã",
                "date": "2024-09-13",
                "time_start": "09:30:20",
                "time_end": "10:30:30",
                "google_event_id":  "oh22rsscprlurobhhlt7non2f4",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }

        ]

#### GET <<http://127.0.0.1:8000/tasks/?title=Trabalho> de POO>

***Buscas baseadas em titulos**

Response:

    [
        {
                "id": 3,
                "title": "Trabalho de POO",
                "description": "Trabalho para amanhã",
                "date": "2024-09-13",
                "time_start": "09:30:20",
                "time_end": "10:30:30",
                "google_event_id":  "oh22rsscprlurobhhlt7non2f4",
                "user": {
                    "id": 1,
                    "username": "denilson"
        }
            }
    ]

#### PUT <http://127.0.0.1:8000/tasks/2/>

***Observções**

1. Foneça o id da tarefa que deseja alterar;
2. Os campos users e google_event_id são read_only, ou seja não podem ser alterados;
3. Todos os outros campos podem serem alterados, porém não vão serem alteradas na agenda.

Body:

        {
            "title": "Trabalho de Redes",
            "date": "2024-09-15",
        }

Response:

         {
                "id": 2,
                "title": "Trabalho de Redes",
                "description": "Trabalho para amanhã",
                "date": "2024-09-15",
                "time_start": "09:30:15",
                "time_end": "22:30:20",
                "google_event_id": "oh22rsscprlurobhhlt7noi092",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }

#### DELETE <http://127.0.0.1:8000/tasks/2/>

***Observações: Passe na url o parâmetro id da tarefa que deseja deletar**

Response:

        {
            "detail": "Task deleted"
        }{
                "id": 2,
                "title": "Trabalho de Matemática",
                "description": "",
                "date": "2024-09-13",
                "time_start": "00:00:00",
                "time_end": "23:59:59",
                "google_event_id": "k0h0j9lmrgkmeo302f7vn49jo8",
                "user": {
                    "id": 1,
                    "username": "denilson"
                }
            }
