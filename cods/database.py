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
        sql_usu = """INSERT INTO usuario (id_usu, email_usu, senha_usu, consumo_men, area_desejada, nome_usu, Regiao_id_reg, Painel_id_painel) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"""
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
        sql_end = """SELECT * FROM relatorio WHERE id_relatorio LIKE :1"""
        try:
            resultado = []
            cursor.execute(sql_user, (id_procurado_usuario,))            
            for dados in cursor:
                resultado.append(dados)
                
            cursor.execute(sql_end, (id_procurado,))
            for dados in cursor:
                resultado.append(dados)
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return resultado

    def update_db (self, cliente : Cliente , endereco : Endereco, id_clie : int):
        conexao = self.gerar_conexao_db()
        cursor = conexao.cursor()
        sql_clie = """UPDATE cliente SET email_cliente = :1, nome_cliente = :2, cpf = :3, data_nascimento = TO_DATE(:4, 'YYYY-MM-DD'), senha_clie = :5, telefone_clie = :6 WHERE id_cliente = :7"""
        sql_end = """UPDATE endereco SET cep = :1, numero =:2, cidade =:3 , rua =:4, uf = :5, complemento = :6, bairro =:7 WHERE id_cliente = :8 """
        try:
            cursor.execute(sql_clie, (cliente.email_cliente, cliente.nome_cliente, cliente.cpf, cliente.data_nascimento, cliente.senha_clie, cliente.telefone_clie, id_clie))
            conexao.commit()
            
            cursor.execute(sql_end, (endereco.cep, endereco.numero, endereco.cidade, endereco.rua, endereco.uf, endereco.complemento, endereco.bairro, id_clie))
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