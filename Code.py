# cargame-for-exam.-py

import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game For Practical Exam")

# Load images
car_img = pygame.image.load("car.png").convert_alpha()
car_img = pygame.transform.rotate(car_img, 90)  # Rotate 90 degrees left
car_img = pygame.transform.scale(car_img, (60, 90))  # Decrease size

obstacle_img = pygame.image.load("obstacle.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (80, 50))

# Set car properties
car_pos = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT-120)
car_speed = 8

# Set obstacle properties
obstacle_pos = pygame.Vector2(random.randint(0, SCREEN_WIDTH-80), -80)
obstacle_speed = 1

# Set score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_pos.x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_pos.x += car_speed

    # Move obstacle
    obstacle_pos.y += obstacle_speed
    if obstacle_pos.y > SCREEN_HEIGHT:
        obstacle_pos.x = random.randint(0, SCREEN_WIDTH-80)
        obstacle_pos.y = -80
        score += 1

    # Check for collision
    car_rect = pygame.Rect(car_pos.x, car_pos.y, car_img.get_width(), car_img.get_height())
    obstacle_rect = pygame.Rect(obstacle_pos.x, obstacle_pos.y, obstacle_img.get_width(), obstacle_img.get_height())
    if car_rect.colliderect(obstacle_rect):
        pygame.quit()
        quit()

    # Draw images and text
    screen.fill((255, 255, 255))
    screen.blit(car_img, car_pos)
    screen.blit(obstacle_img, obstacle_pos)
    screen.blit(font.render("Score: " + str(score), True, (0, 0, 0)), (10, 10))

    # Update screen
    pygame.display.update()
