from flask import Flask, render_template, request, redirect, session, flash
from service.mercado import Mercado
from service.trazer_precos import TrazPrecos
from service.tratar_dados import TratarDados
from service.mensagens import Mensagens
from service.admin import Admin
from service.usuario import Usuario


app = Flask(__name__)
app.secret_key = 'app-ficha-rpg'

titulo = 'App - Fichas RPG'
mercado = Mercado()
mensagens = Mensagens()
admin_sistema = Admin()
usuario = Usuario()
tratar_dados = TratarDados()

@app.route('/')
def pagina_inicial():
    session['admin_logado'] = None
    return render_template(
        'pagina_inicial.html', titulo=titulo)



if __name__ == "__main__":  # Para poder executar quando o arquivo não for importado
    app.run(debug=True)     # Para ir atualizando as modificações que o codigo faz no site
