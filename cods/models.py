class Usuario():
    def __init__(self, id = 0, email = "", senha = "", consumo = 0, area = 0, nome = "", regiao = 0, relatorio = 0):
        self.id_user = id
        self.email_user = email
        self.senha_user = senha
        self.consumo_men = consumo
        self.area_desejada = area
        self.nome_usuario = nome
        self.regiao_fk = regiao
        self.relatorio_fk = relatorio
    
class Relatorio():
    def __init__(self, id = 0, painel_qtnd = 0, potencia = 0, custo = 0, economia = 0, payback = 0, energia = 0):
        self.id_relatorio = id
        self.qtnd_painel = painel_qtnd
        self.potencia_total = potencia
        self.custo_total = custo
        self.economia_mensal = economia
        self.payback = payback
        self.energia_mes = energia

class Regiao():
    def __init__(self, id = 0, nome = "", taxa = 0):
        self.id_regiao = id
        self.nome_regiao = nome
        self.taxa_irradiacao = taxa