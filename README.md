# Questionario-Web

Questionário Web utilizando [Django](https://www.djangoproject.com/). Crie seu questionário com perguntas e alternativas e:

  - Tenha o controle de quantas pessoas responderam o seu questionário
  - Confira a alternativa mais votada para cada questão
  - Administre tudo numa plataforma fácil e intuitiva

### Instalação

Para utilizar o Questionário, instale a versão mais nova do [Python](https://www.python.org/), do [Git](https://git-scm.com/).

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

Inicialize o banco de dados, acessando o diretorio 'questionario-web' via terminal e digite o comando:
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

### Criando um superusuario
Com o servidor rodando, acesse o diretorio 'questionario-web' em outro terminal e digite:
```sh
(myenv) $ python manage.py createsuperuser
```
e crie seu usuario e senha. Esses dados serão utilizados para acesso ao Admin do Django.
### Acessando o Admin do Django
Com o superusuario criado, acesse o http://127.0.0.1:8000/admin/ em seu navegador. Caso tenha executado o servidor na porta 7000, por exemplo, digite http://127.0.0.1:7000/admin/
Digite o usuario e senha criados para ter acesso ao painel do Admin do Django.

### Utilizando o painel do Django
Para criar um questionário:
1. Clique em 'Questionários'
2. Clique em 'Adicionar Questionário'
3. Digite o título do Questionário
4. Digite o texto das pergunta. Para mais perguntas, clique em 'Adicionar outro(a) pergunta'
5. As perguntas já vem com uma imagem padrão. Para alterar clique em 'Escolher arquivo' na coluna imagem
6. Clique em 'Salvar'

Para criar alternativas, na tela inicial do painel:
1. Clique em 'Perguntas'
2. Clique na pergunta desejada
3. Digite o texto das alternativas
4. Clique em Salvar

### Visualizando o site
No painel do Django:
1. Clique em 'Ver o site'
2. Selecione o questionario desejado
3. Selecione uma alternativa para cada pergunta e ao final, clique em 'Enviar'
4. Visualize os resultados na tela seguinte

### Referências
Esse projeto foi basedo no [tutorial do Django](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) e no [tutorial da Django Girls](https://tutorial.djangogirls.org/pt/)