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


        
def pegar_dados_usuario():
    db = Repositorio()
    
    id_user = len(db.ler_db_usuario()) + 1
    email = verificar_email("Digite seu email:\n==> ")
    nome = input("Digite o seu nome de usuario:\n==> ")
    senha = input("Crie uma senha para seu cadastro:\n==> ")
    
    user = Usuario(id_user, email, senha, nome)
        
    return user



def pegar_dados_relatorio():
    db = Repositorio()
    id_relatorio = len(db.ler_db_relatorio()) + 1
    id_user = input("Qual o id do usuario desse relatorio?\n==> ")
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
    
    potencia_total = int(qtnd_painel * 0.33)
    
    estimativa = int(potencia_total * 30 * regiao_escolhida.taxa_irradiacao)
    custo_total = int(potencia_total * 5250)
    economia_mensal = int(potencia_total * 425)
    payback = int(custo_total / economia_mensal)
    
    print(f'O custo total da instalação dos paineís será por volta de R${custo_total} e você tera um payback em {payback} mêses')
    
    if consumo_mensal <= estimativa:
        print("Caso instale o sistema de paínel solar cobrira totalmente o seu consumo de energia")
    else:
        print("Caso instale o sistema de paínel solar não ira cobrir o seu consumo de energia")
        
    relatorio = Relatorio(id_relatorio,consumo_mensal,conta_luz,tamanho_disp, qtnd_painel,potencia_total,custo_total,economia_mensal,payback,estimativa,id_user,regiao_escolhida.id_regiao)
        
    return relatorio



def cadastro():
    db = Repositorio()
    
    while True:
        op_cadastro = sub_menu("\nCADASTRO","Qual tipo de cadastro você deseja fazer?", "Cadastro de Usuario", "Cadastro de Relatorio", "Ambos", "Voltar ao menu")

        if op_cadastro == 1:
            usuario = pegar_dados_usuario()
            print(f'O seu ID de Usúario é ({usuario.id_user})')
            retorno = db.gravar_user(usuario)

        elif op_cadastro == 2:
            relatorio = pegar_dados_relatorio()
            print(f'O ID desse relatorio é ({relatorio.id_relatorio})')
            retorno = db.gravar_relatorio(relatorio)

        elif op_cadastro == 3:
            user = pegar_dados_usuario()
            print(f'O seu ID de Usúario é ({user.id_user})')
            retorno_user = db.gravar_user(user)
            rel = pegar_dados_relatorio()
            print(f'O ID desse relatorio é ({rel.id_relatorio})')
            retorno_rel = db.gravar_relatorio(rel)

            if retorno_user == False or retorno_rel == False:
                retorno = False
            else:
                retorno = True

        elif op_cadastro == 4:
            return True

        input("Aperte ENTER para continuar")


        if retorno:
            msg = "\nCadastro foi realizado com sucesso!!!"
        else:
            msg = "\nOcorreu um erro ao realizar cadastro no nosso sistema contate o nosso suporte!!!"


        opcao = sub_menu(msg,"O que o senhor(a) deseja fazer agora?","Realizar Outro Cadastro", "Voltar ao Menu", "Finalizar Programa")

        if opcao == 1:
            print("Realizando outro cadastro")
        elif opcao == 2:
            return True
        elif opcao == 3:
            return False



def alterar_dados():
    db = Repositorio()
    
    while True:
        op_update = sub_menu("\nATUALIZAR","Quais dados você quer atualizar?", "Dados de Usuario", "Dados de Relatorio", "Voltar ao menu")

        if op_update == 1:
            id_user_alvo = verificar_num("Qual o id do usuario que você deseja alterar os dados\n==> ")
            dados_novo_user = pegar_dados_usuario()
            resultado = db.update_user(dados_novo_user, id_user_alvo)

        elif op_update == 2:
            id_rel_alvo = verificar_num("Qual o id do relatorio que você deseja alterar os dados\n==> ")
            dados_novo_rel = pegar_dados_relatorio()
            resultado = db.update_relatorio(dados_novo_rel, id_rel_alvo)
        elif op_update == 3:
            return True


        if resultado:
            msg = "\nDados alterados com sucesso!!!"
        else:
            msg = "\nErro ao alterar dados contate o nosso suporte"


        opcao = sub_menu(msg,"O que o senhor(a) deseja fazer agora?","Realizar outro Update", "Voltar ao Menu", "Finalizar Programa")

        if opcao == 1:
            print("Atualizando outro dado")
        if opcao == 2:
            return True
        elif opcao == 3:
            return False


def excluir_dados():
    db = Repositorio()
    
    while True:
        op_delete = sub_menu("\nDELETAR","Quais dados você quer deleter?", "Dados de Usuario e Relatorios", "Apenas de um relatorio", "Voltar ao menu")

        if op_delete == 1:
            id_usuario = verificar_num("Qual id do usuario que você quer deletar os dados\n==> ")
            resultado = db.deletar_usuario(id_usuario)
            
        elif op_delete == 2:
            id_relatorio = verificar_num("Qual id do relatorio que você quer deletar os dados\n==> ")
            resultado = db.deletar_relatorio(id_relatorio)
            
        elif op_delete == 3:
            return True



        if resultado:
            msg = "\nDados excluidos com sucesso!!!"
        else:
            msg = "\nErro ao deletar contate nosso suporte!!!"

        opcao = sub_menu(msg,"O que o senhor(a) deseja fazer agora?","Realizar outro Delete", "Voltar ao Menu", "Finalizar Programa")

        if opcao == 1:
            print("Realizando Outro Delete")
        if opcao == 2:
            return True
        elif opcao == 3:
            return False


def consultar_dados():
    db = Repositorio()
    
    op_consulta = sub_menu("\nCONSULTA DADOS", "O que o senhor deseja fazer?", "Consultar dados de um usuario expecifico", "Consultar dados Gerais", "Voltar ao Menu")
    if op_consulta == 1:
        procurado = verificar_num("\nQual o id de quem você deseja procurar?")
        
        dados_ser_vivo = db.procurar_db(procurado)
        
        dado_pessoa = dados_ser_vivo.pop(0)

        print("-----DADOS-USUARIO-----")
        id = dado_pessoa[0]
        nome = dado_pessoa[1]
        email = dado_pessoa[2]
        senha = dado_pessoa[3]
        ser_vivo = Usuario(id,email,senha,nome)
        print(ser_vivo)

        print("-----RELATORIOS-----")
        for dados_rel in dados_ser_vivo:
            id = dados_rel[0]
            consumo = dados_rel[1]
            conta = dados_rel[2]
            area = dados_rel[3]
            paineis = dados_rel[4]
            potencia = dados_rel[5]
            custo = dados_rel[6]
            economia = dados_rel[7]
            payback = dados_rel[8]
            energia = dados_rel[9]
            id_usu = dados_rel[10]
            id_reg = dados_rel[11]
            relatorio = Relatorio(id,consumo,conta,area,paineis,potencia,custo,economia,payback,energia,id_usu,id_reg)
            print(relatorio, "\n--------------------------")
        msg = "\nConsulta realizada com sucesso!!!"
    elif op_consulta == 2:
        resultado = sub_menu("\nConsulta de dados","Quais tipos dados deseja consultar?", "Dados de usuarios", "Dados de relatorios", "Todos os dados")

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
        elif resultado == 2:
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
        elif resultado == 3:
            clientes = db.ler_db_usuario()
            for pessoa in clientes:

                id = pessoa[0]
                nome = pessoa[1]
                email = pessoa[2]
                senha = pessoa[3]

                ser_vivo = Usuario(id,email,senha,nome)
                print(ser_vivo, "\n--------------------------")
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
    elif op_consulta == 3:
        return True
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