import re, requests, json, os
from datetime import datetime
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
        "[5] - Calcular sua ecônomia com energia solar"
        "[5] - Exportar para um arquivo JSON\n"
        "[6] - Finalizar o Programa\n"
        "----------------------------------------------------------")

    mensagem_menu = "Qual serviço o senhor(a) deseja?\n==> "

    resposta_invalida = True
    while resposta_invalida == True:
        print(menu)
        resposta = input(mensagem_menu)

        if resposta in ["1","2","3","4","5","6","7"]:
            resposta_invalida = False
        else:
            mensagem_menu = "Por favor digite algum valor correspondente com o Menu\n==> "
    
    return resposta


def sub_menu (text = "\n",subtitulo="O que o senhor(a) deseja fazer agora?", op1 = "Voltar para o Menu Principal", op2 ="Finalizar Programa"):
    limpar_terminal()
    
    menu = ("-----------------------------------------" + text +
            f"\n{subtitulo}"+
            f"\n\n[1] - {op1}"+
            f"\n[2] - {op2}" + 
            "\n-----------------------------------------" )
    mensagem = "Digite aqui o valor correspondente a função desejada\n==> "
    resposta_invalida = True

    while resposta_invalida == True:
        print(menu)
        resposta = input(mensagem)

        if resposta in ["1","2"]:
            resposta_invalida = False
        else: 
            mensagem = "Por favor digite algum valor correspondente com o Menu\n==> "

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
    email = verificar_email("Digite seu email:\n==> ")
    nome = input("Digite o seu nome de usuario:\n==> ")
    senha = input("Crie uma senha para seu cadastro:\n==> ")
    
    tamanho_disp = verificar_num("Quantos metros quadrados (m²) você possui disponivel para instalar os painéis solares")
    qtnd_painel = int(tamanho_disp / 1.7)
    print(f'A quantidade de painéis possivel instalar é de {qtnd_painel}')
    potencia_total = qtnd_painel * 0.33



    return ""

 
def cadastro_user():
    limpar_terminal()
    db = Repositorio()
    
    print("\n----------------------------------------------------------\n"
          "                  C A D A S T R O\n\n")
    cliente, end = pegar_dados()
    
    retorno = db.gravar_db(cliente,end)

    
    if retorno:
        msg = "\nCadastro foi realizado com sucesso!!!"
    else:
        msg = "\nOcorreu um erro ao realizar cadastro no nosso sistema contate o nosso suporte!!!"


    opcao = sub_menu(msg)

    if opcao == "1":
        repetir = True
    elif opcao == "2":
        repetir = False

    return repetir

def alterar_dados():
    limpar_terminal()
    print("\n----------------------------------------------------------\n             A T U A L I Z A N D O   D A D O S\n\n")
    
    db = Repositorio()
    id_clie_alvo, id_clie_str = verificar_num("Qual o id do usuario que você deseja alterar os dados\n==> ")

    novo_clie, novo_end = pegar_dados()
    
    resultado = db.update_db(novo_clie, novo_end, id_clie_alvo)

    if resultado:
        msg = "\nDados alterados com sucesso!!!"
    else:
        msg = "\nErro ao alterar dados contate o nosso suporte"
    
    
    opcao = sub_menu(msg)

    if opcao == "1":
        repetir = True
    elif opcao == "2":
        repetir = False

    return repetir


def excluir_dados():
    limpar_terminal()
    print("\n----------------------------------------------------------\n"
          "                  E X C L U I N D O   D A D O S\n\n")
    
    db = Repositorio()
    
    id_procurado, id_str = verificar_num("Qual id do usuario que você quer deletar os dados\n==> ")
          
    resultado = db.deletar_db(id_procurado)
    
    if resultado:
        msg = "\nDados excluidos com sucesso!!!"
    else:
        msg = "\nErro ao deletar contate nosso suporte!!!"
        
    opcao = sub_menu(msg)

    if opcao == "1":
        repetir = True
    elif opcao == "2":
        repetir = False

    return repetir


def consultar_dados():
    limpar_terminal()
    db = Repositorio()
    
    op_consulta = sub_menu("\nConsulta de Dados", "Deseja fazer uma consulta expecifica ou geral", "Expecifica", "Geral")
    if op_consulta == "1":
        procurado, procurado_str = verificar_num("\nQual o Id de quem você deseja procurar?")
        
        cliente = db.procurar_db(procurado)

        id_cliente = cliente[0][0]
        email = cliente[0][1]
        nome = cliente[0][2]
        cpf = cliente[0][4]
        dt_nasc = cliente[0][4]
        senha = cliente[0][5]
        tele = cliente[0][6]
        ser_vivo = Cliente(id_cliente,email,nome,cpf,dt_nasc,senha,tele)
        print(ser_vivo, "\n--------------------------")
        
        id_end = cliente[1][0]
        cep = cliente[1][1]
        numero = cliente[1][2]
        cidade = cliente[1][3]
        rua = cliente[1][4]
        uf = cliente[1][5]
        complemento = cliente[1][6]
        bairro = cliente[1][7]
        id_clie = cliente[1][8]
        id_mec = cliente[1][9]
        end = Endereco(id_end,cep,numero,cidade,rua,uf,complemento,bairro,id_clie,id_mec)
        print(end, "\n--------------------------")
    else:
        resultado = sub_menu("\nConsulta de dados","Quais tipos dados deseja consultar?", "Dados de clientes", "Dados de endereços")

        if resultado == "1":    
            clientes = db.ler_db_cliente()
            for pessoa in clientes:

                id = pessoa[0]
                email = pessoa[1]
                nome = pessoa[2]
                cpf = pessoa[3]
                dt_nasc = pessoa[4]
                senha = pessoa[5]
                tele = pessoa[6]

                ser_vivo = Cliente(id,email,nome,cpf,dt_nasc,senha,tele)
                print(ser_vivo, "\n--------------------------")
        else:
            dados = db.ler_db_endereco()
            for endereco in dados:
                id = endereco[0]
                cep = endereco[1]
                numero = endereco[2]
                cidade = endereco[3]
                rua = endereco[4]
                uf = endereco[5]
                complemento = endereco[6]
                bairro = endereco[7]
                id_clie = endereco[8]
                id_mec = endereco[9]

                end = Endereco(id,cep,numero,cidade,rua,uf,complemento,bairro,id_clie,id_mec)
                print(end, "\n--------------------------")
    
    input("Aperte ENTER para continuar")
    opcao = sub_menu(f"\nConsulta realizada com sucesso!!!")

    if opcao == "1":
        repetir = True
    elif opcao == "2":
        repetir = False

    return repetir


def exportar_dados():
    limpar_terminal()
    db = Repositorio()
    
    dados = []
    clientes = db.ler_db_cliente()
    for pessoa in clientes:
        
        id = pessoa[0]
        email = pessoa[1]
        nome = pessoa[2]
        cpf = pessoa[3]
        dt_nasc = pessoa[4]
        senha = pessoa[5]
        tele = pessoa[6]
        
        ser_vivo = Cliente(id,email,nome,cpf,dt_nasc,senha,tele)
        dados.append(ser_vivo.to_dict())
    
    enderecos = db.ler_db_endereco()
    for endereco in enderecos:
        id = endereco[0]
        cep = endereco[1]
        numero = endereco[2]
        cidade = endereco[3]
        rua = endereco[4]
        uf = endereco[5]
        complemento = endereco[6]
        bairro = endereco[7]
        id_clie = endereco[8]
        id_mec = endereco[9]
        
        end = Endereco(id,cep,numero,cidade,rua,uf,complemento,bairro,id_clie,id_mec)
        dados.append(end.to_dict())
        
        
    nome_arquivo = 'dados.json'
    

    with open(nome_arquivo, 'w', encoding='utf-8') as arq_json:
        json.dump(dados, arq_json,default=converter_data, indent=4)

    opcao = sub_menu(f"\nExportação concluida com sucesso olhe os arquivos JSON com os dados!!!")

    if opcao == "1":
        repetir = True
    elif opcao == "2":
        repetir = False

    return repetir