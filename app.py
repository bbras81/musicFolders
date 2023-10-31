import os


def main():
    
    root = '/Users/brunobras/Documents/Programação/musicFolders/musica'
    
    #Aqui é feito o primeiro scaner da pasta root da app    
    diretorios = scanner(root)
    
    dir_1 = []
    dir_2 = []
    nomes = {}


    
    for diretorio in diretorios:
        dir_1.append(scanner(diretorio))

    for diretorio in dir_1:
        dir_2.append(scanner(diretorio))
    

    
def scanner(caminho):  
    diretorios = []
    with os.scandir(caminho) as it:
        for entry in it:
            if entry.is_dir():
                diretorios.append(entry.path)
    return diretorios



def search_name(caminho):
    open_par = caminho.find('(')
    close_par = caminho.find(')')
    if open_par != -1 and close_par != -1:
        novo_nome = caminho[open_par + 1:close_par]
        nomes = {caminho : novo_nome}
    else:
        return False
    return nomes
    
    
    
def renomear_pasta():
    pass








    # for diretorio in diretorios:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Diretório que contém as pastas a serem renomeadas

    # Função para renomear pastas
    
    
    
    
    
    
    
    
    
    # def renomear_pastas():
    #     pass
        
        
        
        
        
        
        
# def ver_pasta(diretorio):
#     caminho = ''
#     with os.scandir(diretorio) as it:
#         for entry in it:
#             if entry.name.startswith('.'):
#                 pass
#             elif entry.is_dir():
#                 caminho = os.path.join(diretorio, entry)
#                 ver_pasta(caminho)
#             else:
#                 break

#     return caminho
        
        
        
        
        
        
        # with os.scandir(diretorio) as it:
        #     for entry in it:
        #         if not entry.name.startswith('.') and entry.is_dir():
        #             novo_dir = diretorio + '/' + entry.name
        #             dir_filho = os.listdir(novo_dir)
        #             if os.path.isdir(novo_dir):
        #                 indice_abre = dir_filho.find("(")
        #                 indice_fecha = dir_filho.find(")")
        #                 if indice_abre != -1 and indice_fecha != -1:
        #                     novo_nome = dir_filho[indice_abre + 1:indice_fecha]
        #                     novo_caminho_pasta = os.path.join(diretorio, novo_nome)
        #                     os.rename(caminho_pasta, novo_caminho_pasta)
        #                     print(f"Pasta '{pasta}' renomeada para '{novo_nome}'.")
        #             print(dir_filho)
        
        # for pasta in os.listdir(diretorio):
        #     caminho_pasta = os.path.join(diretorio, pasta)
        #     if os.path.isdir(caminho_pasta):
        #         indice_abre = pasta.find("(")
        #         indice_fecha = pasta.find(")")
        #         if indice_abre != -1 and indice_fecha != -1:
        #             novo_nome = pasta[indice_abre + 1:indice_fecha]
        #             novo_caminho_pasta = os.path.join(diretorio, novo_nome)
        #             os.rename(caminho_pasta, novo_caminho_pasta)
        #             print(f"Pasta '{pasta}' renomeada para '{novo_nome}'.")

    # Chamando a função para renomear pastas no diretório especificado
    # renomear_pastas()
if __name__ == '__main__':
    main()
