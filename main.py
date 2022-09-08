import pygame
import pygame.locals

pygame.init()

screen = pygame.display.set_mode((1000, 800))
background = pygame.image.load('resources/background.jpg')

snake_img = pygame.image.load('resources/snake_head.png')
snake_x = 100
snake_y = 100

def snake():
    screen.blit(snake_img,(snake_x,snake_y))
    pygame.display.flip()


running = True

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# snake movement when arrow key is pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            snake_y -= 0.5
            snake()
        if event.key == pygame.K_DOWN:
            snake_y += 0.5
            snake()
        if event.key == pygame.K_LEFT:
            snake_x -= 0.5
            snake()
        if event.key == pygame.K_RIGHT:
            snake_x += 0.5
            snake()

 # continual snake movement when arrow keys released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            snake_y -= 0.5
            snake()
        if event.key == pygame.K_DOWN:
            snake_y += 0.5
            snake()
        if event.key == pygame.K_LEFT:
            snake_x -= 0.5
            snake()
        if event.key == pygame.K_RIGHT:
            snake_x += 0.5
            snake()



    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    snake()
    pygame.display.update()
