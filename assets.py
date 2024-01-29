import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()
    
    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    return dicionario_de_arquivos
