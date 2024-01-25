import pygame

#I dont know what this does - maybe look at it later
pygame.init()

#Creates a window of size 1280,720
screen = pygame.display.set_mode((1280, 720))
#Keeps track of game time
clock = pygame.time.Clock()
running = True

while running:

    #Every frame we check the list of events, there are events such as button or moust pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Fill the screen
    screen.fill('pink')

    #First step is to draw the board
    #Break the problem down
    #Board is made up of singular cells
    #Cell is made up of a square and a then a circle on top.
    #So we figure out how to draw one square first
    #Then how do we draw a circle on top of that
    #How do we repeat this code to draw multiple cells 
    #How do we get this into a board shape

    #Confusing name, but this draws all the stuff to the display
    pygame.display.flip()
    #Keeps fps at 60
    clock.tick(60)

pygame.quit()