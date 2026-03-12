import pygame
import random
import sys

pygame.init()

# Get the real screen size from the device
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

# Create fullscreen window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Star Screensaver")

clock = pygame.time.Clock()

STAR_COUNT = 2000
MAX_SPEED = 100


class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.5, MAX_SPEED)

    def update(self):
        self.y += self.speed

        # Respawn at top when leaving bottom
        if self.y > HEIGHT:
            self.x = random.randint(0, WIDTH)
            self.y = 0
            self.speed = random.uniform(0.5, MAX_SPEED)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 2)


# Create stars
stars = [Star() for _ in range(STAR_COUNT)]

# Main loop
while True:

    # Handle quit event only
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for star in stars:
        star.update()
        star.draw()

    pygame.display.flip()
    clock.tick(500)