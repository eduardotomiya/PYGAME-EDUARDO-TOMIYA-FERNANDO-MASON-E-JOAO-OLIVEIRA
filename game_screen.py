import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

#Função que tem como objetivo detectar a colisão entre um ponto e o retangulo:
def colisao_ponto_retangulo(px, py, rx, ry, rw, rh):
    return rx <= px <= rx + rw and ry <= py <= ry + rh


def sorteia_imagem(sheepDog_images, mop_images):
    # Escolhe aleatoriamente entre Cachorro e Mop
    eh_cachorro = random.choice([True, False])
    imagem = random.choice(sheepDog_images if eh_cachorro else mop_images)

    # Sorteia a posição x (garantindo que a imagem não saia da tela)
    x = random.randint(0, WIDTH - imagem.get_width())

    # Sorteia uma posição y negativa para a imagem aparecer gradualmente
    y = random.randint(-100, -1)

    # Sorteia uma velocidade aleatória
    velocidade = random.randint(1, 5)

    return {
        'imagem': imagem,
        'eh_cachorro': eh_cachorro,
        'x': x,
        'y': y,
        'velocidade': velocidade
    }

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega os arquivos de recursos
    dicionario_de_arquivos = carrega_arquivos()
    sheepDog_images = dicionario_de_arquivos['sheepDog']
    mop_images = dicionario_de_arquivos['Mop']

    # Estados do jogo
    DONE = 0
    PLAYING = 1
    state = PLAYING

    # Lista para armazenar as imagens sorteadas
    imagens_sorteadas = []

    # Sorteando 5 imagens iniciais
    for _ in range(5):
        imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
        imagens_sorteadas.append(imagem_sort)

    # Loop principal
    while state != DONE:
        clock.tick(FPS)

        # Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obtém a posição do clique do mouse
                mx, my = pygame.mouse.get_pos()

                # Verifica se alguma imagem foi clicada
                for img in imagens_sorteadas[:]:  # Usar uma cópia da lista para iterar
                    if colisao_ponto_retangulo(mx, my, img['x'], img['y'], img['imagem'].get_width(), img['imagem'].get_height()):
                        imagens_sorteadas.remove(img)  # Remove a imagem clicada
                        nova_imagem = sorteia_imagem(sheepDog_images, mop_images)  # Cria uma nova imagem
                        imagens_sorteadas.append(nova_imagem)  # Adiciona a nova imagem à lista
                        break  # Sai do loop, pois já tratou o clique

        # Gera saídas
        window.fill(BLACK)

        # Desenha as imagens sorteadas na tela
        for img in imagens_sorteadas:
            img['y'] += img['velocidade']
            window.blit(img['imagem'], (img['x'], img['y']))

        pygame.display.update()

    return state