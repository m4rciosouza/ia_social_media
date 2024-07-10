import random
import string
from adiciona_legenda_imagem import gerar_legenda_imagem

BASE_IMAGE_ASSETS_PATH = 'assets/'
BASE_POSTS_IMGS_FINAL_PATH = 'imagens-geradas/'

def gerar_imagens(sentencas):
    """Gera uma ou mais imagens a partir de uma lista de frases.

    Parametros
    ----------
    sentencas : Array
        Lista contendo as sentenças/frases a serem utilizadas para gerar imagens,
        como por exemplo: ["A melhor maneira de prever o futuro é criar-lo."]
    """
    for sentenca in sentencas:
        print('=> ' + sentenca)
        print('gerando imagens...')
        nome_imagem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        gerar_legenda_imagem(
            sentenca, 
            BASE_IMAGE_ASSETS_PATH, 
            BASE_POSTS_IMGS_FINAL_PATH, 
            nome_imagem, 
            maximo_linhas=10, 
            texto_span_inicial=200
        )
    print('processo concluído com sucesso!')

# exemplo de chamada
# sentencas = [
#     "A melhor maneira de prever o futuro é criar-o."
# ]
# gerar_imagens_instagram(sentencas)
