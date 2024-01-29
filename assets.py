import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite com base na spritesheet
    '''
    Recebe uma imagem de sprite sheet e retorna uma lista de imagens. 
    É necessário definir quantos sprites estão presentes em cada linha e coluna.
    Essa função assume que os sprites no sprite sheet possuem todos o mesmo tamanho.
    Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    '''
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    sprites = []

    # Loop para percorrer cada linha e coluna da spritesheet
    for row in range(rows):
        for column in range(columns):
            # Calcula a posição x e y do sprite atual na spritesheet
            x = column * sprite_width
            y = row * sprite_height

            # Cria um retângulo que representa a área do sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma nova superfície (imagem) para armazenar o sprite recortado
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)

            # Copia o sprite da spritesheet para a nova superfície
            image.blit(spritesheet, (0, 0), dest_rect)

            # Adiciona a nova imagem à lista de sprites
            sprites.append(image)
    return sprites

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
    
    # Carregar a spritesheet SheepdogOrMop
    # Carrega a imagem completa da spritesheet
    spritesheet = pygame.image.load(os.path.join(IMG_DIR, 'SheepdogOrMop.jpg'))

    # Usa a função load_spritesheet para obter todos os sprites da spritesheet
    all_sprites = load_spritesheet(spritesheet, rows=4, columns=4)  # Ajuste o número de linhas e colunas conforme necessário

    # Separar as imagens de Cachorro e Mop
    # Separa os sprites em duas listas, uma para Cachorro e outra para Mop, com base em suas posições na lista all_sprites
    sheepDog_images = [all_sprites[i] for i in [0, 2, 5, 7, 8, 10, 13, 15]]
    mop_images = [all_sprites[i] for i in [1, 3, 4, 6, 9, 11, 12, 14]]

    #Armazena som
    dicionario_de_arquivos['som']=pygame.mixer.Sound(os.path.join(SND_DIR, 'wah-wah.wav'))

    # Armazenar as listas no dicionário sob as chaves 'sheepDog' e 'Mop'
    dicionario_de_arquivos['sheepDog'] = sheepDog_images
    dicionario_de_arquivos['Mop'] = mop_images

    return dicionario_de_arquivos
