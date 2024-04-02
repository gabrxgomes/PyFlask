from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#podemos usar uma extensão do flask para usar o bootstrap

# 1 - criamos uma instancia da classe flask
app = Flask(__name__)


#definindo configurações
app.config['TITLE'] = "TEST TITLE"

#usando a ext do bootstrap sempre após a instanciação do meu app flask
Bootstrap(app) #meu app como parametro inicializado ali em cima
#o flask bootstrap nos oferece temas e templates, para usa-lo temos
#que criar uma nova pasta na raiz do nosso projeto chamada "templates"
#e o nosso template é nada mais nada menos que um html por exemplo
# e la em baixo na nossa função index retornamos uma lista mas podemos
#retornar um template


#criamos uma nova rota
@app.route("/")
#definindo uma função
def index():
    #vou criar uma lista
    products =  ["maçã", "tomate", "alface"]

    #posso retornar a nossa propria lista se quisermos passando o 
    #indice como parametro
    #return products[0]



    #correto é passar as variaveis explicitamente
    return render_template("index.html", products=products)


    #ma pratica so serve em desenvolvimento
    return render_template("index.html", **locals())

    #o parametro que retornamos como locals pode ser espaço
    #para retornarmos uma variavel apenas ou mais de uma, mas usando
    #o "**locals()" puxamos todas as variaveis locais existentes
    #para dentro do nosso template

#agora podemos executar o projeto com "flask run" que vai rodar
#na porta padrao localhost:5000

#posso rodar o flask em modo desenvolvimento para fazer build automatica

#FLASK_ENV=development flask run 
#so se eu estiver com ele corretamente habilitado


