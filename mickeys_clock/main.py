import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))

bg = pygame.image.load("images/main-clock.png")
sec_img = pygame.image.load("images/left-hand.png")
min_img = pygame.image.load("images/right-hand.png")

def rotate(img, angle):
    rotated_img = pygame.transform.rotate(img, angle)
    rect = rotated_img.get_rect(center=(400, 400))
    return rotated_img, rect

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t = datetime.datetime.now()
    # Углы для стандартных картинок из лабы
    s_angle = -t.second * 6 + 90
    m_angle = -t.minute * 6 + 90

    screen.blit(bg, (0, 0))
    
    img_s, r_s = rotate(sec_img, s_angle)
    img_m, r_m = rotate(min_img, m_angle)

    screen.blit(img_m, r_m)
    screen.blit(img_s, r_s)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()