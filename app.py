from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- BANCOS DE DADOS EM MEMÓRIA ---
usuarios_db = [
    {"id": 1, "nome": "Usuario 1", "email": "user1@example.com", "celular": "1234567890", "nivel": "Usuário"},
    {"id": 2, "nome": "Usuario 2", "email": "user2@example.com", "celular": "9876543210", "nivel": "Administrador"}
]

planos_db = [
    {"id": 1, "nome": "Minha Vida", "valor": "R$ 24,50/mês", "setor": "Norte / Sul", "desconto": "50%"},
    {"id": 2, "nome": "Minha História", "valor": "R$ 60,00/mês", "setor": "Leste Superior", "desconto": "70%"}
]

ingressos_db = [
    {"id": 1, "partida": "Corinthians x Palmeiras", "data": "2026-10-15", "estadio": "Neo Química Arena", "preco_base": "R$ 100,00"}
]

# --- ROTAS ---
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def index():
    return render_template("index.html")

# Usuários
@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios_listar.html", usuarios=usuarios_db)

@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        novo_id = len(usuarios_db) + 1
        usuarios_db.append({
            "id": novo_id,
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "celular": request.form.get("celular"),
            "nivel": request.form.get("nivel")
        })
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios_cadastrar.html")

# Planos
@app.route("/planos")
def listar_planos():
    return render_template("planos_listar.html", planos=planos_db)

@app.route("/planos/cadastrar", methods=["GET", "POST"])
def cadastrar_plano():
    if request.method == "POST":
        novo_id = len(planos_db) + 1
        planos_db.append({
            "id": novo_id,
            "nome": request.form.get("nome"),
            "valor": request.form.get("valor"),
            "setor": request.form.get("setor"),
            "desconto": request.form.get("desconto")
        })
        return redirect(url_for("listar_planos"))
    return render_template("planos_cadastrar.html")

# Ingressos
@app.route("/ingressos")
def listar_ingressos():
    return render_template("ingressos_listar.html", ingressos=ingressos_db)

@app.route("/ingressos/cadastrar", methods=["GET", "POST"])
def cadastrar_ingresso():
    if request.method == "POST":
        novo_id = len(ingressos_db) + 1
        ingressos_db.append({
            "id": novo_id,
            "partida": request.form.get("partida"),
            "data": request.form.get("data"),
            "estadio": request.form.get("estadio"),
            "preco_base": request.form.get("preco_base")
        })
        return redirect(url_for("listar_ingressos"))
    return render_template("ingressos_cadastrar.html")

if __name__ == "__main__":
    app.run(debug=True)