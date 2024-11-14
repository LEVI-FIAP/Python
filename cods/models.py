import visual

class Usuario():
    def __init__(self, id = 0, email = "", senha = "", nome = ""):
        self.id_user = id
        self.nome_usuario = nome
        self.email_user = email
        self.senha_user = senha
        
    def __str__(self):
        return f'ID - ({self.id_user})\n- Nome Usuário: {self.nome_usuario}\n- Email: {self.email_user}\n- Senha: {self.senha_user}'
    
    def to_dict(self):
        return {
            "id_user": self.id_user,
            "nome_usuario": self.nome_usuario,
            "email": self.email_user,
            "senha": self.senha_user
        }
    
class Relatorio():
    def __init__(self,id = 0,consumo = 0, conta = 0, area = 0, qtd_painel = 0, potencia = 0, custo = 0, economia = 0, payback = 0, estimativa = 0, id_usu = 0,id_reg = 0):
        self.id_relatorio = id
        self.consumo_mensal = consumo
        self.conta_luz = conta
        self.area_desejada = area
        self.qtd_paineis = qtd_painel
        self.potencia_total = potencia
        self.estimativa_energia = estimativa
        self.custo_instal = custo
        self.economia_mensal = economia
        self.payback = payback
        self.id_usu = id_usu
        self.id_reg = id_reg
        
    def __str__(self):
        return f'ID - ({self.id_relatorio})\n- Consumo Mensal: {self.consumo_mensal}\n- Conta de Luz: {self.conta_luz}\n- Area Desejada: {self.area_desejada}\n- Quantidade de Paineis: {self.qtd_paineis}\n- Potência Total: {self.potencia_total}\n- Custo Instalação: {self.custo_instal}\n- Economia Mensal: {self.economia_mensal}\n- Payback {self.payback}\n- ID Usuario: {self.id_usu}\n- ID Região: {self.id_reg}'
    
    def to_dict(self):
        return {
            "id_relatorio": self.id_relatorio,
            "consumo_mensal": self.consumo_mensal,
            "conta_luz": self.conta_luz,
            "area_desejada": self.area_desejada,
            "qtd_paineis": self.qtd_paineis,
            "potencia_total": self.potencia_total,
            "custo_instal": self.custo_instal,
            "economia_mensal": self.economia_mensal,
            "payback": self.payback,
            "id_usu": self.id_usu,
            "id_reg": self.id_reg
        }


class Regiao():
    def __init__(self, id = 0, nome = "", taxa = 0):
        self.id_regiao = id
        self.nome_regiao = nome
        self.taxa_irradiacao = taxa
        
    def __str__(self):
        return f'ID - ({self.id_regiao})\n- Nome Região: {self.nome_regiao}\n- Horas de Sol: {self.taxa_irradiacao}'
    
    def to_dict(self):
        return {
            "id_regiao": self.id_regiao,
            "nome_regiao": self.nome_regiao,
            "taxa_irradiacao": self.taxa_irradiacao
        }
        
if __name__ == "__main__":
    visual.view()