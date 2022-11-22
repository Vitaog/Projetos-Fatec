from flask import Flask, render_template, request
import mariadb


def create_app():
    from app import routes
    routes.init_app(app)

    return app

try:
    connection = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3306,
        database = "contatos"
    )
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")

app = Flask(__name__)




@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/quemsomos")
def quem_somos():
    return render_template("quem-somos.html")

'''
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

'''


@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        connection.commit()
        return 'sucesso'
    return render_template('contato.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    cursor = connection.cursor()

    users = cursor.execute("SELECT * FROM contatos")

    if users !='':
        userDetails = cursor.fetchall()

        return render_template("users.html", userDetails=userDetails)