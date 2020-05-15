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