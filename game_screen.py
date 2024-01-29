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
    # Inicialização do relógio para controle de FPS
    clock = pygame.time.Clock()

    # Carrega os arquivos de imagem e som
    dicionario_de_arquivos = carrega_arquivos()
    sheepDog_images = dicionario_de_arquivos['sheepDog']
    mop_images = dicionario_de_arquivos['Mop']

    # Definição dos estados do jogo
    DONE = 0
    PLAYING = 1
    state = PLAYING

    # Lista para armazenar as imagens sorteadas
    imagens_sorteadas = []

    # Variáveis para controlar vidas e pontuação
    vidas = 3
    segundos = 0

    # Fonte para renderizar texto na tela
    fonte = pygame.font.Font(None, 36)

    # Carrega efeito sonoro
    efeito_sonoro = pygame.mixer.Sound('assets/snd/efeito_sonoro.wav')

    while state != DONE:
        # Limita o jogo a uma taxa de FPS (Frames Per Second)
        clock.tick(FPS)

        # Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o jogador clicou em alguma imagem
                mx, my = pygame.mouse.get_pos()
                for img in imagens_sorteadas[:]:
                    if colisao_ponto_retangulo(mx, my, img['x'], img['y'], img['imagem'].get_width(), img['imagem'].get_height()):
                        if not img['eh_cachorro']:
                            efeito_sonoro.play()
                            vidas -= 1
                        imagens_sorteadas.remove(img)
                        for _ in range(2):
                            imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
                            imagens_sorteadas.append(imagem_sort)
                        break

        # Verifica se imagens de Cachorro saíram da tela
        for img in imagens_sorteadas[:]:
            if img['y'] > HEIGHT and img['eh_cachorro']:
                imagens_sorteadas.remove(img)
                vidas -= 1
                for _ in range(2):
                    imagem_sort = sorteia_imagem(sheepDog_images, mop_images)
                    imagens_sorteadas.append(imagem_sort)

        # Atualiza a contagem de segundos
        segundos += 1

        # Preenche a tela com a cor preta
        window.fill(BLACK)

        # Desenha as imagens sorteadas na tela
        for img in imagens_sorteadas:
            img['y'] += img['velocidade']  # Atualiza a posição y
            window.blit(img['imagem'], (img['x'], img['y']))

        # Renderiza a quantidade de vidas no canto superior direito
        vidas_text = fonte.render(f'Vidas: {vidas}', True, (255, 255, 255))
        window.blit(vidas_text, (WIDTH - vidas_text.get_width() - 10, 10))

        # Renderiza a pontuação no canto superior esquerdo
        pontuacao_text = fonte.render(f'Pontuação: {segundos}', True, (255, 255, 255))
        window.blit(pontuacao_text, (10, 10))

        # Atualiza a tela
        pygame.display.update()

        # Verifica se o jogador perdeu todas as vidas
        if vidas <= 0:
            state = DONE

    return state