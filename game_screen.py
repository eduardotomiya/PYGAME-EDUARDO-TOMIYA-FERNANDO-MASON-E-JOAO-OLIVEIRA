import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos

# Função para verificar colisão entre ponto (clique do mouse) e retângulo (imagem)
def colisao_ponto_retangulo(px, py, rx, ry, rw, rh):
    return rx <= px <= rx + rw and ry <= py <= ry + rh

# Função para sortear uma nova imagem (Cachorro ou Mop), posição e velocidade
def sorteia_imagem(sheepDog_images, mop_images):
    eh_cachorro = random.choice([True, False])
    imagem = random.choice(sheepDog_images if eh_cachorro else mop_images)
    x = random.randint(0, WIDTH - imagem.get_width())
    y = random.randint(-100, -1)
    velocidade = random.randint(1, 5)
    return {'imagem': imagem, 'eh_cachorro': eh_cachorro, 'x': x, 'y': y, 'velocidade': velocidade}

# Função principal do jogo
def game_screen(window):
    # Inicialização e carregamento dos recursos
    clock = pygame.time.Clock()
    dicionario_de_arquivos = carrega_arquivos()
    sheepDog_images = dicionario_de_arquivos['sheepDog']
    mop_images = dicionario_de_arquivos['Mop']
    som = dicionario_de_arquivos['som']

    # Estados do jogo e inicialização de variáveis
    DONE, PLAYING = 0, 1
    state, vidas, segundos = PLAYING, 3, 0
    imagens_sorteadas = [sorteia_imagem(sheepDog_images, mop_images) for _ in range(5)]  # Inicializa com 5 imagens
    fonte = pygame.font.Font(None, 36)

    while state != DONE:
        clock.tick(FPS)  # Limita a taxa de quadros por segundo (FPS)

        # Trata eventos como fechar o jogo ou cliques do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for img in imagens_sorteadas[:]:  # Verifica colisão do clique com as imagens
                    if colisao_ponto_retangulo(mx, my, img['x'], img['y'], img['imagem'].get_width(), img['imagem'].get_height()):
                        if not img['eh_cachorro']:
                            som.play()  # Toca som ao clicar em Mop
                            vidas -= 1  # Jogador perde uma vida ao clicar em Mop
                        imagens_sorteadas.remove(img)  # Remove a imagem clicada
                        # Adiciona duas novas imagens
                        for _ in range(2):
                            imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
                            imagens_sorteadas.append(imagem_sort)
                        break

        # Remove imagens de Cachorro que saíram da tela e reduz vidas
        for img in imagens_sorteadas[:]:
            if img['y'] > HEIGHT and img['eh_cachorro']:
                imagens_sorteadas.remove(img)
                vidas -= 1  # Perde uma vida
                # Adiciona duas novas imagens
                for _ in range(2):
                    imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
                    imagens_sorteadas.append(imagem_sort)

        segundos += 1  # Atualiza o contador de segundos

        window.fill(BLACK)  # Preenche a tela com a cor preta

        # Desenha as imagens sorteadas na tela
        for img in imagens_sorteadas:
            img['y'] += img['velocidade']  # Atualiza a posição y da imagem
            window.blit(img['imagem'], (img['x'], img['y']))

        # Renderiza a quantidade de vidas e a pontuação na tela
        vidas_text = fonte.render(f'Vidas: {vidas}', True, (255, 255, 255))
        pontuacao_text = fonte.render(f'Pontuação: {segundos}', True, (255, 255, 255))
        window.blit(vidas_text, (WIDTH - vidas_text.get_width() - 10, 10))
        window.blit(pontuacao_text, (10, 10))

        pygame.display.update()  # Atualiza a tela

        if vidas <= 0:
            state = DONE  # Termina o jogo se o jogador perder todas as vidas

    return state
