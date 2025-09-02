import pygame
import random

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

cobra = [(100, 50)]
dire = (10, 0)
macas = (300, 200)

def desenhar():
    tela.fill((0, 0, 0))
    for parte in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (*parte, 10, 10))
    
    pygame.draw.rect(tela, (255, 0 , 0), (*macas, 10, 10))
    pygame.display.update()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type  == pygame.QUIT:
            rodando = False
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                dire = (0, -10)
            elif evento.key == pygame.K_DOWN:
                dire = (0, 10)
            elif evento.key == pygame.K_LEFT:
                dire = (-10, 0)
            elif evento.key == pygame.K_RIGHT:
                dire = (10, 0)

    nova_cabeca = (cobra[0][0] + dire[0], cobra[0][1] + dire[1])
    cobra.insert(0, nova_cabeca)
    
    if nova_cabeca == macas:
        macas = (random.randrange(0, 800, 10), random.randrange(0, 600, 10))
    else:
        cobra.pop()

    if nova_cabeca in cobra[1:]:
        rodando = False

    if nova_cabeca[0] < 0 or nova_cabeca[0] >= 800:
        rodando = False
    
    if nova_cabeca[1] < 0 or nova_cabeca[1] >= 600:
        rodando = False

    desenhar()
    clock.tick(15)

pygame.quit()