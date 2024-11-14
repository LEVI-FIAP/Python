from database import Repositorio
from models import Usuario, Relatorio, Regiao

db = Repositorio()

teste_user = Usuario(666, "luizGay@gmail.com", "I ghost to the down o cool", "vicenzinho")
teste_rel = Relatorio(69, 666, 200, 69, 69, 69,69,69,69,666,2)
resultado = db.gravar_db(teste_user, teste_rel)
print(resultado)
# import controler

# repetir = True
# while repetir == True:
#     opcoes = controler.menu()
    
#     if opcoes == "1":
#         repetir = controler.cadastro_user()
        
#     elif opcoes == "2":
#         repetir = controler.alterar_dados()

#     elif opcoes == "3":
#         repetir = controler.excluir_dados()

#     elif opcoes == "4":
#         repetir = controler.consultar_dados()

#     elif opcoes == "5":
#         repetir = controler.calcular_energia()

#     elif opcoes == "6":
#         repetir = controler.exportar_dados()
        
#     else:
#         print("Programa finalizado")
#         break;