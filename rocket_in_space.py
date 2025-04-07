import pygame
WIDTH = 600
HIEGHT = 600
TITLE = "rocket in space"

screen = pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption(TITLE)
rocket = pygame.image.load("rocket.png")
space_background = pygame.image.load("space background!.png")
run = True
x = 300
y = 300
while run == True:
    screen.blit(space_background,(0,0)) 
    screen.blit(rocket,(x,y))
    #press and hold the key will work
    key_pressed = pygame.key.get_pressed() 
    if key_pressed[pygame.K_LEFT]:
        x = x -10
    if key_pressed[pygame.K_RIGHT]:
        x = x +10 
    if key_pressed[pygame.K_UP]:
        y = y -10
    if key_pressed[pygame.K_DOWN]:
        y = y +10
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            #press and moving not work
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x -10
            if event.key == pygame.K_RIGHT:
                x = x +10
            if event.key == pygame.K_UP:
                y = y -10
            if event.key == pygame.K_DOWN:
                y = y +10

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 400:
        x = 400
    if y > 400:
        y = 400
    
    
    



    pygame.display.update()




