import oracledb
from models import Usuario, Relatorio, Regiao


class Repositorio():
    def __init__(self):
        self.usuario = "RM556864"
        self.senha = "111005"
        self.db_path= "oracle.fiap.com.br:1521/orcl"
        
    def gerar_conexao_db(self):
        con = oracledb.connect(
            user=self.usuario,
            password=self.senha,
            dsn=self.db_path)
        return con

    def gravar_db(self, usuario : Usuario , relatorio : Relatorio) -> bool:
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_usu = """INSERT INTO usuario (id_usu, email_usu, senha_usu, consumo_men, area_desejada, nome_usu, Regiao_id_reg, Relatorio_id_relatorio) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"""
        sql_rel = """INSERT INTO relatorio (id_relatorio, qtnd_pain, potencia_total, custo_total, economia_mensal, payback, energia_mes) VALUES (:1, :2, :3, :4, :5, :6, :7)"""
        try:
            cursor.execute(sql_usu, (usuario.id_user, usuario.email_user, usuario.senha_user, usuario.consumo_men, usuario.area_desejada, usuario.nome_usuario, usuario.regiao_fk, usuario.relatorio_fk))

            cursor.execute(sql_rel, (relatorio.id_relatorio, relatorio.qtnd_painel, relatorio.potencia_total,relatorio.custo_total, relatorio.economia_mensal, relatorio.payback, relatorio.energia_mes))
            conexao.commit()
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return True

    def ler_db_usuario(self):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql = """SELECT * FROM usuario"""
        try:
            cursor.execute(sql)
            resultado = []
            for dados in cursor:
                resultado.append(dados)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado
    
    def ler_db_regiao(self):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql = """SELECT * FROM regiao"""
        try:
            cursor.execute(sql)
            resultado = []
            for dados in cursor:
                resultado.append(dados)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado
        

    def ler_db_relatorio(self):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql = """SELECT * FROM relatorio"""
        try:
            cursor.execute(sql)
            resultado = []
            for dados in cursor:
                resultado.append(dados)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado

    
    def procurar_db(self, id_procurado_usuario ):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_user = """SELECT * FROM usuario WHERE id_usu LIKE :1"""
        sql_rel = """SELECT * FROM relatorio WHERE id_relatorio LIKE :1"""
        try:
            resultado = []
            cursor.execute(sql_user, (id_procurado_usuario,))            
            for dados in cursor:
                resultado.append(dados)
            id_procurado_relatorio =  cursor[0][-1]
                
            cursor.execute(sql_rel, (id_procurado_relatorio,))
            for dados in cursor:
                resultado.append(dados)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado

    def update_db (self, usuario : Usuario , relatorio : Relatorio, id_clie : int):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_user = """UPDATE usuario SET email_usu = :1, senha_usu = :2, consumo_men = :3, area_desejada = :4, nome_usu = :5, Regiao_id_reg = :6 WHERE id_cliente = :7"""
        sql_end = """UPDATE relatorio SET qtnd_pain = :1, potencial_total =:2, custo_total =:3 , economia_mensal =:4, payback = :5, energia_mes = :6  WHERE id_cliente = :7"""
        try:
            cursor.execute(sql_user, (usuario.id_user, usuario.email_user, usuario.senha_user, usuario.consumo_men, usuario.area_desejada, usuario.nome_usuario, usuario.regiao_fk))
            conexao.commit()
            # Fazer o negocio para procurar o id
            cursor.execute(sql_end, (relatorio.qtnd_painel, relatorio.potencia_total, relatorio.custo_total, relatorio.economia_mensal, relatorio.payback, relatorio.energia_mes, relatorio.id_relatorio))
            conexao.commit()
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def deletar_end(self, id):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql = """DELETE FROM endereco WHERE id_cliente = :1"""
        try:
            cursor.execute(sql, (id,))
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.commit()
        conexao.close()
        return True
    
    def deletar_db(self, id_alvo):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql = """DELETE FROM cliente WHERE id_cliente = :1"""
        self.deletar_end(id_alvo)
        try:
            cursor.execute(sql, (id_alvo,))
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.commit()
        conexao.close()
        return True