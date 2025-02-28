from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Inicializa o Flask
app = Flask(__name__)

# Configura o banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Inicializa o SQLAlchemy
db = SQLAlchemy(app)
# Inicializa o Flask-Migrate
migrate = Migrate(app, db)


# Modelo da tabela de aniversários
class Aniversario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_aniversario = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(20))
    telefone = db.Column(db.String(20))


# Rota para cadastrar aniversários
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.json

    # Converte a data de aniversário para o formato correto
    data_aniversario = datetime.strptime(dados["data_aniversario"], "%Y-%m-%d").date()

    # Cria um novo registro no banco de dados
    novo_aniversario = Aniversario(
        nome=dados["nome"],
        data_aniversario=data_aniversario,
        email=dados["email"],
        telefone=dados["telefone"],
    )

    # Salva no banco de dados
    db.session.add(novo_aniversario)
    db.session.commit()

    return jsonify({"mensagem": "Aniversário cadastrado com sucesso!"}), 201


# Rota para listar aniversários
@app.route("/aniversarios", methods=["GET"])
def listar_aniversarios():
    aniversarios = Aniversario.query.all()
    resultado = []
    for aniversario in aniversarios:
        resultado.append(
            {
                "id": aniversario.id,
                "nome": aniversario.nome,
                "data_aniversario": aniversario.data_aniversario.strftime("%Y-%m-%d"),
                "email": aniversario.email,
                "telefone": aniversario.telefone,
            }
        )
    return jsonify(resultado), 200


# Cria o banco de dados e as tabelas
with app.app_context():
    db.create_all()

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
