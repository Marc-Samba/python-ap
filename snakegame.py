"""import pygame
import operator
pygame.init()
screenwidth=400
screenheight=300
color=(255,255,255)
snake_color=(0,255,0)
fps=20
screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()


screen.fill(color)
ligne=15
colonne=20
taillecase=screenwidth//colonne
RIGHT=(1,0)
LEFT=(-1,0)
UP=(0,1)
DOWN=(0,-1)
snake_dir = RIGHT



serpent=[pygame.Rect(taillecase*5,taillecase*9,20,20),pygame.Rect(taillecase*6,taillecase*9,20,20),pygame.Rect(taillecase*7,taillecase*9,20,20)]
ind_ligne=[10,10,10]
ind_colonne=[6,7,8]
n=len(ind_ligne) #longueur du serpent

flag=True
while flag==True:

    clock.tick(fps)
    
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                pygame.QUIT()

            elif event.key == pygame.K_UP:
                snake_dir = UP
            elif event.key == pygame.K_DOWN:
                snake_dir = DOWN
            elif event.key == pygame.K_RIGHT:
                snake_dir = RIGHT
            elif event.key == pygame.K_LEFT:
                snake_dir = LEFT
            #
            #serpent.append(pygame.Rect(20*(ind_colonne[-1]+direction[0],20*ind_ligne[-1],20,20)))
                    
    for i in range (ligne): #affichage du quadrillage
        for j in range (colonne):
            if (i+j)%2==0:
                rect= pygame.Rect(taillecase*j, taillecase*i , taillecase, taillecase)
                pygame.draw.rect(screen, (0,0,0), rect)
            else:
                rect= pygame.Rect(taillecase*j, taillecase*i , taillecase, taillecase)
                pygame.draw.rect(screen, (255,255,255), rect)       
    for i in range(n):
                pygame.draw.rect(screen, (0,255,0),serpent[i])
    pygame.display.update()

    serpent.pop(0) # Remove queue
    head = tuple(map(operator.add, serpent[-1], snake_dir)) # Compute new head
    serpent.append(head) """




import operator
import pygame

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
TILE_SIZE = 20
# *** EXPLANATION ***
# WE INCREASE SPEED AND THUS MAKE THE GAME LESS ANNOYING.
# *******************
FPS = 5 # Frame per second to display
BG_COLOR_1 = (255, 255, 255) # Background color 1
BG_COLOR_2 = (0, 0, 0) # Background color 2
SNAKE_COLOR = (0, 255, 0)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Global variables
snake = [(5, 10), (6, 10), (7, 10)]
#        Queue              Head
# *** EXPLANATION ***
# NOW WE NEED A MOVING DIRECTION FOR THE SNAKE.
# *******************
snake_dir = RIGHT

# Initialize the Pygame library.
# This is a special step needed by Pygame. Most (99%) libraries do not need an
# initialization step.
pygame.init()

# Create a screen for display, choosing its size (width x height).
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a clock object that we will use to control the speed of our game.
clock = pygame.time.Clock()

# Loop forever
running = True
while running:
    
    # Wait 1/FPS of a second, starting from last display or now
    clock.tick(FPS)
    
    # Process new events (keyboard, mouse)
    for event in pygame.event.get():
        
        # Catch selection of exit icon (Window "cross" icon)
        if event.type == pygame.QUIT:
            running = False

        # Catch a key press
        elif event.type == pygame.KEYDOWN:
            
            # "Q" key has been pressed
            if event.key == pygame.K_q:
                running = False
    
            # *** EXPLANATION ***
            # NOW WE CATCH THE PRESSES ON ARROW KEYS.
            # *******************
            elif event.key == pygame.K_UP:
                snake_dir = UP
            elif event.key == pygame.K_DOWN:
                snake_dir = DOWN
            elif event.key == pygame.K_RIGHT:
                snake_dir = RIGHT
            elif event.key == pygame.K_LEFT:
                snake_dir = LEFT
            
    # Draw the checkerboard
    # Compute number of rows and columns
    n = SCREEN_WIDTH // TILE_SIZE
    m = SCREEN_HEIGHT // TILE_SIZE
    # Loop on all rows and columns
    for i in range(n):
        for j in range(m):
            
            # Alternate color
            tile_color = BG_COLOR_1 if (i + j) % 2 == 0 else BG_COLOR_2
            
            # Compute rectangle
            tile_rect = pygame.Rect(i * TILE_SIZE, j * TILE_SIZE,
                    TILE_SIZE, TILE_SIZE)
            
            # Draw tile
            pygame.draw.rect(screen, tile_color, tile_rect)

    # Update snake position
    # *** EXPLANATION ***
    # WE MAKE THE SNAKE MOVE BY ADDING A HEAD AND REMOVING THE QUEUE.
    # *******************
    del(snake[0]) # Remove queue
    new_head = tuple(map(operator.add, snake[-1], snake_dir)) # Compute new head
    snake.append(new_head)
    # Draw snake
    # Loop on all snake cells
    for c in snake:
        
        # Compute rectangle
        tile_rect = pygame.Rect(c[0] * TILE_SIZE, c[1] * TILE_SIZE,
                TILE_SIZE, TILE_SIZE)
        
        # Draw tile
        pygame.draw.rect(screen, SNAKE_COLOR, tile_rect)

    FRUIT=pygame.Rect(3*TILE_SIZE, TILE_SIZE*3 , TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen,(255,0,0),FRUIT)
    # Display the screen
    pygame.display.update()

# Turn off Pygame
pygame.quit()