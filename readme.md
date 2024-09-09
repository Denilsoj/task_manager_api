# TaskManagerAPI

O taskManagerAPI se trata de uma **API**(**Interface de programação de aplicativo**) para o usuário organizar as atividades do dia à dia onde o mesmo pode criar uma nova tarefa, deletar e excluir a mesma, essa API é integrada com a API do google calendar, logo toda vez que o usuário adicionar, a mesma será adicionada na agenda vinculada com esta API, da mesma maneira se o mesmo deletar alguma tarefa, a mesma será removida da agenda vinculada a esta API.

## Tecnologias utilizadas

- Python 3.10
- Django 5.1.1
- Django Rest Framework 3.15.2
- Sqlite
- API Google Calendar

## Funcionalidades

**Adicicionar uma nova tarefa**, o usuário pode criar uma nova tarefa passando os parâmetro, title, description, date e time, onde apenas o titulo e datas são obrigatórios;

**Buscar tarefas**, o usuário pode buscar tarefas com base no ID, período de datas e títulos;

**Deletar tarefas** O usuário pode apagar tarefas fornecendo o ID da tarefa;

**Atualizar tarefa**, o usuário pode atualizar tarefas passando o ID da tarefa como parâmetro, porém essa atualização será ignorada no google calendar;
