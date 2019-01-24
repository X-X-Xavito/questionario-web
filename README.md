# Questionario-Web

Questionário Web utilizando Django. Crie seu questionário com perguntas e alternativas e:

  - Tenha o controle de quantas pessoas responderam o seu questionário
  - Confira a alternativa mais votada para cada questão
  - Administre tudo numa plataforma fácil e intuitiva
### Instalação

Para utilizar o Questionário, instale a versão mais nova do [Python](https://www.python.org/), do [Django](https://www.djangoproject.com/) e do [Git](https://git-scm.com/).

Crie um diretório para o seu projeto em seu computador, acesse-o e execute o comando git clone para fazer uma cópia remota do projeto

```sh
$ git clone https://github.com/X-X-Xavito/questionario-web.git
```

Acesse o diretório 'questionario-web/' e instale um ambiente virtual(virtualenv) chamado de myenv

```sh
$ python3 -m venv myvenv
```
Depois acesse o ambiente virtual. O prefixo *myenv* irá aparecer no inicio do terminal:
- Windows
```sh
$ myvenv\Scripts\activate
```
- Linux e OS X
```sh
$ source myvenv/bin/activate
```
### requirements.txt
Acesse o diretório 'questionario-web/' e execute o comando abaixo para instalar todas as aplicações e libs do projeto:

```sh
(myvenv) ~$ pip install -r requirements.txt
```

### Banco de Dados

Inicialize o banco de dados, acessando o diretorio 'questionario-web' via terminal e digite os comandos:
```sh
(myenv) $ python manage.py makemigrations questionario
```
```sh
(myenv) $ python manage.py migrate
```

### Iniciando o servidor

Dentro do diretorio 'questionario-web', digite no terminal:
```sh
(myenv) $ python manage.py runserver
```
Isso irá rodar o servidor na porta 8000. Para rodar em outra porta, como a 7000, por exemplo, digite:
```sh
(myenv) $ python manage.py runserver 7000
```


