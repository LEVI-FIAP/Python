class Usuario():
    def __init__(self, id = 0, email = "", senha = "", nome = ""):
        self.id_user = id
        self.nome_usuario = nome
        self.email_user = email
        self.senha_user = senha
    
class Relatorio():
    def __init__(self,id = 0,consumo = 0, conta = 0, area = 0, qtd_painel = 0, potencia = 0, custo = 0, economia = 0, payback = 0, id_usu = 0,id_reg = 0):
        self.id_relatorio = id
        self.consumo_mensal = consumo
        self.conta_luz = conta
        self.area_desejada = area
        self.qtd_paineis = qtd_painel
        self.potencia_total = potencia
        self.custo_instal = custo
        self.economia_mensal = economia
        self.payback = payback
        self.id_usu = id_usu
        self.id_reg = id_reg


class Regiao():
    def __init__(self, id = 0, nome = "", taxa = 0):
        self.id_regiao = id
        self.nome_regiao = nome
        self.taxa_irradiacao = taxa