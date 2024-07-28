import pygame
import main
import math
pygame.init()

picture1 = pygame.image.load("photo.jpeg")
picture1 = pygame.transform.scale(picture1,(600,400))
picture2 = pygame.image.load("back2.jpg") 

enemy1 = pygame.Rect(250,250,50,50)
screen = "center"

window = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
player = main.Player((150,150))
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.events(event)
    window.fill((0,0,0))

    

    if player.rect.x < -50 and screen == "center":
        player.rect.x = 550
        screen = "left"
    elif player.rect.x > 550 and screen == "left":
        player.rect.x = 0
        screen = "center"

    
    

    
    if screen == "center":
        window.blit(picture1, (0,0))
    elif screen == "left":
        window.blit(picture2,(0,0))

    dx = player.rect.x - enemy1.x
    dy = player.rect.y - enemy1.y 

    dist = math.hypot(dx, dy)

    if dist != 0:
        dx /= dist
        dy /= dist

    enemy1.x += dx * 2
    enemy1.y += dy * 2

    window.blit(player.image, player.rect)
    pygame.draw.rect(window,(255,0,0),enemy1)

    clock.tick(30)
    pygame.display.update()