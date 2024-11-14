from database import Repositorio
from models import Usuario, Relatorio, Regiao

db = Repositorio()

teste_user = Usuario(666, "luizGay@gmail.com", "Subi no pé de pera", "LuanGameplay")
teste_rel = Relatorio(69, 333, 333, 33, 33, 33,33,33,33,666,5)
resultado = db.update_db(teste_user, teste_rel, 666,69)
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