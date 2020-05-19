## Entenda Flask com uma visão Full-Stack

---

![](/home/rsl/Documents/GITHUB/Kuaa-Mbo-e/tecnologia/programacao/Python/Flask/Flask_1/image/LOGO_FLASK_1.png)

---

# O que é Flask?

**Flask** é um web-framework desenvolvido em **Python**, sendo constituído pelas bibliotecas:

-  (**Jinja2**) - gerencia dinâmicamente os arquivos **HTML** existentes no projeto. Estes arquivos são responsáveis pela interface gráfica do Web App (**Front-End**).
-  (**Werkzeug**) - uma biblioteca orientada para desenvolvimento de programas Web seguindo o protocolo Python **WSGI** (**Web Server Gateway Interface**), responsável pelo controle e mapeamento de **rotas** que comunicam cliente-servidor da aplicação.

 Não se engane com esta estrutura minimalista do **Flask**, pois ela está diretamente relacionada a eficiência da biblioteca. Esta característica proporciona **flexibilidade** na utilização de diferentes bancos de dados (DB - database) que irão compor o **Back-End** do seu programa. Alguns DB's compatíveis com o **Flask**:



- **MongoDB** (MongoDB) -- Database NoSQL

- **DynamoDB** (Amazon-AWS) -- Database NoSQL

- **MySQL** (Oracle) -- Database SQL

- **PostgreSQL** (PostgreSQL) -- Database SQL                                



O seu **MVP** pode se tornar um grande negócio com simplicidade e rapidez utilizando o **Flask**.  Em paralelo, a utilização para o ensino de desenvolvimento web, é bastante indicada, pois disponibiliza em poucas linhas de código um aplicativo funcional, tornando a curva de aprendizado mais amena comparando com o Django, por exemplo. Sendo assim , nada melhor do que um exemplo para explicar a tecnologia não é? Utilizaremos uma abordagem "**Full-Stack**" do **Flask**, visando uma melhor consolidação do conhecimento. 

O arquivo 1 (**app.py**) é a aplicação **Flask** e o arquivo 2  o **template** para  comunicação com o usuário. Este template poderá estar rodando no seu navegador favorito, como o Google Chrome (**Client**) por exemplo. As informações enviadas pelo cliente (navegador) através de uma requisição (***request***) serão interpretadas e respondidas pela aplicação **Flask**. O retorno da informação para tela do seu dispositível móvel será a resposta da aplicação (***Response***). O design da nossa aplicação para este tutorial, é demonstrado abaixo na Figura 1 e nos códigos 1,2:



https://medium.com/@rodrigo.schmidt.lucchesi/flask-full-stack-5144b5e9ee4d

Figura 1 – Design do diretório raiz para este tutorial

https://medium.com/@rodrigo.schmidt.lucchesi/flask-full-stack-5144b5e9ee4d?sk=43c0d3a164267e9da327f2f55c435587

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



Código 1 - Código Flask da aplicação responsável pelo Back-End

### 

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

Código 2 - Código HTML responsável pelo Front-End





O mecanismo de comunicação entre os dois arquivos (Python e HTML) será através do Protocolo **HTTP**, métodos GET e POST. Estes são ilustrados na Figura 2:



![](/home/rsl/Documents/GITHUB/Kuaa-Mbo-e/tecnologia/programacao/Python/Flask/Flask_1/image/First_Flask.png)

Figura 2 - Comunicação HTTP entre os arquivos Python e HTML



---



# 1 -> Inicialização da aplicação Flask

 

```python
from flask import Flask, render_template, request
 # (1)
app = Flask(__name__) # Instância Flask
           # (2)
```

Código 3 - Inicialização do app Flask



Nesta parte ocorre a inicialização da aplicação **Flask**. Os módulos (**Flask**, **render_template**, **request**) são importados para que a aplicação tenha os pré-requisitos necessários para nosso tutorial (**1**). Os métodos **render_template** e **request** serão detalhados no próximo passo. Vamos admitir que nesta parte estes dois não são importantes para o funcionamento do app : )

Sendo assim, primeiramente cria-se a instância **Flask** dentro da estrutura raiz do nosso aplicativo (**2**). As rotas estarão definidas dentro deste design. Para entendermos o que significa este “objeto”  **Flask**, os parâmetros do módulo são descritos abaixo. Para maior informação:

[flask.Flask]: https://flask.palletsprojects.com/en/1.1.x/api/	"Flask-API"



`class flask.Flask`(*import_name*, *static_url_path=None*, *static_folder='static'*, *static_host=None*, *host_matching=False*, *subdomain_matching=False*, *template_folder='templates'*, *instance_path=None*, *instance_relative_config=False*, *root_path=None*)



O objeto ou instância **Flask**, é o nosso maestro que conduzirá o fluxo de dados seguindo o protocolo **WSGI**. 



> DICA: O **Flask** utiliza este parâmetro ____name____  para determinar o diretório raiz da aplicação, sendo usado futuramente para a procura de outros arquivos utilizados na execução do nosso código



---

# 2 -> Rotas -   Endpoint → Request →  Response



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

Código 4 - Rota Flask para o exemplo do tutorial



A estrutura **@app.route( )** chama-se ***endpoint decorator*.** Para cada página da aplicação web, o **Flask** atribui uma função em que será executada quando este recurso for requisitado. Sendo assim, os **decorators** atuam na adição de funcionalidades extras para funções importadas de bibliotecas pessoais ou de terceiros, visando não alterar a estrutura original destas. 

Quando utiliza-se do sistema de roteamento da biblioteca **Werkzeug** **url_map.add(...) **, o mapeamento da função responsável pelo **endpoint** requisitado ocorre. A combinação **endpoint + função** responsável, chama-se ***view function***. O método **route( )** do Flask realiza a mesma combinação. Esta explicação é exemplificada no código:

```python
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

Código 5 - Comparação da regra de rotemaneto Flask x Werkzeug





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

No exemplo acima, verifica-se que a comunicação cliente-servidor seguirá diferentes rotas para acessar o mesmo recurso. Os dados (**o estado**) do sistema serão tratados dentro de uma única view function - **pagina_inicial( )** . Sendo assim, diferentes **endpoints** poderão acessar o mesmo recurso criando diferentes rotas. Cabe ao programador desenvolver estas com eficiência no seu app, evitando futuras dores de cabeça com o Front-End : )







Dando seguimento ao entendimento do sistema de rotemento **Flask**, o método request é utilzado para obter dados vindos da comunicação HTTP. Este possui alguns métodos específicos no protocolo. Vamos utilizar uma analogia com o mecanismo CRUD e os métodos existentes:

```python
if request.method ...
```

- Create – POST (Cria um novo registro no banco de dados)
- Read   - GET  (Obtém uma informação do sistema sem alterar os estado do mesmo)
- Update - PATCH & POST (Atualiza um registro no banco de dados)
- Delete – DELETE  (Deleta um registro no banco de dados)



Se o usuário não digitar nenhum argumento dentro do formulário da página inicial, o método **HTTP** disparado pela rota será o **GET** ao contrário se o formulário for preenchido e o botão enviar clicado o método **POST** será acionado. Abaixo na Figura 3 verificamos os códigos **Python** e **HTML** disparados para o método **GET**, junto com a página web retornada pelo método.



![](/home/rsl/Documents/GITHUB/Kuaa-Mbo-e/tecnologia/programacao/Python/Flask/Flask_1/image/GET.png)

Figura 3 - Método GET acionado e a lógica ocorrida



Na segunda condição da rota Flask, o método **POST** será ativado. A informação do texto com o nome de variável "**entrada**" será interpretado pela **view function** **pagina_inicial( )** utilizando a estrutura:

```python
formulario_preenchido_pelo_usuario = request.form.get('entrada',"")
frase_para_encaminhar_para_tela = formulario_preenchido_pelo_usuario
```

Ocorre uma superposição de variável (**frase_para_encaminhar_para_tela)**. Cabe salientar que esta redundância foi utilizada para fins didáticos, atribuindo o mesmo valor lido pelo request.forms.get(). O retorno do método **POST** será através de uma resposta (**response**) do tipo renderizar um arquivo **HTML** (**render_template**) junto com os dados obtidos dentro da função. Para maiores informações deste método, segue o link :

[flask.Flask.render_template]: https://flask.palletsprojects.com/en/1.1.x/api/	"render_template"



![](/home/rsl/Documents/GITHUB/Kuaa-Mbo-e/tecnologia/programacao/Python/Flask/Flask_1/image/POST.png)

Figura 3 - Método POST acionado e a lógica ocorrida



## 3 -> Rodando a aplicação em um servidor local



```python
if __name__ == "__main__": (1)
  app.run(debug=True) (2)
```

Código 6 - Servidor local Flask



Tendo a aplicação estruturada, a instância **app** possui um método chamado    **run( )** que executa o servidor integrado do **Flask** para desenvolvimento ou produção. A parte do Código 6:

`if __name__ == "__main__":` 

... é utilizada para confirmar que o servidor será iniciado somente quando o **app.py** for executado. Quando ocorrer esta inicialização, a aplicação entra em um ***loop*** contínuo até que seja interrompido pelo comando **CTRL+C** do seu teclado, por exemplo. Existem outros argumentos para esta função **run( )**:

`run(host=None, port=None, debug=None, load_dotenv=True, **options)`

Cabe salientar, que durante o desenvolviemento é conveniente a utilização do argumento `debug=True`, o qual habilita um debugger para o contole dos erros do seu software, sendo estes impressos no navegador. Um reloader para reiniciar o servidor também é ativado com este parâmetro, caso ocorra alguma mudança no seu programa e você não tenha que rodar o código novamente no terminal do seu sistema operacional. Importante saber que este atributo deve ser nulo durante o **período de produção** do app. Isto evita que usuários ou prováveis hackers descubram as brechas do seu sistema ; )



Para teste e estudo junto com o texto, o código utilizado neste tutorial encontra-se no Github em uma estrutura Flask e Jupyter notebook, este último atuando como um caderno iterativo:

https://github.com/rodrigo-schmidt-lucchesi-85/Kuaa-Mbo-e/tree/master/tecnologia/programacao/Python/Flask/Flask_1

Agradeço pela atenção de todos e fico a disposição para maiores dúvidas.

### Happy coding : )

---



**REFERÊNCIAS**:

GRINBERG, Miguel. **Flask web development: developing web applications with python**. " O'Reilly Media, Inc.", 2018.

https://flask.palletsprojects.com/en/1.1.x/

https://flask.palletsprojects.com/en/1.1.x/api/



### 