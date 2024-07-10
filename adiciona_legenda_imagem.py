import os
import random
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

MAXIMO_LINHAS = 10
TAMANHO_MAXIMO_LINHA = 21
TEXTO_LINHA_X_POS = 50
TEXTO_LINHA_Y_POS = 70
TEXTO_LINHA_Y_OFFSET = 120
TEXTO_SPAN_INICIAL = 400

def dividir_sentencas(texto, tamanho_maximo_linha = TAMANHO_MAXIMO_LINHA, maximo_linhas = MAXIMO_LINHAS):
    """Quebra o texto da imagem em pequenas sentenças a serem utilizadas por linhas para gerar a imagem.

    Parametros
    ----------
    texto : str
        texto completo a ser dividido por linhas
    tamanho_maximo_linha : int (opcional)
        tamanho máximo de caracteres por linha. Padrão de 21 caracteres
    maximo_linhas : int (opcional)
        máximo de linhas por imagem. Padrão de 10 linhas
    """
    sentencas = []
    sentenca_completa = ""
    paragrafos = texto.split("\n")
    num_linhas = 0

    for paragrafo in paragrafos:
        palavras = paragrafo.split(" ")
        sentenca = ""
        for palavra in palavras:
            if (len(sentenca) + len(palavra)) > tamanho_maximo_linha:
                num_linhas += 1
                sentenca = palavra + " "
                sentenca_completa += palavra + " "
                if num_linhas == maximo_linhas:
                    num_linhas = 0
                    sentencas.append(sentenca_completa)
                    sentenca_completa = ""
            else:
                sentenca += palavra + " "
                sentenca_completa += palavra + " "
        if len(sentenca) > 0:
            num_linhas += 1
            if num_linhas == maximo_linhas:
                num_linhas = 0
                sentencas.append(sentenca_completa)
                sentenca_completa = ""

    if len(sentenca_completa) > 0:
        sentencas.append(sentenca_completa)
                
    return sentencas


def carregar_imagem(path_dir_imagem):
    """Carrega uma imagem aleatoriamente de um diretório usando o OpenCV. Aceita os formatos jpg, jpeg e png.
    O OpenCV não suporta fontes com carecteres especiais, portanto o PIL é usado para escrever os textos nas imagens.

    Parametros
    ----------
    path_dir_imagem : str
        path do diretório utilizado para carregar a imagem aleatória
    """
    imagens = [i for i in os.listdir(path_dir_imagem) if i.endswith((".jpg", ".jpeg", ".png"))]
    imagem = cv2.imread(path_dir_imagem + imagens[random.randint(0, len(imagens) - 1)])

    return Image.fromarray(imagem)

def adicionar_texto_imagem(imagem, sentenca, posicaoX, posicaoY):
    """Adiciona um texto a uma imagem em determinada posição X e Y.

    Parametros
    ----------
    imagem : obj
        objeto imagem
    sentenca : str
        texto a ser adicionado a imagem
    posicaoX : int
        posição X na imagem onde o texto será adicionado
    posicaoY : int
        posição Y na imagem onde o texto será adicionado
    """
    font = ImageFont.truetype("C:\Windows\Fonts\\arial.ttf", 100)
    draw = ImageDraw.Draw(imagem)
    draw.text((posicaoX, posicaoY), sentenca, font=font)

def gravar_imagem(path_destino, imagem):
    """Grava a imagem em um diretório.

    Parametros
    ----------
    path_destino : str
        caminho completo onde a imagem será gravada, incluindo o seu nome e extensão
    imagem : obj
        objeto imagem
    """
    imagem_cv2 = np.asarray(imagem)
    cv2.imwrite(path_destino, imagem_cv2)

def gerar_legenda_imagem(texto, dir_path_imagens, dir_destino_imagens, nome_imagem, tamanho_maximo_linha = TAMANHO_MAXIMO_LINHA, maximo_linhas = MAXIMO_LINHAS, texto_span_inicial = TEXTO_SPAN_INICIAL):
    """Cria uma imagem legendada com o texto passado como parametro.

    Parametros
    ----------
    texto : str
        texto completo a ser usado para gerar uma ou mais imagens.
    dir_path_imagens : str
        path do diretório utilizado para carregar as imagens de fundo
    dir_destino_imagens : str
        path onde a imagem ou imagens serao geradas e armazenadas
    nome_imagem : str
        nome da imagem a ser gerada
    tamanho_maximo_linha : int (opcional)
         tamanho máximo de caracteres por linha. Padrão de 21 caracteres
    maximo_linhas : int (optional)
        quantidade máxima de linhas por imagem. Padrão de 10 linhas
    texto_span_inicial : int (opcional)
        deslocamento inicial do texto da leganda na imagem a ser gerada. Padrao de 400
    """
    offset_imagem = 0
    imagem = carregar_imagem(dir_path_imagens)
    paragrafos = texto.split("\n")
    texto_linha = texto_span_inicial
    numero_linhas = 0

    for paragrafo in paragrafos:
        palavras = paragrafo.split(" ")
        sentenca = ""
        texto_linha += TEXTO_LINHA_Y_OFFSET
        for palavra in palavras:
            if (len(sentenca) + len(palavra)) > tamanho_maximo_linha:
                numero_linhas += 1
                adicionar_texto_imagem(imagem, sentenca, TEXTO_LINHA_X_POS, texto_linha)
                sentenca = palavra + " "
                texto_linha += TEXTO_LINHA_Y_OFFSET
                if numero_linhas == maximo_linhas:
                    numero_linhas = 0
                    offset_imagem += 1
                    gravar_imagem(dir_destino_imagens + "/" + nome_imagem + str(offset_imagem) + ".jpg", imagem)
                    imagem = carregar_imagem(dir_path_imagens)
                    texto_linha = texto_span_inicial + TEXTO_LINHA_Y_OFFSET
            else:
                sentenca += palavra + " "
        if len(sentenca) > 0:
            numero_linhas += 1
            adicionar_texto_imagem(imagem, sentenca, TEXTO_LINHA_X_POS, texto_linha)
            if numero_linhas == maximo_linhas:
                numero_linhas = 0
                offset_imagem += 1
                gravar_imagem(dir_destino_imagens + "/" + nome_imagem + str(offset_imagem) + ".jpg", imagem)
                imagem = carregar_imagem(dir_path_imagens)
                texto_linha = texto_span_inicial + TEXTO_LINHA_Y_OFFSET

    offset_imagem += 1

    gravar_imagem(dir_destino_imagens + "/" + nome_imagem + str(offset_imagem) + ".jpg", imagem)
