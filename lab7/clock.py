import pygame
import sys
from datetime import datetime

width, height = 1400, 1000
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Mickey Clock')
background_image = pygame.image.load('mainclock.png')
right_arm = pygame.image.load('leftarm.png')
left_arm = pygame.image.load('rightarm.png')

clock_center = (width // 2, height // 1.9)

l_rect = left_arm.get_rect(center=clock_center)
r_rect = right_arm.get_rect(center=clock_center)

clock = pygame.time.Clock()

current_time = datetime.now().time()
sec = current_time.second 
min = current_time.minute

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    min_angle = min * 6 + 54
    sec_angle = sec * 6 + 5

    rot_l= pygame.transform.rotate(left_arm, -min_angle)
    rot_r = pygame.transform.rotate(right_arm, -sec_angle)

    rot_l_rect = rot_l.get_rect(center=l_rect.center)
    rot_r_rect = rot_r.get_rect(center=r_rect.center)

    screen.blit(background_image, (0, 0))
    screen.blit(rot_l, rot_l_rect)
    screen.blit(rot_r, rot_r_rect)
    pygame.display.flip()

    clock.tick(1)
    if sec < 59:
        sec+=1
    else:
        sec = 0
        min+=1
    print(min, sec)


