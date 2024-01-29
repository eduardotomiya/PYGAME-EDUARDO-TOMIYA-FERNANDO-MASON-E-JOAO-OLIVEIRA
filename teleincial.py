import pygame
import random
from os import path
from sprites import Botao
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, WHITE
from assets import carrega_arquivos


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    dicionario_de_arquivos = carrega_arquivos()
    # Criando botoes
    all_buttons = pygame.sprite.Group()

    medidas_botao = Botao(dicionario_de_arquivos, '')
    espacamento = (WIDTH - (medidas_botao.rect.width * 4))/ 5
    x = espacamento
    y = HEIGHT /2

    for i in range(4):
        jogo = Botao(dicionario_de_arquivos, f"Jogo {i+1}")

        jogo.rect.x = x
        jogo.rect.centery = y
        all_buttons.add(jogo)

        x+= jogo.rect.width + espacamento
  
    
    espacamento = (WIDTH - (medidas_botao.rect.width * 3))/ 4
    x = espacamento
    y += medidas_botao.rect.height + 50

    for i in range(4, 7):
        jogo = Botao(dicionario_de_arquivos, f"Jogo {i+1}")
        jogo.rect.x = x
        jogo.rect.centery = y
        all_buttons.add(jogo)

        x+= jogo.rect.width + espacamento
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = GAME
                running = False

            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for btn in all_buttons:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)
            

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        all_buttons.draw(screen)

        # Escrevendo texto dos botões
        for btn in all_buttons:
            btn_texto = dicionario_de_arquivos['font'].render(f"{btn.nome_do_jogo}", True, WHITE)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)

        tela_texto = dicionario_de_arquivos['font_media'].render("Minigames DesSoft", True, WHITE)
        text_rect = tela_texto.get_rect()
        text_rect.centerx = WIDTH / 2
        text_rect.centery = 200
        screen.blit(tela_texto, text_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
