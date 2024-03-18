import pygame

pygame.init()

width = 800
height = 600 
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Circle')

red = (255,0,0) 

radius = 25 # Радиус круга
speed = 20 # Скорость круга

x = width // 2
y = height // 2 
# Установил максимумы, их можно изменить, но я сделал так, чтобы только часть круга выходило, если -20 не делать, то до центра круг выходит за экран
max_x = width - 20 # Максимум до которого может дойти круг по y - координате 
max_y = height - 20 # максимум до которого может дойти круг по x - координате
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Двигает мяч с нажатием клавиш, но регирует только один раз, а на нажатие нет
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y > 20:
                y-=speed
                if event.key == pygame.K_UP and y < 20:
                    y = 0
            elif event.key == pygame.K_DOWN and y < max_y:
                y+=speed
                if event.key == pygame.K_DOWN and y > max_y:
                    y = 0
            elif event.key == pygame.K_RIGHT and x < max_x:
                x +=speed
                if event.key == pygame.K_RIGHT and x > max_x:
                    x = 0
            elif event.key == pygame.K_LEFT and x > 20:
                x -=speed
                if event.key == pygame.K_LEFT and x < 20:
                    x = 0
       
    """
    #А этот код позволяет, двигать мяч зажимая клавишы, но скорость передвижения может менятся из за зажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 20 :
        y-= speed
        if keys[pygame.K_UP] and y < 20:
            y += speed
    elif keys[pygame.K_DOWN] and y < max_y:
        y += speed
        if keys[pygame.K_DOWN] and y > max_y :
            y-=speed
    elif keys[pygame.K_RIGHT] and x < max_x:
        x += speed
        if keys[pygame.K_RIGHT] and x > max_x:
            x -=speed
    elif keys[pygame.K_LEFT] and x > 20 :
        x -= speed
        if keys[pygame.K_LEFT] and x < 20:
            x +=speed
    """
    screen.fill((255,255,255))
    pygame.draw.circle(screen,red, (x,y), radius)
    pygame.display.update()
    pygame.time.Clock().tick(240)

pygame.quit()