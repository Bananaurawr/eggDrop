import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() * 0.75)
basket_img = pygame.image.load("basket.png").convert_alpha()
basket_rect = basket_img.get_rect(center=player_pos)

egg_img = pygame.image.load("apple.png").convert_alpha()

eggs = []
score = 0
spawn_timer = 0
SPAWN_INTERVAL = 1.5  # a new egg every 1.5 seconds

def spawn_egg(screen_width):
    return {
        "x": random.randint(20, screen_width - 20),
        "y": 0,
        "speed": random.uniform(150, 300),
        "type": "normal"
    }

def update_eggs(eggs, dt, screen_height):
    for egg in eggs:
        egg["y"] += egg["speed"] * dt
    return [egg for egg in eggs if egg["y"] < screen_height]

def check_catch(eggs, basket_rect):
    caught = 0
    remaining = []
    for egg in eggs:
        egg_rect = pygame.Rect(egg["x"], egg["y"], 40, 40)
        if egg_rect.colliderect(basket_rect):
            caught += 1
        else:
            remaining.append(egg)
    return remaining, caught

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("dark green")

    # spawn eggs on a timer
    spawn_timer += dt
    if spawn_timer >= SPAWN_INTERVAL:
        eggs.append(spawn_egg(screen.get_width()))
        spawn_timer = 0

    # move and draw eggs
    eggs = update_eggs(eggs, dt, screen.get_height())
    eggs, caught = check_catch(eggs, basket_rect)
    score += caught

    for egg in eggs:
        screen.blit(egg_img, (egg["x"], egg["y"]))

    # move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 500 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 500 * dt
    player_pos.x = max(20, min(player_pos.x, screen.get_width() - 20))

    basket_rect.center = player_pos
    screen.blit(basket_img, basket_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()