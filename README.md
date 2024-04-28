# Agenda de Telefone

Uma ramificação do repositório [Python-basico-avancado](https://github.com/agostin-afk/Python-basico-avancado)


A criação de um sistema simulando uma agenda telefônica com certo nível de verificação de dados e trabalhando com validações de usuários django




## Funcionalidades

- Cadastrar Usuários e contatos

- Lista de contatos

- Pesquisa totalmente funcional

- CRUD de contatos e usuários completo

## Instalação

Rode esses comandos no terminal da raiz do projeto:

```bash
python -m venv nome_ambienteVirtual
nome_ambienteVirtual/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py ceatesuperuser
python manage.py runserver
```
_para algumas funcionalidades é preciso criar um super usuario_:
```python manage.py createsuperuser```
    
## Bibliotecas

Com o ambiente virtual ativado, instale as seguintes dependências antes de rodar os comandos migrate:

```bash
asgiref==3.7.2
Django==5.0.2
Faker==24.2.0
pillow==10.2.0
python-dateutil==2.9.0.post0
six==1.16.0
sqlparse==0.4.4
tzdata==2024.1
```

## Tela inicial:
![Tela inicial da Agenda feita com Django](media_github\tela_inicial.png)


