import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

x, y = width // 2, height // 2
radius = 25
step = 20

run = True
clock = pygame.time.Clock()

while run:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - step >= radius:
                y -= step
            if event.key == pygame.K_DOWN and y + step <= height - radius:
                y += step
            if event.key == pygame.K_LEFT and x - step >= radius:
                x -= step
            if event.key == pygame.K_RIGHT and x + step <= width - radius:
                x += step

    pygame.display.flip()
    clock.tick(60)

pygame.quit()