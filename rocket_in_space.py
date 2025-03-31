import pygame
WIDTH = 600
HIEGHT = 600
TITLE = "rocket in space"

screen = pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption(TITLE)
rocket = pygame.image.load("rocket.png")
space_background = pygame.image.load("space background!.png")
run = True

while run == True:
    screen.blit(space_background,(0,0)) 
    screen.blit(rocket,(300,300))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()




