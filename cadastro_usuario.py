
import bcrypt

def listar_usuario(conexao):
    usuarios   = []
    cursor    = conexao.cursor()
    cursor.execute("select id, login  from usuario")
    registros = cursor.fetchall()
    for registro in registros:
        item  = {
            "id": registro[0],
            "login": registro[1],
        
        }
        usuarios.append(item)
    return usuarios

def inserir_usuario_db(conexao,login,senha):
    criptografia = bcrypt.gensalt()
    senha_criptografada = bcrypt.hashpw(senha.encode("utf-8"), criptografia)
    print(senha_criptografada)
    cursor = conexao.cursor()
    cursor.execute ("insert into usuario (login,senha) values (%s, %s)", (login, senha_criptografada))
    conexao.commit()

def alterar_usuario_db(conexao,id,login,senha):
    cursor     = conexao.cursor() 
    sql_update = "update usuario set login = %s, senha = %s where id = %s "
    dados      = (login,senha,id)
    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_usuario_db(conexao, id):
    cursor     = conexao.cursor() 
    sql_delete = "delete from usuario where id = %s"
    cursor.execute(sql_delete,[id])
    conexao.commit()

def consultar_usuario_por_id_db(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,login from usuario where id = %s",[id])
    registro = cursor.fetchone()
    item = {
        "id": registro[0],
        "login": registro[1]
    }
    return item

def verificar_login(conexao, login, senha):
    print(login)
    print(senha)
    cursor = conexao.cursor()
    cursor.execute(" select id, login, senha from usuario " + 
                   "where login = '" + login + "'")
    registro = cursor.fetchone()

    if registro is None:
        senha_do_banco = registro[2]
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        if bcrypt.checkpw(senha_do_banco, senha_criptografada):
            return "Login bem sucedido"
        else: 
            return "Login falhou, verifique o usuario e a senha" 
    
    else:
        return "Login falhou, verifique o usuario!"
    


   
