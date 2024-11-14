import re, json, os, visual
from database import Repositorio
from models import Usuario, Relatorio, Regiao

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu ():
    limpar_terminal()
    menu = ("\n----------------------------------------------------------\n"
        "                  B E M   V I N D O\n\n"
        "Esses são os serviços que temos disponíveis:\n\n"
        "[1] - Cadastro de Usuario\n"
        "[2] - Alterar dados\n"
        "[3] - Excluir dados\n"
        "[4] - Consultar dados\n"
        "[5] - Calcular sua ecônomia com energia solar\n"
        "[6] - Exportar para um arquivo JSON\n"
        "[7] - Finalizar o Programa\n"
        "----------------------------------------------------------")

    mensagem_menu = "Qual serviço o senhor(a) deseja?\n==> "

    resposta_invalida = True
    while resposta_invalida == True:
        print(menu)
        resposta = input(mensagem_menu)

        if resposta.isdigit() and 1 <= int(resposta) <= 7:
            resposta_invalida = False
        else:
            mensagem_menu = "Por favor digite algum valor correspondente com o Menu\n==> "
    
    return resposta

def sub_menu(text="\n", subtitulo="O que o senhor(a) deseja fazer agora?", *opcoes):
    limpar_terminal()
    if not opcoes:
        opcoes = ("Voltar ao Menu", "Finalizar programa")
        
    menu = ("-----------------------------------------" + text +
            f"\n{subtitulo}\n")

    for index, opcao in enumerate(opcoes, start=1):
        menu += f"\n[{index}] - {opcao}"
    
    menu += "\n-----------------------------------------"
    
    mensagem = "Digite aqui o valor correspondente à função desejada\n==> "
    resposta_invalida = True

    while resposta_invalida:
        print(menu)
        resposta = verificar_num(mensagem)

        if 1 <= int(resposta) <= len(opcoes):
            resposta_invalida = False
        else:
            mensagem = "Por favor, digite algum valor correspondente ao Menu\n==> "

    return resposta

def verificar_num(text, qtd_min=0, qtd_max=100):
    while True:
        valor = input(text)
        if valor.isdigit() and qtd_min <= len(valor) <= qtd_max:
            return int(valor)
        print(f"\nPreencha com um valor numérico de {qtd_min} a {qtd_max} caracteres.")

def verificar_s_n(text):
    msg = text
    while True:
        escolha = input(msg).upper()[0]
        if escolha in ["S", "N"]:
            return escolha
        msg = "Por favor, digite um valor válido (S/N)\n==> "

def verificar_email(text):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    msg = text
    while True:
        email = input(msg)
        if re.match(padrao_email, email):
            return email
        msg = "Por favor, digite um email válido\n==> "
        
def pegar_dados():
    db = Repositorio()
    
    id_user = len(db.ler_db_usuario()) + 1
    email = verificar_email("Digite seu email:\n==> ")
    nome = input("Digite o seu nome de usuario:\n==> ")
    senha = input("Crie uma senha para seu cadastro:\n==> ")
    
    id_relatorio = len(db.ler_db_relatorio()) + 1
    tamanho_disp = verificar_num("Quantos metros quadrados (m²) você possui disponivel para instalar os painéis solares?\n==> ")
    consumo_mensal = verificar_num("Quanto de energia você consome no mês?\n==> ")
    conta_luz = verificar_num("Qual o valor da sua conta de luz normalmente?\n==> ")
    
    id_regiao = sub_menu("\nEscolha a região que deseja instalar os painéis", "Digite o número correspondente a região que deseja","Norte", "Nordeste", "Centro Oeste", "Sudeste", "Sul")
    
    regioes = db.ler_db_regiao()
    for dados in regioes:
        if dados[0] == id_regiao:
            regiao_escolhida = Regiao(dados[0], dados[1], dados[2])
            break;
    
    qtnd_painel = int(tamanho_disp / 1.7)
    print(f'A quantidade de painéis possivel instalar é de {qtnd_painel}')
    
    potencia_total = qtnd_painel * 0.33
    
    estimativa = potencia_total * 30 * regiao_escolhida.taxa_irradiacao
    custo_total = potencia_total * 5250
    economia_mensal = potencia_total * 425
    payback = custo_total / economia_mensal
    
    print(f'O custo total da instalação dos paineís será por volta de R${custo_total} e você tera um payback em {payback} mêses')
    
    if consumo_mensal <= estimativa:
        print("Caso instale o sistema de paínel solar cobrira totalmente o seu consumo de energia")
    else:
        print("Caso instale o sistema de paínel solar não ira cobrir o seu consumo de energia")
    
    user = Usuario(id_user, email, senha, nome)
    
    relatorio = Relatorio(id_relatorio,consumo_mensal,conta_luz,tamanho_disp, qtnd_painel,potencia_total,custo_total,economia_mensal,payback,estimativa,id_user,regiao_escolhida.id_regiao)
    
    return user, relatorio
 
def cadastro_user():
    limpar_terminal()
    db = Repositorio()
    
    print("\n----------------------------------------------------------\n"+ "                  C A D A S T R O\n\n")
    user, rel = pegar_dados()
    
    retorno = db.gravar_db(user, rel)

    if retorno:
        msg = "\nCadastro foi realizado com sucesso!!!"
    else:
        msg = "\nOcorreu um erro ao realizar cadastro no nosso sistema contate o nosso suporte!!!"


    opcao = sub_menu(msg)

    if opcao == 1:
        repetir = True
    elif opcao == 2:
        repetir = False

    return repetir

def alterar_dados():
    limpar_terminal()
    print("\n----------------------------------------------------------\n             A T U A L I Z A N D O   D A D O S\n\n")
    
    db = Repositorio()
    id_user_alvo = verificar_num("Qual o id do usuario que você deseja alterar os dados\n==> ")
    id_rel_alvo = verificar_num("Qual o id do relatorio que você deseja alterar os dados\n==> ")

    novo_user, novo_relatorio = pegar_dados()
    
    resultado = db.update_db(novo_user, novo_relatorio, id_user_alvo, id_rel_alvo)

    if resultado:
        msg = "\nDados alterados com sucesso!!!"
    else:
        msg = "\nErro ao alterar dados contate o nosso suporte"
    
    
    opcao = sub_menu(msg)

    if opcao == 1:
        repetir = True
    elif opcao == 2:
        repetir = False

    return repetir

def excluir_dados():
    limpar_terminal()
    print("\n----------------------------------------------------------\n"
          "                  E X C L U I N D O   D A D O S\n\n")
    
    db = Repositorio()
    
    id_usuario = verificar_num("Qual id do usuario que você quer deletar os dados\n==> ")
    id_relatorio = verificar_num("Qual id do relatorio que você quer deletar os dados\n==> ")
          
    resultado = db.deletar_db(id_usuario,id_relatorio)
    
    if resultado:
        msg = "\nDados excluidos com sucesso!!!"
    else:
        msg = "\nErro ao deletar contate nosso suporte!!!"
        
    opcao = sub_menu(msg)

    if opcao == 1:
        repetir = True
    elif opcao == 2:
        repetir = False

    return repetir

def consultar_dados():
    limpar_terminal()
    db = Repositorio()
    
    op_consulta = sub_menu("\nConsulta de Dados", "Deseja fazer uma consulta expecifica ou geral", "Expecifica", "Geral")
    if op_consulta == 1:
        procurado = verificar_num("\nQual o id de quem você deseja procurar?")
        
        dados_ser_vivo = db.procurar_db(procurado)
        for dados in dados_ser_vivo:
            print(dados)
        msg = "\nConsulta realizada com sucesso!!!"
    elif op_consulta == 2:
        resultado = sub_menu("\nConsulta de dados","Quais tipos dados deseja consultar?", "Dados de usuarios", "Dados de relatorios")

        if resultado == 1:    
            clientes = db.ler_db_usuario()
            for pessoa in clientes:

                id = pessoa[0]
                nome = pessoa[1]
                email = pessoa[2]
                senha = pessoa[3]

                ser_vivo = Usuario(id,email,senha,nome)
                print(ser_vivo, "\n--------------------------")
                msg = "\nConsulta realizada com sucesso!!!"
        else:
            dados = db.ler_db_relatorio()
            for rel in dados:
                id = rel[0]
                consumo = rel[1]
                conta = rel[2]
                area = rel[3]
                paineis = rel[4]
                potencia = rel[5]
                custo = rel[6]
                economia = rel[7]
                payback = rel[8]
                energia = rel[9]
                id_usu = rel[10]
                id_reg = rel[11]

                relatorio = Relatorio(id,consumo,conta,area,paineis,potencia,custo,economia,payback,energia,id_usu,id_reg)
                print(relatorio, "\n--------------------------")
                msg = "\nConsulta realizada com sucesso!!!"
    else:
        msg = "Erro ao realizar a consulta de dados contato o suporte!!!"
    input("Aperte ENTER para continuar")
    opcao = sub_menu(msg)

    if opcao == 1:
        repetir = True
    elif opcao == 2:
        repetir = False

    return repetir   

def exportar_dados():
    limpar_terminal()
    db = Repositorio()
    
    dados = []
    clientes = db.ler_db_usuario()
    for pessoa in clientes:
        id = pessoa[0]
        nome = pessoa[1]
        email = pessoa[2]
        senha = pessoa[3]
        ser_vivo = Usuario(id,email,senha,nome)
        dados.append(ser_vivo.to_dict())
    
    relatorios = db.ler_db_relatorio()
    for rel in relatorios:
        id = rel[0]
        consumo = rel[1]
        conta = rel[2]
        area = rel[3]
        paineis = rel[4]
        potencia = rel[5]
        custo = rel[6]
        economia = rel[7]
        payback = rel[8]
        energia = rel[9]
        id_usu = rel[10]
        id_reg = rel[11]
        relatorio = Relatorio(id,consumo,conta,area,paineis,potencia,custo,economia,payback,energia,id_usu,id_reg)
        dados.append(relatorio.to_dict())
        
        
    nome_arquivo = 'dados.json'
    

    with open(nome_arquivo, 'w', encoding='utf-8') as arq_json:
        json.dump(dados, arq_json, indent=4)

    opcao = sub_menu(f"\nExportação concluida com sucesso olhe os arquivos JSON com os dados!!!")

    if opcao == 1:
        repetir = True
    elif opcao == 2:
        repetir = False

    return repetir

if __name__ == "__main__":
    visual.view()