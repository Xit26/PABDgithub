#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(curso, matricula, senha, data_nasc):
    db.cur.execute("""
                   INSERT into public.tbUsers (curso, matricula, senha, data_nasc)
                   VALUES ('%s','%s','%s','%s')
                   """ % (curso, int(matricula), senha, data_nasc))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbUsers
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#funcão para excluir registro no banco de dados
def deletar(matricula):
    db.cur.execute("""
            Delete FROM tbUsers Where matricula = '%s'
    """ % (int(matricula)))
    db.con.commit()

#função para editar registro no banco de dados
def alterar(curso, matricula, senha, data_nasc):
    data = db.cur.execute("""
            UPDATE tbUsers 
            SET curso='%s', matricula='%s', senha='%s', data_nasc='%s' 
            WHERE matricula = '%s'
    """ % (curso, int(matricula), senha, data_nasc, int(matricula)))
    db.con.commit()
    return data