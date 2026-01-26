import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() * 0.75)

basket_img = pygame.image.load("basket.png").convert_alpha()
basket_rect = basket_img.get_rect(center=player_pos)

while running:
    # Handle events
    # pygame.QUIT means the used clicked the window's "X" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop on window close
    
    # Fill the screen with a color
    screen.fill("dark green") # Clear the screen with purple color

    basket_rect.center = player_pos
    screen.blit(basket_img, basket_rect) # Draw the basket at the player's position

    keys = pygame.key.get_pressed() # Get the state of all keyboard buttons
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 500 * dt # Move left
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 500 * dt # Move right
    
    # Clamp player position to screen boundaries
    player_pos.x = max(20, min(player_pos.x, screen.get_width() - 20))

    pygame.display.flip() # Update the display
    dt = clock.tick(60) / 1000 # Limit to 60 frames per second

pygame.quit()