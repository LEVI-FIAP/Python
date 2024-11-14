import oracledb 
from models import Usuario, Relatorio
import visual

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
        sql_usu = """INSERT INTO usuario (id_usu, email, senha, NOME_USUARIO) VALUES (:1, :2, :3, :4)"""
        
        sql_rel = """INSERT INTO RELATORIO(ID_RELATORIO,CONSUMO_MENSAL,CONTA_LUZ,AREA_DESEJADA,QTD_PAINEIS,POTENCIA_TOTAL,CUSTO_INSTAL,ECONOMIA_MENSAL,PAYBACK,ID_USU,ID_REG) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10, :11)"""
        try:
            cursor.execute(sql_usu, (usuario.id_user, usuario.email_user, usuario.senha_user, usuario.nome_usuario))

            cursor.execute(sql_rel, (relatorio.id_relatorio, relatorio.consumo_mensal,relatorio.conta_luz, relatorio.area_desejada, relatorio.qtd_paineis, relatorio.potencia_total, relatorio.custo_instal, relatorio.economia_mensal, relatorio.payback, relatorio.id_usu, relatorio.id_reg))
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
            dados_users = cursor.fetchall()
            resultado.extend(dados_users)
            
            if dados_users:
                id_procurado_relatorio = dados_users[-1][0]
                
            cursor.execute(sql_rel, (id_procurado_relatorio,))
            dados_relatorio = cursor.fetchall()
            resultado.extend(dados_relatorio)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado

    def update_db (self, usuario : Usuario , relatorio : Relatorio, id_user : int, id_rel :int):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_user = """UPDATE usuario SET nome_usuario = :1, email = :2, senha = :3 WHERE id_usu = :4"""
        sql_end = """UPDATE relatorio SET consumo_mensal = :1, conta_luz = :2, area_desejada = :3, qtd_paineis = :4, potencia_total = :5, custo_instal = :6, economia_mensal = :7, payback = :8,id_reg =:9   WHERE id_relatorio = :10"""
        try:
            cursor.execute(sql_user, (usuario.nome_usuario, usuario.email_user, usuario.senha_user, id_user))
            conexao.commit()
            
            cursor.execute(sql_end, (relatorio.consumo_mensal, relatorio.conta_luz, relatorio.area_desejada, relatorio.qtd_paineis, relatorio.potencia_total, relatorio.custo_instal, relatorio.economia_mensal, relatorio.payback, relatorio.id_reg, id_rel))
            conexao.commit()
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def deletar(self, id_alvo):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_user = """DELETE FROM usuario WHERE id_usu = :1"""
        sql_rel = """DELETE FROM relatorio WHERE id_usu = :1"""
        try:
            cursor.execute(sql_rel, (id_alvo,))
            cursor.execute(sql_user, (id_alvo,))
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.commit()
        conexao.close()
        return True
    
if __name__ == "__main__":
    visual.view()