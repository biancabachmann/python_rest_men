from flask import Flask, jsonify, request

from cadastro_editora import inserir_editora_bd

from cadastro_usuario import (listar_usuario, inserir_usuario_db, alterar_usuario_db, deletar_usuario_db,consultar_usuario_por_id_db,verificar_login)

from cadastro_livro import (alterar, consultar, consultar_por_id, deletar,
                            inserir)

from cadastro_autor import listar_autores,inserir_autor_bd,alterar_autor_bd, deletar_autor_bd,consultar_autor_por_id_bd
from conexao import conecta_db

app = Flask(__name__)

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
   conexao = conecta_db()
   livros = consultar_por_id(conexao,id)
   return jsonify(livros)

@app.route("/livros", methods=["POST"])
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    id_editora = data["id_editora"]
    id_autor = data ["id_autor"]
    inserir(conexao,nome,id_editora,id_autor)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar(conexao,int(id),nome)
    return jsonify(data)


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    conexao = conecta_db()
    deletar(conexao,id)
    return jsonify({"message": "Livro deletado com sucesso" })


@app.route("/livros", methods=["GET"])
def listar_todos():
    conexao = conecta_db()
    livros = consultar(conexao)
    return jsonify(livros)

@app.route("/autores", methods=["GET"])
def listar_todos_autores():
    conexao = conecta_db()
    autores = listar_autores(conexao)
    return jsonify(autores)

@app.route("/autores", methods=["POST"])
def inserir_autor():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_autor_bd(conexao,nome)
    return jsonify(data)


@app.route("/autores/<int:id>", methods=["PUT"])
def update_autor(id):
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    alterar_autor_bd(conexao,int(id),nome)
    return jsonify(data)


@app.route("/autores/<int:id>", methods=["DELETE"])
def excluir_autor(id):
    conexao = conecta_db()
    deletar_autor_bd(conexao,id)
    return jsonify({"message": "Autor deletado com sucesso" })

@app.route("/autores/<int:id>", methods=["GET"])
def consultar_autor_por_id(id):
   conexao = conecta_db()
   autor = consultar_autor_por_id_bd(conexao,id)
   return jsonify(autor)


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuario(conexao)
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    inserir_usuario_db(conexao,login,senha)
    return jsonify(data)
 
@app.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    alterar_usuario_db(conexao,int(id), login , senha)
    return jsonify(data)

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    conexao = conecta_db()
    deletar_usuario_db(conexao,id)
    return jsonify({"message": "Usuario deletado com sucesso" })

@app.route("/usuarios/<int:id>", methods=["GET"])
def consultar_usuario_por_id(id):
   conexao = conecta_db()
   usuarios = consultar_usuario_por_id_db(conexao,id)
   return jsonify(usuarios)

@app.route("/autenticar", methods=["POST"])
def autenticar():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    print(login)
    print(senha)
    resultado = verificar_login(conexao,login,senha)
    return jsonify(resultado)

@app.route("/editoras", methods=["POST"])
def inserir_editoras():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_editora_bd(conexao,nome)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)