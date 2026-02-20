import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Run until the user asks to quit
running = True
while running:
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))

    # Draw a blue circle
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 75)

    # Draw a green line
    pygame.draw.line(screen, (0, 255, 0), (600, 100), (600, 500), 5)

    # Update the display
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()