import controler

def view():
    repetir = True
    while repetir == True:
        opcoes = controler.menu()

        if opcoes == "1":
            repetir = controler.cadastro_user()

        elif opcoes == "2":
            repetir = controler.alterar_dados()

        elif opcoes == "3":
            repetir = controler.excluir_dados()

        elif opcoes == "4":
            repetir = controler.consultar_dados()

        elif opcoes == "5":
            repetir = controler.calcular_energia()

        elif opcoes == "6":
            repetir = controler.exportar_dados()

        else:
            print("Programa finalizado")
            break;
        
if __name__ == "__main__":
    view()