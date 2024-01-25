import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('pink')

    #First step is to draw the board
    #Break the problem down
    #Board is made up of singular cells
    #Cell is made up of a square and a then a circle on top.
    #So we figure out how to draw one square first
    #Then how do we draw a circle on top of that
    #How do we repeat this code to draw multiple cells 
    #How do we get this into a board shape

    pygame.display.flip()
    clock.tick(60)

pygame.quit()