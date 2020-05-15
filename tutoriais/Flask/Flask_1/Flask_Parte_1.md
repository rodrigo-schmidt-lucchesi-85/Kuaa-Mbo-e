# Um guia para entender Flask... ...detalhadamente

![](/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/flask_terminal.png)







---

# O que é Flask?

Flask é um web-framework desenvolvido em Python, com a seguintes bibliotecas:

-  (**Jinja2**) para gerenciar dinamicamente os arquivos **HTML** do código, responsáveis pela interface gráfica  (**Front-End**) do aplicativo

- (**Werkzeug**) focada para aplicações web seguindo o protocolo Python **WSGI** (**Web Server Gateway Interface**), responsável pelo gerenciamento e mapeamento de **rotas** na comunicação cliente - servidor

Não se engane com a estrutura compacta do **Flask**, pois seu atributo de **modularidade** proporciona **flexibilidade** para escolher diferentes bancos de dados como alguns exemplos abaixo:





- MongoDB (MongoDB) -- Database NoSQL

- DynamoDB (Amazon-AWS) -- Database NoSQL

- MySQL (Oracle) -- Database SQL

- PostgreSQL (PostgreSQL) -- Database SQL

  





O seu produto final de sua startup (**MVP**) pode se tornar um grande negócio com simplicidade e rapidez. O **Flask**  auxilia também no ensino, disponibilizando em poucas linhas de código um aplicativo funcional para o aprendizado em desenvolvimento web com **Python**.

Sendo assim , nada melhor do que um exemplo para explicar a tecnologia não é?
Iremos usar dois arquivos para o tutorial "Full-Stack" do Flask, seguindo a estrutura do diretório abaixo:







#### ├── app.py (arquivo 1)

#### └── templates

####     └── pagina_inicial.html (arquivo 2)



Figura 1 - Estrutura de um diretório de uma aplicação Flask







O arquivo **1** é a nossa aplicação **Flask** e o **2** será o nosso **template** para a comunicação com o usuário que estará utilizando um navegador como o Google Chrome (**Client**) por exemplo, em que as informçãoes enviadas pelo mesmo (**Request**) serão interpretadas e respondidas pela aplicação **Flask** , imprimindo na tela do seu computador a resposta programada (**Response**). 

#### Não se esqueça:







> # O Flask procura por padrão os templates na pasta ***templates***







### Flask app.py (Back-End):

```python
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    if request.method == 'POST':
        formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
        frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
        return render_template('pagina_inicial.html', dados=frase_para_encaminhar_para_tela)
    else:
        frase_para_encaminhar_para_tela = 'Pythonista!'
        return render_template('pagina_inicial.html',
                               dados=frase_para_encaminhar_para_tela)


if __name__ == "__main__":
    app.run()
```







### Jinja2 template (Front-End)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jinja template</title>
</head>

<body>
    <!-- Jinja object -->
    <p>Olá {{ dados }}</p> 
    <form method="POST">
        <input type="text" name="entrada" value="Insira seu nome"><br>
        <input type="submit" value="Envie">
    </form> 
</body>

</html>
```



O mecanismo de comunicação entre os dois arquivos (Python e HTML) será através do Protocolo **HTTP**.




<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/web_app.jpg" style="zoom:300%;" />

Figura 1 - Comunicação HTTP entre os arquivos Python e HTML







---

- # Inicialização da aplicação Flask

   

```python
from flask import Flask, render_template, request
app = Flask(__name__) # Instância Flask
```

Nesta parte ocorre a inicialização da aplicação **Flask**. Os módulos (**Flask**, **render_template**, **request**) são importados para que a aplicação tenha os pré-requisitos para estar funcionando. Primeiro cria-se a instância **Flask** dentro do nosso módulo *main*, onde as rotas estarão definidas. Os parâmetros deste método são:



`class flask.Flask`(*import_name*, *static_url_path=None*, *static_folder='static'*, *static_host=None*, *host_matching=False*, *subdomain_matching=False*, *template_folder='templates'*, *instance_path=None*, *instance_relative_config=False*, *root_path=None*)



O objeto ou instância **Flask**, implementará a nossa aplicação **WSGI**. Todo o fluxo de dados dentro do nosso **web-app** circularão por este "controlador". 



> DICA: O Flask utiliza este parâmetro __name__ para determinar o diretório raiz da aplicação, usando futuramente na procura dos outros arquivos utilizados na execução do app





---

- # Rotas (Request & Response)



```python
@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    if request.method == 'POST':
        formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
        frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
        return render_template('pagina_inicial.html',           dados=frase_para_encaminhar_para_tela)
    else:
        frase_para_encaminhar_para_tela = 'Pythonista!'
        return render_template('pagina_inicial.html',
                               dados=frase_para_encaminhar_para_tela)
```





A estrutura **@app.route()** chama-se **endpoint decorator.** Cada página da aplicação web, o Flask atribui uma função em que será executada quando este **endpoint** for requisitado. Sendo assim os **decorators** podem ser utilizados para adcionar mais funcionalidades para as funções em que você importa de uma biblioteca pessoal ou de terceiros, sem modificar a estrutura original da mesma. Quando você utiliza o sistema de roteamento da biblioteca **Werkzeug**  os métodos **url_map.add(...) ** faz o mapeamento da função responsável pelo **endpoint** (***view function***). O método route( ) irá realizar a mesma combinação como mostrado abaixo com a utilização da biblioteca **Werkzeug** explicitamente:





```python
from flask import Flask, render_template
from werkzeug.routing import Rule


#@app.route('/', methods=['GET', 'POST'])
#def pagina_inicial():

app = Flask(__name__)
app.url_map.add(Rule('/', endpoint='pagina_inicial')) # Regra de rotemanto
    
@app.endpoint('pagina_inicial')
def pagina_inicial():
    frase_para_encaminhar_para_tela = 'Pythonista!'
    return render_template('pagina_inicial.html',
                               dados=frase_para_encaminhar_para_tela)
```







---

---

### "A arte do roteamento"

##### ... Diferentes endpoints podem acessar o mesmo recurso criando diferentes rotas através da mesma view function ...

```python
rota_1 = '/' # endpoint da rota 1
rota_2 = '/home' # endpoint da rota 2

@app.route(rota_1, methods=['GET', 'POST']) # rota 1
@app.route(rota_2, methods=['GET', 'POST']) # rota 2
def pagina_inicial():
    if request.method == 'POST':
        formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
        frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
        return render_template('pagina_inicial.html', dados=frase_para_encaminhar_para_tela)
    else:
        frase_para_encaminhar_para_tela = 'Pythonista!'
        return render_template('pagina_inicial.html',
                               dados=frase_para_encaminhar_para_tela)
```

No exemplo acima, verifica-se que a comunicação cliente-servidor seguirá diferentes rotas para acessar o mesmo recurso. Os dados (**o estado**) do sistema serão tratados dentro de uma única view function - **pagina_inicial( )** . Sendo assim, diferentes endpoints podem acessar o mesmo recurso criando diferentes rotas. Cabe ao programador desenvolver com eficiência as rotas do seu app, evitando futuras dores de cabeça : )



---

---







Voltando para a **view function** do aplicativo **Flask**, se o usuário não digitar nenhum argumento dentro do formulário da página inicial, o método **HTTP** disparado pela rota será o **GET**. Abaixo verificamos os códigos Python e HTML disparados por este método, junto com a página web retornada pelo mesmo.





#### ... Python _> HTML _> Web page ... (GET)

```Python
def pagina_inicial():
    
    #... se o método for GET
    
    else:
        frase_para_encaminhar_para_tela = 'Pythonista!'
        return render_template('pagina_inicial.html',
                               dados=frase_para_encaminhar_para_tela)
```

```html
...

<body>
    <!-- Jinja object -->
    <p>Olá {{ dados }}</p> 
    <form method="POST">
        <input type="text" name="entrada" value="Insira seu nome"><br>
        <input type="submit" value="Envie">
    </form> 
</body>

...
```

<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/GET.png"  />





---





Contudo, digitando no formulário e pressionando o botão envie, o método **POST** será disparado pela rota. A informação do texto com o nome de variável "**entrada**" será interpretado pela **view function** **pagina_inicial( )**, atribuindo este valor a variável **frase_para_encaminhar_para_tela**, retornando com uma resposta (**response**) do tipo renderizar um arquivo **HTML** junto com os dados obtidos dentro da função:







#### ... Python _> HTML _> Web page ... (POST)

```python
def pagina_inicial():
    # ... se o método for POST
    if request.method == 'POST':
        formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
        frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
        return render_template('pagina_inicial.html', dados=frase_para_encaminhar_para_tela)
    
    #...
```

<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/prePOST.png"  />

<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/POST.png"  />

<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/req_res.png" style="zoom: 150%;" />

Figura 2 - Mecanismo de uma comunicação cliente servidor (Método POST e GET)

---




- ## Rodando a aplicação em um servidor local

  

  
  
  ```python
  if __name__ == "__main__":
    app.run(debug=True)
  ```





A instância app possui um método chamdo **run( )** que executa o servidor integrado no **Flask**. A parte do código acima:

`if __name__ == "__main__":` 

... é utilizada para confirmar que o servidor web de desenvolvimento será iniciado somente quando o **app.py** for executado. Quando ocorrer esta inicialização, a aplicação entra em ***loop*** continuo até que seja interrompido pelo comando **CTRL+C** por exemplo do seu teclado. Existem diversos argumentos que podem ser atribuidos a este método **run( )**:

`run(host=None, port=None, debug=None, load_dotenv=True, **options)`

Cabe salientar, que durante o desenvolviemento é conveniente a utilização do argumento `debug=True`,
o qual habilita um debugger para o contole dos erros do seu código sendo impressos no navegador utilizado e um reloader para reiniciar o servidor se alguma mudança no programa for feita sem que ocorra uma interrupção do desenvolvimento. Importante saber que este atributo deve ser nulo durante ao **período de produção** do seu app (sendo utilizado por terceiros) , evitando que seus usuários ou prováveis hackers não descubram as brechas do seu sistema ; )



O código utilizado neste tutorial encontra-se no Github:

www.meusite.com



Agradeço pela atenção de todos e fico a disposição para maiores dúvidas.

### Happy coding : )