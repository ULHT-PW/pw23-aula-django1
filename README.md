# Aula #1 de Django
* Web app criada na aula de 8.5.2022 de Programação Web

### Passos para lançar e editar a aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue este repositório com o comando `git clone https://github.com/ULHT-PW-2020-21/pw-django-01` 
1. Entre na pasta  `cd pw-django-01`
1. Se não tiver, instale o django `python -m pip install django`
1. Lance a aplicação no browser com o comando `python manage.py runserver`. 
1. Tem disponíveis as aplicações hello no link `http://127.0.0.1:8000/hello/` e pw no link `http://127.0.0.1:8000/pw/` 
1. abra a pasta com o VSCode, para a explorar, ou com o comando `code .`

### Passos para brincar e criar uma nóva página na aplicação
1. na pasta `website\templates\pw` crie uma página HTML correspondente para ser renderizada, extendendo a base.html (veja como é feito nas outras páginas)
2. no ficheiro `views.py` crie uma nova função que renderize a nova página
3. no ficheiro `website\urls.py` crie um novo `path` para o novo URL
4. no ficheiro `layout.html` (que está na pasta `website\templates\website`) atualize o menu de navegação, inlcuindo um link para a nova página
