import os
import sys 


# print(len(sys.argv))
if len(sys.argv) == 3:
    caminho_origem = sys.argv[1]
    caminho_destino = sys.argv[2]
elif len(sys.argv) == 2:
    caminho_origem = sys.argv[1]
else:
    print("Argumentos invalidos, por favor insira 2 argumentos 'app.py' e 'Path' da pasta.")

# print(caminho_origem)
# print(caminho_destino)

caminho_origem = sys.argv[1]

for caminho_ativo, nome_diretorio, ficheiros in os.walk(caminho_origem):
    print(f'Caminho ativo {caminho_ativo}')
    print(f'Nome Directorios {nome_diretorio}')
    print(f'Ficheiros {ficheiros}')
    print()
    
