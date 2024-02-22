import pygame

# Initialize Pygame
pygame.init()

# Set screen size (adjust width and height as needed)
screen_width = 1350
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set black background color
background_color = (0, 0, 0)

# Set circle properties
circle_radius = 50  # cm converted to pixels (assuming 100 pixels/cm)
circle_color = (255, 255, 255)  # White

# Set initial position (center of the screen)
circle_x = 100
circle_y = 100

# Set movement speeds
fast_speed = 1
slow_speed = 5
very_slow_speed = 2

# Set movement state (initially fast)
movement_state = "very_slow"

# Flag for running the program
running = True

# Main loop
while running:
    # Check for events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle position based on movement state
    if movement_state == "fast":
        circle_x += fast_speed
        circle_y += fast_speed
    elif movement_state == "slow":
        circle_x += slow_speed
        circle_y += slow_speed
    elif movement_state == "very_slow":
        circle_x += very_slow_speed
        circle_y += very_slow_speed

    # Check for edge collisions and bounce back
    if circle_x + circle_radius > screen_width or circle_x - circle_radius < 0:
        circle_x = 100
        # circle_x -= fast_speed  # Reverse horizontal movement
    if circle_y + circle_radius > screen_height or circle_y - circle_radius < 0:
        circle_y = 100
        # circle_y -= fast_speed  # Reverse vertical movement

    # # Change movement state after reaching certain positions
    # if circle_x > screen_width * 0.25:
    #     movement_state = "slow"
    # elif circle_x < screen_width * 0.25:
    #     movement_state = "fast"
    # elif circle_y > screen_height * 0.25:
    #     movement_state = "very_slow"
    # elif circle_y < screen_height * 0.25:
    #     movement_state = "slow"

    # Fill the screen with background color
    screen.fill(background_color)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
