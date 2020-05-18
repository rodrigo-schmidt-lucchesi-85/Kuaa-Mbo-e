# Um guia para entender Flask... ...detalhadamente

![](/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/flask_terminal.png)







---

# O que é Flask?

**Flask** é um web-framework desenvolvido em Python, sendo constituído pelas bibliotecas:

-  (**Jinja2**) - gerencia dinâmicamente os arquivos **HTML** existentes no projeto. Estes arquivos são responsáveis pela interface gráfica (**Front-End**) da aplicação.
- (**Werkzeug**) - uma biblioteca orientada para programas web seguindo o protocolo Python **WSGI** (**Web Server Gateway Interface**), responsável pela gestão e mapeamento de **rotas** para comunicação cliente-servidor da aplicação.

Não se engane com esta estrutura minimalista do **Flask**, pois está diretamente  relacionada a eficiência da biblioteca. Esta característica,por exemplo, proporciona **flexibilidade** para utilizar diferentes bancos de dados para o **Back-End** do seu programa. Alguns bancos de dados compatíveis com o **Flask**:



- **MongoDB** (MongoDB) -- Database NoSQL

- **DynamoDB** (Amazon-AWS) -- Database NoSQL

- **MySQL** (Oracle) -- Database SQL

- **PostgreSQL** (PostgreSQL) -- Database SQL                                **OK ATE AQUI**



O seu **MVP** pode se tornar um grande negócio com simplicidade e rapidez utilizando o **Flask**.  A utilização para o ensino de desenvolvimento web, é bastante indicada, pois disponibiliza em poucas linhas de código um aplicativo funcional, tornando a curva de aprendizado mais amena comparando com o Django. Sendo assim , nada melhor do que um exemplo para explicar a tecnologia não é? Utilizaremos uma abordagem "Full-Stack" do **Flask**, visando um melhor consolidação do conhecimento. O design da nossa aplicação para este tutorial, é demonstrado abaixo:



#### ├── app.py (arquivo 1)

#### └── templates

####     └── pagina_inicial.html (arquivo 2)



Figura 1 – Design do diretório raiz para este tutorial



O arquivo 1 (**app.py**) é a aplicação **Flask** e o arquivo 2  o **template** para  comunicação com o usuário. Este template poderá estar rodando no seu navegador favorito, como o Google Chrome (**Client**) por exemplo. As informações enviadas pelo cliente (navegador) através de uma requisição (***request***) serão interpretadas e respondidas pela aplicação **Flask**. O retorno da informação para tela do seu dispositível móvel será a resposta da aplicação (***Response***). 

#### Não se esqueça:



> # O Flask procura por padrão os arquivos HTML no diretório ***templates***





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





O mecanismo de comunicação entre os dois arquivos (Python e HTML) será através do Protocolo **HTTP**, métodos GET e POST.




<img src="/home/rsl/Documents/GITHUB/Logic-Rate/tutoriais/image/web_app.jpg" style="zoom:300%;" />

Figura 2 - Comunicação HTTP entre os arquivos Python e HTML







---

- # Inicialização da aplicação Flask

   

```python
from flask import Flask, render_template, request # (1)
app = Flask(__name__) # Instância Flask           # (2)
```

Nesta parte ocorre a inicialização da aplicação **Flask**. Os módulos (**Flask**, **render_template**, **request**) são importados para que a aplicação tenha os pré-requisitos necessários para nosso tutorial (1). Os métodos **render_template** e **request** serão detalhados no próximo passo. Vamos admitir que nesta parte estes dois não são importantes para o funcionamento do app : )

Sendo assim, primeiramente cria-se a instância **Flask** dentro da estrutura raiz do nosso aplicativo (2). As rotas estarão definidas dentro deste desing. Para entendermos o que signigica este “objeto” **Flask**, os parâmetros são descritos abaixo. Para maior informação (Link):



`class flask.Flask`(*import_name*, *static_url_path=None*, *static_folder='static'*, *static_host=None*, *host_matching=False*, *subdomain_matching=False*, *template_folder='templates'*, *instance_path=None*, *instance_relative_config=False*, *root_path=None*)



O objeto ou instância **Flask**, é o nosso maestro que conduzira o fluxo de dados seguindo o protocolo **WSGI**. 



> DICA: O **Flask** utiliza este parâmetro __name__ para determinar o diretório raiz da aplicação, sendo usado futuramente para a procura de outros arquivos utilizados para execução do nosso código



---

- # Rotas - mecanismo Endpoint → Request →  Response



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



A estrutura **@app.route()** chama-se **endpoint decorator.** Para cada página da aplicação web, o **Flask** atribui uma função em que será executada quando este recurso for requisitado. Sendo assim os **decorators** atuam na adição de funcionalidades extras para funções em que você importa de uma biblioteca pessoal ou de terceiros, visando não alterar a estrutura original destas. 

Quando você utiliza o sistema de roteamento da biblioteca **Werkzeug** **url_map.add(...) **, estes realizam o mapeamento da função responsável pelo **endpoint** requisitado, nomeando essa função de ***view function***. O método **route( )** realizará a mesma combinação.


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

No exemplo acima, verifica-se que a comunicação cliente-servidor seguirá diferentes rotas para acessar o mesmo recurso. Os dados (**o estado**) do sistema serão tratados dentro de uma única view function - **pagina_inicial( )** . Sendo assim, diferentes **endpoints** podem acessar o mesmo recurso criando diferentes rotas. Cabe ao programador desenvolver com eficiência as rotas do seu app, evitando futuras dores de cabeça : )



---

---


O método request é utilzado para capturarmos os dados vindos do navegador. Este possui alguns métodos específicos no protocolo HTTP. Vamos utilizar uma analogia com o mecanismo CRUD e os métodos existentes:

``` python
if request.method ...```

- Create – POST (Cria um novo registro no banco de dados)
- Read   - GET  (Obtém uma informação do sistema sem alterar os estado do mesmo)
- Update - PATCH & POST (Atualiza um registro no banco de dados)
- Delete – DELETE  (Deleta um registro no banco de dados)

Sendo assim, o método request identifica qual tipo de método está sendo requisitado, entrando dentro de uma estrutura condional do Python. Utilizando uma linguagem mais simples, se o usuário não digitar nenhum argumento dentro do formulário da página inicial, o método **HTTP** disparado pela rota será o **GET** ao contrário se preencher e clicar no botão enviar acionará o método POST. Abaixo verificamos os códigos **Python** e **HTML** disparados para o método GET, junto com a página web retornada pelo método.



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





Contudo, digitando no formulário e pressionando o botão envie como já mencionado, o método **POST** será ativado dentro da rota. A informação do texto com o nome de variável "**entrada**" será interpretado pela **view function** **pagina_inicial( )** pela função:

```python
formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
```

Ocorre a atribuição deste valor para variável **frase_para_encaminhar_para_tela**. Cabe salientar que há uma redundância nesta variável, atribuindo o mesmo valor lido pelo request.forms.get(). Esta estrutura foi utilizada para fins didáticos. O retorno do método POST será atrvés de uma resposta (**response**) do tipo renderizar um arquivo **HTML** (render_template) junto com os dados obtidos dentro da função. Para maiores informações deste método, segue o link ao lado:







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





Tendo a aplicação estruturada, a instância app possui um método chamado **run( )** que executa o servidor integrado ao **Flask** oara desenvolvimento e produção. A parte do código acima:

`if __name__ == "__main__":` 

... é utilizada para confirmar que o servidor será iniciado somente quando o **app.py** for executado. Quando ocorrer esta inicialização, a aplicação entra em um ***loop*** contínuo até que seja interrompido pelo comando **CTRL+C** do seu teclado, por exemplo. Existem outros argumentos para esta função **run( )**:

`run(host=None, port=None, debug=None, load_dotenv=True, **options)`

Cabe salientar, que durante o desenvolviemento é conveniente a utilização do argumento `debug=True`,
o qual habilita um debugger para o contole dos erros do seu software, sendo estes impressos no navegador. Um reloader para reiniciar o servidor também é ativado com este parâmetro, caso ocorra alguma mudança no seu programa e você não tenha que rodar o código novamente no terminal do seu sistema operacional. Importante saber que este atributo deve ser nulo durante o **período de produção** do app. Isto evita que usuários ou prováveis hackers descubram as brechas do seu sistema ; )



Para teste e estudo junto com o texto, o código utilizado neste tutorial encontra-se no Github em uma estrutura Flask e Jupyter notebook, este último atuando como um caderno iterativo:

www.meusite.com



Agradeço pela atenção de todos e fico a disposição para maiores dúvidas.

### Happy coding : )
