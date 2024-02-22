import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH, HEIGHT = 1400, 900

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the diameter of the round object
DIAMETER = 40

# Set the initial position of the round object
x = 100
y = 300

# Set the velocity of the round object (pixels per second)
velocity = 2 / 100

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Object")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Calculate the total time for movement (in milliseconds)
total_time = 60000  # 60 seconds in milliseconds

# Main loop
start_time = pygame.time.get_ticks()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate elapsed time since start (in milliseconds)
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Clear the screen
    screen.fill(BLACK)

    # Draw the white round object
    pygame.draw.circle(screen, WHITE, (round(x), round(y)), DIAMETER // 2)

    # Update the position of the round object based on elapsed time
    if elapsed_time < total_time:
        distance_moved = velocity * (elapsed_time / 1000)  # Convert milliseconds to seconds
        x += distance_moved
    else:
        x += velocity * (total_time / 1000)  # Move the object to its final position

    # Check for edge collisions and bounce back
    if x + DIAMETER > WIDTH or x - DIAMETER < 0:
        x = 100
    if y + DIAMETER > HEIGHT or y - DIAMETER < 0:
        y = 100

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)
