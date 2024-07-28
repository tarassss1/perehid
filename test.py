import pygame
import sys
import math

# Ініціалізація Pygame
pygame.init()

# Розміри екрану
screen_width = 800
screen_height = 600

# Створення екрану
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Штучний інтелект - Переслідування гравця')

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player1 = pygame.Rect(100,100,50,50)
player2 = pygame.Rect(200,200,50,50)

# Швидкість гравця та ворога
player_speed = 5
enemy_speed = 3


# Основний цикл програми
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    # Отримання натиснутих клавіш
    keys = pygame.key.get_pressed()
    
    # Рух гравця
    if keys[pygame.K_LEFT]:
        player1.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player1.x += player_speed
    if keys[pygame.K_UP]:
        player1.y -= player_speed
    if keys[pygame.K_DOWN]:
        player1.y += player_speed

    # Розрахунок напрямку до гравця
    dx = player1.x - player2.x
    dy = player1.y - player2.y
    dist = math.hypot(dx, dy)
    
    # Нормалізація вектора та рух ворога
    if dist != 0:
        dx /= dist
        dy /= dist
    player2.x += dx * enemy_speed
    player2.y += dy * enemy_speed

    # Очищення екрану
    screen.fill(BLACK)
    
    # Малювання гравця та ворога
    pygame.draw.rect(screen, BLUE, (int(player1.x), int(player1.y)))
    pygame.draw.rect(screen, RED, (int(player2.x), int(player2.y)))
    
    # Оновлення екрану
    pygame.display.flip()

    # Затримка для стабільної швидкості кадрів
    pygame.time.delay(30)
