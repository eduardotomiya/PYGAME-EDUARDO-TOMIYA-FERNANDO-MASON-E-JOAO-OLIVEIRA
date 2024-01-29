import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

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

    dicionario_de_arquivos = carrega_arquivos()
    sheepDog_images = dicionario_de_arquivos['sheepDog']
    mop_images = dicionario_de_arquivos['Mop']
    DONE = 0
    PLAYING = 1
    state = PLAYING
    # Lista para armazenar as imagens sorteadas
    imagens_sorteadas = []

    # Sorteando 5 imagens
    for _ in range(5):
        imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
        imagens_sorteadas.append(imagem_sort)

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta

        # Desenha as imagens sorteadas na tela
        for img in imagens_sorteadas:
            img['y'] += img['velocidade']  # Atualiza a posição y
            window.blit(img['imagem'], (img['x'], img['y']))

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state