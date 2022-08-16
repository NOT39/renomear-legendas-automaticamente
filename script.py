import os

path = str(input('Insira o endereço dos arquivos: '))
saida = str(input('Digite o endereço de saída: '))
nome = str(input('Digite o novo nome do arquivo com E00 no lugar do episódio: '))
a = os.listdir(path)
for c in a:
    if '.srt' in c:
        n = c[:2]
        os.rename(f'{path}/{c}',
                  f'{saida}/{nome.replace("E00", f"E{n}")}.srt')
