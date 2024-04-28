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
<div align= "center">
<img src="https://github.com/agostin-afk/agenda_django/assets/67163625/f0572f77-293a-4454-a784-a4e80272e0c5" width="800">
</div>


Caso não esteja logado essa será a tela inicial.
Os dados desse exemplo foram criados usando a biblioteca Faker.
<br></br>
## Quando logado e exemplos de funcionalidades:
#### - Tela quando efetuar o login:
<div align= "center">
<img src="https://github.com/agostin-afk/agenda_django/assets/67163625/819ffee0-29ce-440a-b95e-99702ac55b98" width="800">
</div>

<br></br>

### - Exemplo de pesquisa:

<div align= "center">
<img src="https://github.com/agostin-afk/agenda_django/assets/67163625/4643948e-3365-478a-81bc-91e31053a0e2" width="800">
</div>
<br></br>

### - Página de contato único:

<div align= "center">
<img src="https://github.com/agostin-afk/agenda_django/assets/67163625/184c6a87-7d49-44eb-9f74-dfec3f6f0549" width="800">
</div>
<br></br>

### - Página de criação de contato:

<div align= "center">
<img src="https://github.com/agostin-afk/agenda_django/assets/67163625/8da1fa3d-1ecb-40e5-986e-442a92140389" width="800">
</div>
<br></br>
