import os


def renomear(path, output, name):
    '''
    Recebe um caminho, saída e nome, renomeia os arquivos .srt do caminho e envia pra saída.
    :param path: Endereço da pasta com os arquivos .srt
    :param output: Endereço de saída dos arquivos
    :param name: Nome que os arquivos serão renomeados
    '''

    #Faz uma lista com o nome de todos os arquivos no caminho de origem.
    a = os.listdir(path)

    #Verifica se o arquivo possuí a extensão .srt e os renomeia.
    for c in a:
        if '.srt' in c:
            n = c[:2]
            os.rename(f'{path}/{c}',
                    f'{output}/{name.replace("E00", f"E{n}")}.srt')


endereco = str(input('Insira o endereço dos arquivos: '))
saida = str(input('Digite o endereço de saída: '))
nome = str(input('Digite o novo nome do arquivo com E00 no lugar do episódio: '))
renomear(endereco, saida, nome)