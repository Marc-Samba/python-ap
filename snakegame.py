import pygame

pygame.init()
screenwidth=400
screenheight=300
color=(255,255,255)
fps=20
screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()

for i in range (0,screenwidth,40):
    for j in range (0, screenheight,40):
        rect = pygame.Rect(i, screenheight-j , 20, 20)
        pygame.draw.rect(screen, (0,0,0), rect)

while True:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.QUIT()

    screen.fill(color)
    ligne=15
    colonne=20
    taillecase=screenwidth//colonne
    for i in range (ligne):
        for j in range (colonne):
            if (i+j)%2==0:
                rect= pygame.Rect(taillecase*j, taillecase*i , taillecase, taillecase)
                pygame.draw.rect(screen, (0,0,0), rect)
            else:
                rect= pygame.Rect(taillecase*j, taillecase*i , taillecase, taillecase)
                pygame.draw.rect(screen, (255,255,255), rect)

    pygame.display.update()
